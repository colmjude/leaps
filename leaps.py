import datetime

from bin.dates import add_weeks

def leap_dates(due_date, leap):
  start_date = add_weeks(due_date, leap['start'])
  return start_date

due_date = datetime.datetime.strptime("2021-01-02","%Y-%m-%d")

print(leap_dates(due_date, {'start': 4.5}))