# Class and Object - Task 4
# Has-A Relation/Association - Task 7
# Collection - Task 10
from datetime import datetime


class Booking:
    def __init__(self, booking_id, customer, event, num_tickets):
        self.__booking_id = booking_id
        self.__customer = customer
        self.__event = event
        self.__num_tickets = num_tickets
        self.__total_cost = event.ticket_price * num_tickets
        self.__booking_date = datetime.now()

    @property
    def booking_id(self):
        return self.__booking_id

    @property
    def customer(self):
        return self.__customer

    @property
    def event(self):
        return self.__event

    @property
    def num_tickets(self):
        return self.__num_tickets

    @property
    def total_cost(self):
        return self.__total_cost

    @property
    def booking_date(self):
        return self.__booking_date

    def display_booking_details(self):
        print(f"Booking ID: {self.__booking_id}")
        print("\nCustomer Details:")
        self.__customer.display_customer_details()
        print("\nEvent Details:")
        self.__event.display_event_details()
        print(f"\nNumber of Tickets: {self.__num_tickets}")
        print(f"Total Cost: ₹{self.__total_cost}")
        print(f"Booking Date: {self.__booking_date}")