from counter import Counter
import threading


def init_counters():
    counter_1 = Counter('counter_1', 1)
    counter_2 = Counter('counter_2', 2)
    counter_3 = Counter('counter_3', 3)

    counter_1.start()
    counter_2.start()
    counter_3.start()


init_counters()