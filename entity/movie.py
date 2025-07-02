# Task 5
from entity.event import Event


class Movie(Event):
    def __init__(self, event_name="", event_date=None, event_time=None, venue=None,
                 total_seats=0, available_seats=0, ticket_price=0.0,
                 genre="", actor_name="", actress_name=""):
        super().__init__(event_name, event_date, event_time, venue,
                         total_seats, available_seats, ticket_price, "Movie")
        self.__genre = genre
        self.__actor_name = actor_name
        self.__actress_name = actress_name

    @property
    def genre(self):
        return self.__genre

    @genre.setter
    def genre(self, value):
        self.__genre = value

    @property
    def actor_name(self):
        return self.__actor_name

    @actor_name.setter
    def actor_name(self, value):
        self.__actor_name = value

    @property
    def actress_name(self):
        return self.__actress_name

    @actress_name.setter
    def actress_name(self, value):
        self.__actress_name = value

    def display_event_details(self):
        super().display_event_details()
        print(f"Genre: {self.__genre}")
        print(f"Starring: {self.__actor_name} and {self.__actress_name}")

    def __str__(self):
        return f"Movie: {self.event_name} ({self.__genre})"