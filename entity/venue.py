# Class and Object - Task 4
class Venue:
    def __init__(self, venue_name="", address=""):
        self.__venue_name = venue_name
        self.__address = address

    @property
    def venue_name(self):
        return self.__venue_name

    @venue_name.setter
    def venue_name(self, value):
        self.__venue_name = value

    @property
    def address(self):
        return self.__address

    @address.setter
    def address(self, value):
        self.__address = value

    def display_venue_details(self):
        print(f"Venue Name: {self.__venue_name}")
        print(f"Address: {self.__address}")

    def __str__(self):
        return f"Venue: {self.__venue_name}, {self.__address}"