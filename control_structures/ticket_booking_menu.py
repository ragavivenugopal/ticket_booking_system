from control_structures.ticket_availability import check_ticket_availability
from control_structures.ticket_cost_calculator import calculate_ticket_cost


def display_menu():
    while True:
        print("\nTicket Booking System - Control Structures Demo")
        print("1. Check Ticket Availability")
        print("2. Calculate Ticket Cost")
        print("3. Exit")

        choice = input("Enter your choice (1-3): ")

        if choice == "1":
            available = int(input("Enter available tickets: "))
            booking = int(input("Enter tickets to book: "))
            success, message, _ = check_ticket_availability(available, booking)
            print(message)
        elif choice == "2":
            print("\nTicket Categories:")
            print("1. Silver - ₹100")
            print("2. Gold - ₹200")
            print("3. Diamond - ₹500")
            category = input("Enter category (Silver/Gold/Diamond): ")
            num_tickets = int(input("Enter number of tickets: "))
            success, message, _ = calculate_ticket_cost(category, num_tickets)
            print(message)
        elif choice == "3":
            print("Thank you for using the Ticket Booking System!")
            break
        else:
            print("Invalid choice. Please try again.")