from dao.booking_service_provider import IBookingSystemServiceProvider
from dao.event_service_provider_impl import EventServiceProviderImpl
from exception.event_not_found_exception import EventNotFoundException
from exception.invalid_booking_id_exception import InvalidBookingIDException
from typing import List, Dict, Any


class BookingSystemServiceProviderImpl(EventServiceProviderImpl, IBookingSystemServiceProvider):
    def __init__(self):
        super().__init__()
        self.bookings: List['Booking'] = []  # String literal for type hint
        self.__booking_counter = 1000

    def calculate_booking_cost(self, event_name, num_tickets):
        for event in self.events:
            if event.event_name == event_name:
                return event.ticket_price * num_tickets
        raise EventNotFoundException(event_name)

    def book_tickets(self, event_name, num_tickets, customer):
        from entity.booking import Booking  # Local import

        for event in self.events:
            if event.event_name == event_name:
                if event.book_tickets(num_tickets):
                    booking_id = f"B{self.__booking_counter}"
                    self.__booking_counter += 1
                    booking = Booking(booking_id, customer, event, num_tickets)
                    self.bookings.append(booking)
                    return booking
                raise Exception("Not enough tickets available")
        raise EventNotFoundException(event_name)

    def cancel_booking(self, booking_id):
        for booking in self.bookings:
            if booking.booking_id == booking_id:
                if booking.event.cancel_booking(booking.num_tickets):
                    self.bookings.remove(booking)
                    return True
                return False
        raise InvalidBookingIDException(booking_id)

    def get_booking_details(self, booking_id):
        for booking in self.bookings:
            if booking.booking_id == booking_id:
                return booking
        raise InvalidBookingIDException(booking_id)