from crypt import methods
from flask import render_template, request

from app import app
from models.event import Event
from models.events import delete_event, events, add_new_event, delete_event

@app.route('/')
def events_index():
    return render_template('index.html', title='Home', events=events)

@app.route('/', methods=['POST'])
def add_task():
    event_date = request.form['date']
    event_name = request.form['name']
    num_of_guests = request.form['num_of_guests']
    room_location = request.form['room_location']
    event_description = request.form['description']
    new_event = Event(event_date, event_name, num_of_guests, room_location, event_description,)
    add_new_event(new_event)
    return render_template('index.html', title='Home', events=events)

@app.route('/delete/<id>', methods=['POST'])
def event_delete(id):
    events.pop(int(id))
    return render_template('index.html', title='Home', events=events)
   