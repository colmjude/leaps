

class Leap():
  def __init__(self, num, start, name):
    self.num = num
    self.start = start
    self.name = name

  def print(self):
    print(f"Leap {self.num} - {self.name}")
    print(f"Likely to start: {self.start}")
