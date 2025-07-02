class EventNotFoundException(Exception):
    def __init__(self, event_name):
        super().__init__(f"Event '{event_name}' not found!")
        self.event_name = event_name