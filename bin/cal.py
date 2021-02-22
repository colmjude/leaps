from ics import Calendar, Event, DisplayAlarm
import datetime


def add_alarm():
    return DisplayAlarm(datetime.timedelta(days=0.5))


def ics_event(name, start_date):
    a = add_alarm()
    e = Event(alarms=[a])
    e.name = name
    u = start_date
    e.begin = u
    return e


def create_ics_event(d=None):
    c = Calendar()
    e = ics_event("Leap one", datetime.datetime.strptime("2021-02-05", "%Y-%m-%d"))
    c.events.add(e)

    return c


# print(str(create_ics_event()))
