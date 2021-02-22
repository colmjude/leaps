from bin.cal import ics_event


class Leap:
    def __init__(self, num, start, name):
        self.num = num
        self.start = start
        self.name = name

    def event(self):
        print(ics_event(self.name, self.start))

    def print(self):
        print(f"Leap {self.num} - {self.name}")
        print(f"Likely to start: {self.start}")
