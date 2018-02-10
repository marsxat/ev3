#!/usr/bin/python3

# Parallel Parking Program
# Parallel Parking means the truck will park in a spot next to it's current place by going forward, then
# reversing into the parking spot.
#
# 1: The truck will go forward 3 rotations, then stop.
# 2: The truck's front wheels will turn left (maximum)
# 3: Reverses 1 rotation
# 4: Straighten front wheels
# 5: reverse 2 rotations  reverse( 2.0)
#  6: Turn front wheels right
# 7: Reverse 1 rotation
# 8: Straighten front wheels
# 9: Forward 1 rotation

import ev3dev.ev3 as ev3
import time

gear_ratio = 3.0


def forward(rotations):
    left = ev3.LargeMotor('outB')
    right = ev3.LargeMotor('outC')

    counts = rotations * left.count_per_rot / gear_ratio
    speed = 0.5 * left.count_per_rot / gear_ratio
    #left.max_speed * 0.5
    print(counts)
    print(speed)
    left.run_to_rel_pos(position_sp=counts, speed_sp=speed, ramp_up_sp=1000, ramp_down_sp=1000)
    right.run_to_rel_pos(position_sp=counts, speed_sp=speed, ramp_up_sp=1000, ramp_down_sp=1000)
    left.wait_until_not_moving()
    right.wait_until_not_moving()


def backward(rotations):
    forward(-rotations)


forward(2.0)
time.sleep(1.0)
backward(2.0)