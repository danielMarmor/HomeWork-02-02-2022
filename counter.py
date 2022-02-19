
import threading
import datetime
import time


class Counter(threading.Thread):
    _MAX_VALUE = 30

    def __init__(self, name, increment):
        threading.Thread.__init__(self)
        self.name = name
        self.increment = increment
        self.count_value = 0

    def run(self) -> None:
        self.start_count()

    def start_count(self):
        while True:
            if self.count_value > Counter._MAX_VALUE:
                break
            print(f'Thread {self.name}, Time {datetime.datetime.now()}, count={self.count_value}')
            self.count_value += self.increment
            time.sleep(0.5)







