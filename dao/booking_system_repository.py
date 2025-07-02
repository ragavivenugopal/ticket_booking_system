# task 11
from util.db_conn_util import DBConnUtil
from util.db_property_util import DBPropertyUtil
from exception.event_not_found_exception import EventNotFoundException
from exception.invalid_booking_id_exception import InvalidBookingIDException
import psycopg2


class BookingSystemRepository:
    def __init__(self):
        self.connection = DBConnUtil.get_connection(property_file_name="db.properties")

    def __del__(self):
        if hasattr(self, 'connection') and self.connection:
            self.connection.close()

    def create_event(self, event):
        try:
            cursor = self.connection.cursor()

            # Insert venue if not exists
            cursor.execute(
                "INSERT INTO Venue (venue_name, address) VALUES (%s, %s) ON CONFLICT (venue_name) DO NOTHING RETURNING venue_id",
                (event.venue.venue_name, event.venue.address)
            )
            venue_id = cursor.fetchone()

            if not venue_id:
                cursor.execute(
                    "SELECT venue_id FROM Venue WHERE venue_name = %s",
                    (event.venue.venue_name,)
                )
                venue_id = cursor.fetchone()

            venue_id = venue_id[0]

            # Insert event
            cursor.execute(
                """INSERT INTO Event (event_name, event_date, event_time, venue_id,
                                      total_seats, available_seats, ticket_price, event_type)
                   VALUES (%s, %s, %s, %s, %s, %s, %s, %s) RETURNING event_id""",
                (event.event_name, event.event_date, event.event_time, venue_id,
                 event.total_seats, event.available_seats, event.ticket_price, event.event_type)
            )

            event_id = cursor.fetchone()[0]
            self.connection.commit()
            return event_id
        except psycopg2.Error as e:
            self.connection.rollback()
            raise e

    def get_all_events(self):
        try:
            cursor = self.connection.cursor()
            cursor.execute("""
                           SELECT e.event_id,
                                  e.event_name,
                                  e.event_date,
                                  e.event_time,
                                  e.total_seats,
                                  e.available_seats,
                                  e.ticket_price,
                                  e.event_type,
                                  v.venue_id,
                                  v.venue_name,
                                  v.address
                           FROM Event e
                                    JOIN Venue v ON e.venue_id = v.venue_id
                           """)
            return cursor.fetchall()
        except psycopg2.Error as e:
            raise e

    def book_tickets(self, event_name, num_tickets, customer):
        try:
            cursor = self.connection.cursor()

            # Check event availability
            cursor.execute(
                "SELECT event_id, available_seats, ticket_price FROM Event WHERE event_name = %s",
                (event_name,)
            )
            event_data = cursor.fetchone()

            if not event_data:
                raise EventNotFoundException(event_name)

            event_id, available_seats, ticket_price = event_data

            if available_seats < num_tickets:
                raise ValueError("Not enough tickets available")

            # Insert customer
            cursor.execute(
                """INSERT INTO Customer (customer_name, email, phone_number)
                   VALUES (%s, %s, %s) ON CONFLICT (email) DO
                UPDATE
                    SET customer_name = EXCLUDED.customer_name,
                    phone_number = EXCLUDED.phone_number
                    RETURNING customer_id""",
                (customer.customer_name, customer.email, customer.phone_number)
            )

            customer_id = cursor.fetchone()[0]

            # Create booking
            total_cost = ticket_price * num_tickets
            cursor.execute(
                """INSERT INTO Booking (customer_id, event_id, num_tickets, total_cost)
                   VALUES (%s, %s, %s, %s) RETURNING booking_id""",
                (customer_id, event_id, num_tickets, total_cost)
            )

            booking_id = cursor.fetchone()[0]

            # Update available seats
            cursor.execute(
                "UPDATE Event SET available_seats = available_seats - %s WHERE event_id = %s",
                (num_tickets, event_id)
            )

            self.connection.commit()
            return booking_id
        except psycopg2.Error as e:
            self.connection.rollback()
            raise e

    # Implement other methods similarly...