import datetime


def add_weeks(d, weeks):
    days = weeks * 7
    delta = datetime.timedelta(days=days)
    return d + delta


# u = datetime.datetime.strptime("2021-01-02","%Y-%m-%d")
# l1 = add_weeks(u, 4)
