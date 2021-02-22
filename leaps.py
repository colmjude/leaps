import datetime

from bin.dates import add_weeks
from bin.file import read_json_file

from bin.leap import Leap

DUE_DATE = datetime.datetime.strptime("2021-01-02", "%Y-%m-%d")


def leap_dates(due_date, leap_start):
    start_date = add_weeks(due_date, leap_start)
    return start_date


leaps_data = read_json_file("leaps.json")

for n, data in leaps_data.items():
  leap = Leap(n, leap_dates(DUE_DATE, data["start"]), data['name'])
  leap.event()

