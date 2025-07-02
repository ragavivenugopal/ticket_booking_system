def check_ticket_availability(available_tickets, booking_tickets):
    if available_tickets >= booking_tickets:
        remaining = available_tickets - booking_tickets
        return True, f"Tickets booked successfully! Remaining tickets: {remaining}", remaining
    else:
        return False, "Not enough tickets available!", available_tickets