from ics import Calendar, Event
import datetime

def create_ics_event(d=None):
  c = Calendar()
  e = Event()
  e.name = "Leap one"
  u = datetime.datetime.strptime("2021-01-30","%Y-%m-%d")
  e.begin = u
  c.events.add(e)
  return c.events

print(str(create_ics_event()))

