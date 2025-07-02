# Interface/Abstract Class - Task 8
from dao.event_service_provider import IEventServiceProvider
from entity.movie import Movie
from entity.concert import Concert
from entity.sports import Sports
from typing import List


class EventServiceProviderImpl(IEventServiceProvider):
    def __init__(self):
        self.events: List['Event'] = []

    def create_event(self, event_name, date, time, total_seats, ticket_price, event_type, venue, **kwargs):
        """Create an event with type-specific parameters"""
        if event_type == "Movie":
            event = Movie(
                event_name, date, time, venue,
                total_seats, total_seats, ticket_price,
                kwargs.get('genre', ''),
                kwargs.get('actor_name', ''),
                kwargs.get('actress_name', '')
            )
        elif event_type == "Concert":
            event = Concert(
                event_name, date, time, venue,
                total_seats, total_seats, ticket_price,
                kwargs.get('artist', ''),
                kwargs.get('concert_type', '')
            )
        elif event_type == "Sports":
            event = Sports(
                event_name, date, time, venue,
                total_seats, total_seats, ticket_price,
                kwargs.get('sport_name', ''),
                kwargs.get('teams_name', '')
            )
        else:
            raise ValueError(f"Invalid event type: {event_type}")

        self.events.append(event)
        return event

    def get_event_details(self):
        return self.events

    def get_available_no_of_tickets(self, event_name):
        for event in self.events:
            if event.event_name == event_name:
                return event.available_seats
        raise Exception(f"Event '{event_name}' not found")