import datetime

from bin.leap import Leap


def test_leap_event():
    leap = Leap("1", datetime.datetime(2021, 2, 2), "Test leap", 1)
    e = leap.event()

    assert len(leap.event().alarms) == 1
    assert leap.event().alarms[0].trigger.days < 0

    assert e.duration.days == 7

    must_haves = [
        "BEGIN:VEVENT",
        "BEGIN:VALARM",
        "TRIGGER:-PT12H",
        "SUMMARY:Leap 1: Test leap",
        "END:VALARM",
        "DTSTART;VALUE=DATE:20210202",
        "DTEND;VALUE=DATE:20210209",
        "END:VEVENT",
    ]
    for s in must_haves:
        assert s in str(e)
