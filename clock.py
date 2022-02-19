import datetime
import time

import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.widget import Widget
from kivy.clock import Clock
import threading


class ClockThread(threading.Thread):
    # 10 MINUTES === THEN STOP PROGRAM
    _MAX_COUNTER = 600

    def __init__(self, clock):
        self.clock = clock
        self.counter = 0
        threading.Thread.__init__(self)

    def run(self) -> None:
        while True:
            if self.counter > ClockThread._MAX_COUNTER:
                break
            self.clock.show_time()
            self.counter += 1
            time.sleep(1)


class ClockGrid(Widget):
    def __init__(self):
        super(ClockGrid, self).__init__()
        self.init_clock()

    def init_clock(self):
        clock_thread = ClockThread(self)
        clock_thread.start()

    def show_time(self):
        current_time = datetime.datetime.now()
        current_time_str = current_time.strftime("%I:%M:%S")
        self.ids.lblClock.text = current_time_str


class ClockApp(App):
    def build(self):
        return ClockGrid()



if __name__ == "__main__":
    ClockApp().run()


