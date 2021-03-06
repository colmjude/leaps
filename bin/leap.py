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
    def __init__(self, due_date, path_to_data="leaps.json"):
        self.due_date = due_date
        self.data_file = path_to_data
        self.data = self.read_csv()

    def read_csv(self):
        return read_json_file(self.data_file, True)

    def calendar(self):
        cal = Calendar()
        for n, data in self.data.items():
            leap = Leap(
                n,
                leap_dates(self.due_date, data["start"]),
                data["name"],
                data["duration"],
            )
            cal.events.add(leap.event())
        return cal


class Leap:
    def __init__(self, num, start, name, duration_in_weeks):
        self.num = num
        self.start = start
        self.name = name
        self.duration_in_weeks = duration_in_weeks

    def event(self):
        # don't double count the start day
        days = math.floor(self.duration_in_weeks * 7) - 1
        event = ics_event(
            f"Leap {self.num}: {self.name}",
            self.start,
            days,
        )
        event.make_all_day()
        return event

    def print(self):
        print(f"Leap {self.num} - {self.name}")
        print(f"Likely to start: {self.start}")
