from ics import Calendar, Event, DisplayAlarm
import datetime


def add_alarm(days):
    # we want alarms before the event so delta needs to be negative
    return DisplayAlarm(datetime.timedelta(days=-days))


# alarm_start in days
def ics_event(name, start_date, duration=None, alarm_start=0.5):
    a = add_alarm(alarm_start)
    e = Event(alarms=[a])
    e.name = name
    u = start_date
    e.begin = u
    if duration:
        d = datetime.timedelta(days=duration)
        e.duration = d
    return e


def create_ics_event(d=None):
    c = Calendar()
    e = ics_event("Leap one", datetime.datetime.strptime("2021-02-05", "%Y-%m-%d"))
    c.events.add(e)

    return c


# print(str(create_ics_event()))
