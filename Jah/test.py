import utime
from motor import DCMotor
from robot_drive import DifferentialDrive
from machine import Pin
import time

ir_right = Pin(6, Pin.IN)
ir_left = Pin(7, Pin.IN)


utime.sleep_ms(2000)  # USB safety delay

left_motor = DCMotor(2, 3, 4)
right_motor = DCMotor(6, 7, 8)

robot = DifferentialDrive(left_motor, right_motor)

while True:
    

    robot.set_speed(0.5, 0.3)   # turn right
    utime.sleep(2)

    robot.stop()
    utime.sleep(2)
    if ir_right.value() == 0:
        if ir_left.value() == 0: # IR receivers usually go LOW when detecting signal
            robot.set_speed(0.5, 0.0)   # straight
            utime.sleep(2)
        else:
            robot.set_speed(0.5, 0.3)   # turn right
            utime.sleep(2)
    else:
        if ir_left.value() == 0: # IR receivers usually go LOW when detecting signal
            robot.set_speed(0.5, -0.3)   # turn left(?)
            utime.sleep(2)
        else:
            robot.set_speed(0.0, 0.0)   # turn left(?)
            utime.sleep(2)
