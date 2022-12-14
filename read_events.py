
from __future__ import print_function
import time


from inputs import get_gamepad


def main():
    while 1:
        events = get_gamepad()
        for event in events:
            start_time = time.time()
            print(event.ev_type, event.code, event.state)
            print("--- %s seconds ---" % (time.time() - start_time))


if __name__ == "__main__":
    main()