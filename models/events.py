from models.event import Event
import datetime

event_1 = Event(datetime.date(2022, 6, 10), 'Python Meeting', 12, 'Glasgow', 'Meeting about Python', True)
event_2 = Event(datetime.date(2022, 6, 11), 'JavaScript Meeting',34 , 'Glasgow', 'Meeting about JavaScript', True)
event_3 = Event(datetime.date(2022, 6, 12), 'Java Meeting', 'Glasgow', 42, 'Meeting about Java', False)

events = [event_1, event_2, event_3]

def add_new_event(event):
    events.append(event)

def find_event(event_name, events):
    for event in events:
        if event.event_name == event_name:
            return event

def delete_event(index, events):
    events.pop(id)