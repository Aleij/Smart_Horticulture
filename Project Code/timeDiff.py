import time

class TimeDiff:
    def __init__(self, timer):
        self.timer = timer
        self.start_time = time.ticks_ms()

    def check(self):
        if time.ticks_diff(time.ticks_ms(), self.start_time) > self.timer * 1000:
            self.start_time = time.ticks_ms()
            return True
        else:
            return False