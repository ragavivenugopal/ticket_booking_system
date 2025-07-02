# Task 5
from entity.event import Event


class Sports(Event):
    def __init__(self, event_name="", event_date=None, event_time=None, venue=None,
                 total_seats=0, available_seats=0, ticket_price=0.0,
                 sport_name="", teams_name=""):
        super().__init__(event_name, event_date, event_time, venue,
                         total_seats, available_seats, ticket_price, "Sports")
        self.__sport_name = sport_name
        self.__teams_name = teams_name

    @property
    def sport_name(self):
        return self.__sport_name

    @sport_name.setter
    def sport_name(self, value):
        self.__sport_name = value

    @property
    def teams_name(self):
        return self.__teams_name

    @teams_name.setter
    def teams_name(self, value):
        self.__teams_name = value

    def display_event_details(self):
        super().display_event_details()
        print(f"Sport: {self.__sport_name}")
        print(f"Teams: {self.__teams_name}")

    def __str__(self):
        return f"Sports: {self.__sport_name} - {self.__teams_name}"