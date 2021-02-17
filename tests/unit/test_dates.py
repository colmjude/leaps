import datetime

from bin.dates import add_weeks


def test_add_weeks():
    d = "2021-01-05"
    _date = datetime.datetime.strptime(d, "%Y-%m-%d")

    assert add_weeks(_date, 1).strftime("%Y-%m-%d") == "2021-01-12"
    assert add_weeks(_date, 1.5).strftime("%Y-%m-%d") == "2021-01-15"
