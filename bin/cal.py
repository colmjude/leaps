from ics import Calendar, Event, DisplayAlarm
import datetime


def add_alarm():
    return DisplayAlarm(datetime.timedelta(days=0.5))


def create_ics_event(d=None):
    c = Calendar()
    a = add_alarm()
    e = Event(alarms=[a])
    e.name = "Leap one"
    u = datetime.datetime.strptime("2021-02-05", "%Y-%m-%d")
    e.begin = u
    c.events.add(e)

    return c


print(str(create_ics_event()))
