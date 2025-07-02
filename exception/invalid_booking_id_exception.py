# Exception Handling - Task 9
class InvalidBookingIDException(Exception):
    def __init__(self, booking_id):
        super().__init__(f"Invalid booking ID: {booking_id}")
        self.booking_id = booking_id