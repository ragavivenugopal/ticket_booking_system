# Task 5
from entity.event import Event

class Concert(Event):
    def __init__(self, event_name="", event_date=None, event_time=None, venue=None,
                 total_seats=0, available_seats=0, ticket_price=0.0,
                 artist="", concert_type=""):
        super().__init__(event_name, event_date, event_time, venue,
                         total_seats, available_seats, ticket_price, "Concert")
        self.__artist = artist
        self.__concert_type = concert_type

    @property
    def artist(self):
        return self.__artist

    @artist.setter
    def artist(self, value):
        self.__artist = value

    @property
    def concert_type(self):
        return self.__concert_type

    @concert_type.setter
    def concert_type(self, value):
        self.__concert_type = value

    def display_event_details(self):
        super().display_event_details()
        print(f"Artist: {self.__artist}")
        print(f"Concert Type: {self.__concert_type}")

    def __str__(self):
        return f"Concert: {self.event_name} by {self.__artist}"