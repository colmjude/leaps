import datetime

from bin.dates import add_weeks
from bin.file import read_json_file

DUE_DATE = datetime.datetime.strptime("2021-01-02", "%Y-%m-%d")


def leap_dates(due_date, leap):
    start_date = add_weeks(due_date, leap["start"])
    return start_date


leaps_data = read_json_file("leaps.json")

for n, data in leaps_data.items():
    print(f"Leap {n} - {data['name']}")
    print(f"Week {data['start']} ({leap_dates(DUE_DATE, data)})")


# print(leap_dates(DUE_DATE, {"start": 4.5}))
