from abc import ABC, abstractmethod
from datetime import datetime
from entity.venue import Venue


class Event(ABC):
    def __init__(self, event_name="", event_date=None, event_time=None, venue=None,
                 total_seats=0, available_seats=0, ticket_price=0.0, event_type=""):
        self.__event_name = event_name
        self.__event_date = event_date if event_date else datetime.now().date()
        self.__event_time = event_time if event_time else datetime.now().time()
        self.__venue = venue if venue else Venue()
        self.__total_seats = total_seats
        self.__available_seats = available_seats if available_seats else total_seats
        self.__ticket_price = ticket_price
        self.__event_type = event_type

    @property
    def event_name(self):
        return self.__event_name

    @event_name.setter
    def event_name(self, value):
        self.__event_name = value

    @property
    def event_date(self):
        return self.__event_date

    @event_date.setter
    def event_date(self, value):
        self.__event_date = value

    @property
    def event_time(self):
        return self.__event_time

    @event_time.setter
    def event_time(self, value):
        self.__event_time = value

    @property
    def venue(self):
        return self.__venue

    @venue.setter
    def venue(self, value):
        self.__venue = value

    @property
    def total_seats(self):
        return self.__total_seats

    @total_seats.setter
    def total_seats(self, value):
        self.__total_seats = value

    @property
    def available_seats(self):
        return self.__available_seats

    @available_seats.setter
    def available_seats(self, value):
        self.__available_seats = value

    @property
    def ticket_price(self):
        return self.__ticket_price

    @ticket_price.setter
    def ticket_price(self, value):
        self.__ticket_price = value

    @property
    def event_type(self):
        return self.__event_type

    @event_type.setter
    def event_type(self, value):
        self.__event_type = value

    def calculate_total_revenue(self):
        booked_tickets = self.__total_seats - self.__available_seats
        return booked_tickets * self.__ticket_price

    def get_booked_no_of_tickets(self):
        return self.__total_seats - self.__available_seats

    def book_tickets(self, num_tickets):
        if num_tickets <= self.__available_seats:
            self.__available_seats -= num_tickets
            return True
        return False

    def cancel_booking(self, num_tickets):
        if (self.__available_seats + num_tickets) <= self.__total_seats:
            self.__available_seats += num_tickets
            return True
        return False

    @abstractmethod
    def display_event_details(self):
        print(f"Event Name: {self.__event_name}")
        print(f"Date: {self.__event_date}, Time: {self.__event_time}")
        print(f"Venue: {self.__venue.venue_name}")
        print(f"Available Seats: {self.__available_seats}/{self.__total_seats}")
        print(f"Ticket Price: ₹{self.__ticket_price}")
        print(f"Event Type: {self.__event_type}")

    def __str__(self):
        return f"{self.__event_type} Event: {self.__event_name} at {self.__venue.venue_name}"