import utime
from motor import DCMotor
from robot_drive import DifferentialDrive

utime.sleep_ms(2000)  # USB safety delay

left_motor = DCMotor(2, 3, 4)
right_motor = DCMotor(6, 7, 8)

robot = DifferentialDrive(left_motor, right_motor)

while True:
    robot.set_speed(0.5, 0.0)   # straight
    utime.sleep(2)

    robot.set_speed(0.5, 0.3)   # turn right
    utime.sleep(2)

    robot.stop()
    utime.sleep(2)
