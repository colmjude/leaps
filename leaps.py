import datetime

from bin.file import read_json_file, write_to_file

from bin.leap import Leaps, Leap

DUE_DATE = datetime.datetime.strptime("2021-01-02", "%Y-%m-%d")

leaps = Leaps(DUE_DATE, "leaps.json")
# print(leaps.calendar())
cal = leaps.calendar()
write_to_file("leaps.ics", str(cal))

# for n, data in leaps_data.items():
#     leap = Leap(n, leap_dates(DUE_DATE, data["start"]), data["name"])
#     leap.event()
