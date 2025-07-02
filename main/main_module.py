from entity.venue import Venue
from entity.customer import Customer
from exception.event_not_found_exception import EventNotFoundException
from exception.invalid_booking_id_exception import InvalidBookingIDException
import sys


class MainModule:
    def __init__(self):
        # Initialize with the service implementation
        from dao.booking_service_provider_impl import BookingSystemServiceProviderImpl
        self.booking_system = BookingSystemServiceProviderImpl()
        self.initialize_sample_events()

    def initialize_sample_events(self):
        try:
            # Sample venues
            arena = Venue("City Arena", "123 Main St")
            theater = Venue("Royal Theater", "456 Broadway")

            # Sample events
            from entity.movie import Movie
            from entity.concert import Concert
            from entity.sports import Sports

            # Create sample events directly through the service
            self.booking_system.create_event(
                "Avengers Premiere", "2023-12-20", "18:30",
                300, 800, "Movie", theater,
                genre="Action", actor_name="Robert Downey Jr.", actress_name="Scarlett Johansson"
            )

            self.booking_system.create_event(
                "Rock Concert", "2023-12-15", "20:00",
                500, 1500, "Concert", arena,
                artist="The Rolling Stones", concert_type="Rock"
            )

            self.booking_system.create_event(
                "Cricket Finals", "2023-11-25", "14:00",
                10000, 1200, "Sports", Venue("Sports Complex", "789 Stadium Rd"),
                sport_name="Cricket", teams_name="India vs Australia"
            )
        except Exception as e:
            print(f"Error initializing sample events: {e}")

    def display_menu(self):
        print("\n==== Ticket Booking System ====")
        print("1. Create Event")
        print("2. View All Events")
        print("3. Book Tickets")
        print("4. View Booking Details")
        print("5. Cancel Booking")
        print("6. Check Available Tickets")
        print("7. Exit")

    def create_event(self):
        print("\n--- Create New Event ---")
        try:
            # Get basic event details
            event_name = input("Enter event name: ")
            event_date = input("Enter event date (YYYY-MM-DD): ")
            event_time = input("Enter event time (HH:MM): ")
            total_seats = int(input("Enter total seats: "))
            ticket_price = float(input("Enter ticket price: "))

            # Get venue details
            print("\nVenue Details:")
            venue_name = input("Enter venue name: ")
            address = input("Enter venue address: ")
            venue = Venue(venue_name=venue_name, address=address)

            # Get event type and type-specific details
            print("\nEvent Types: Movie, Sports, Concert")
            event_type = input("Enter event type: ").capitalize()

            extra_params = {}
            if event_type == "Movie":
                extra_params['genre'] = input("Enter movie genre: ")
                extra_params['actor_name'] = input("Enter lead actor: ")
                extra_params['actress_name'] = input("Enter lead actress: ")
            elif event_type == "Concert":
                extra_params['artist'] = input("Enter artist/band: ")
                extra_params['concert_type'] = input("Enter concert type: ")
            elif event_type == "Sports":
                extra_params['sport_name'] = input("Enter sport name: ")
                extra_params['teams_name'] = input("Enter teams (e.g., TeamA vs TeamB): ")
            else:
                print("Invalid event type!")
                return

            # Create the event through the service
            event = self.booking_system.create_event(
                event_name, event_date, event_time, total_seats,
                ticket_price, event_type, venue, **extra_params
            )
            print(f"\nEvent created successfully! Event Name: {event.event_name}")
        except ValueError as e:
            print(f"Invalid input: {e}")
        except Exception as e:
            print(f"Error creating event: {e}")

    def view_all_events(self):
        print("\n--- All Events ---")
        try:
            events = self.booking_system.get_event_details()
            if not events:
                print("No events available yet.")
                return

            for idx, event in enumerate(events, 1):
                print(f"\nEvent #{idx}:")
                event.display_event_details()
                print("-----------------------")
        except Exception as e:
            print(f"Error retrieving events: {e}")

    def book_tickets(self):
        print("\n--- Book Tickets ---")
        try:
            self.view_all_events()
            event_choice = int(input("\nEnter event number to book: ")) - 1
            events = self.booking_system.get_event_details()

            if event_choice < 0 or event_choice >= len(events):
                raise EventNotFoundException("Invalid event selection")

            selected_event = events[event_choice]
            num_tickets = int(input("Enter number of tickets: "))

            if num_tickets <= 0:
                raise ValueError("Number of tickets must be positive")

            print("\nCustomer Details:")
            customer_name = input("Enter your name: ")
            email = input("Enter your email: ")
            phone = input("Enter your phone: ")
            customer = Customer(customer_name, email, phone)

            booking = self.booking_system.book_tickets(
                selected_event.event_name, num_tickets, customer
            )
            print(f"\nBooking successful! Booking ID: {booking.booking_id}")
            print(f"Total cost: ₹{booking.total_cost:.2f}")
        except EventNotFoundException as e:
            print(f"Error: {e}")
        except ValueError as e:
            print(f"Invalid input: {e}")
        except Exception as e:
            print(f"Error booking tickets: {e}")

    def view_booking_details(self):
        print("\n--- View Booking ---")
        try:
            booking_id = input("Enter booking ID: ")
            booking = self.booking_system.get_booking_details(booking_id)
            print("\nBooking Details:")
            booking.display_booking_details()
        except InvalidBookingIDException as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"Error retrieving booking: {e}")

    def cancel_booking(self):
        print("\n--- Cancel Booking ---")
        try:
            booking_id = input("Enter booking ID to cancel: ")
            if self.booking_system.cancel_booking(booking_id):
                print("Booking cancelled successfully!")
            else:
                print("Failed to cancel booking")
        except InvalidBookingIDException as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"Error cancelling booking: {e}")

    def check_available_tickets(self):
        print("\n--- Available Tickets ---")
        try:
            events = self.booking_system.get_event_details()
            if not events:
                print("No events available yet.")
                return

            print("\nCurrent Availability:")
            for event in events:
                print(f"{event.event_name}: {event.available_seats}/{event.total_seats} available")
        except Exception as e:
            print(f"Error checking availability: {e}")

    def run(self):
        while True:
            self.display_menu()
            choice = input("\nEnter your choice (1-7): ")

            try:
                if choice == "1":
                    self.create_event()
                elif choice == "2":
                    self.view_all_events()
                elif choice == "3":
                    self.book_tickets()
                elif choice == "4":
                    self.view_booking_details()
                elif choice == "5":
                    self.cancel_booking()
                elif choice == "6":
                    self.check_available_tickets()
                elif choice == "7":
                    print("\nThank you for using the Ticket Booking System!")
                    sys.exit()
                else:
                    print("Invalid choice. Please enter a number between 1-7.")
            except Exception as e:
                print(f"\nAn error occurred: {e}")


if __name__ == "__main__":
    app = MainModule()
    app.run()