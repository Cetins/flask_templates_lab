class Event:

    def __init__(self, date, event_name, num_of_guests, room_location, description, recursive):
        self.date = date
        self.event_name = event_name
        self.num_of_guests = num_of_guests
        self.room_location = room_location
        self.description = description
        self.recursive = recursive