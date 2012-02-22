# Test the tracking function of the copter.

import tracker
from helicopter import copter
import time;

# Set center calibaration, assuming it now.
range = 0.5

# set successive samples
sleep_time = 0;

#open up copter.
device=copter('/dev/ttyUSB0', 19200, 0)

def move():
    x,y = tracker.track();

    if x > range:
        if x > 0:
            value = '+'
        else:
            value = '-'
        device.adjust_direction('x', value)

    if y > range:
        if y > 0:
            value = '+'
        else:
            value = '-'

        device.adjust_rotor(value)


if __name__ == "__main__":
    while True:
        move()
        time.sleep(sleep_time)
        
        
