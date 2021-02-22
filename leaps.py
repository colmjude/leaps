import datetime

from bin.file import read_json_file

from bin.leap import Leaps, Leap

DUE_DATE = datetime.datetime.strptime("2021-01-02", "%Y-%m-%d")

leaps = Leaps("leaps.json")
print(leaps.calendar())

# for n, data in leaps_data.items():
#     leap = Leap(n, leap_dates(DUE_DATE, data["start"]), data["name"])
#     leap.event()
