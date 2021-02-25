import datetime
import math

from ics import Calendar

from bin.cal import ics_event
from bin.file import read_json_file
from bin.dates import add_weeks


def leap_dates(due_date, leap_start):
    start_date = add_weeks(due_date, leap_start)
    return start_date


class Leaps:
    DUE_DATE = datetime.datetime.strptime("2021-01-02", "%Y-%m-%d")

    def __init__(self, path_to_data="leaps.json"):
        self.data_file = path_to_data
        self.data = self.read_csv()

    def read_csv(self):
        return read_json_file(self.data_file, True)

    def calendar(self):
        cal = Calendar()
        for n, data in self.data.items():
            duration = math.floor(data["duration"] * 7)
            leap = Leap(
                n, leap_dates(self.DUE_DATE, data["start"]), data["name"], duration
            )
            cal.events.add(leap.event())
        return cal


class Leap:
    def __init__(self, num, start, name, duration):
        self.num = num
        self.start = start
        self.name = name
        self.duration = duration

    def event(self):
        event = ics_event(
            f"Leap {self.num}: {self.name}",
            self.start,
            self.duration,
        )
        event.make_all_day()
        return event

    def print(self):
        print(f"Leap {self.num} - {self.name}")
        print(f"Likely to start: {self.start}")
