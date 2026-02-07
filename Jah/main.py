import utime
from esc_motors import ESCMotor

utime.sleep_ms(2000)  # USB safety delay

motor_left  = ESCMotor(pin=2)
motor_right = ESCMotor(pin=3)

# ARM ESCs (IMPORTANT)
motor_left.stop()
motor_right.stop()
utime.sleep(3)

while True:
    # forward
    motor_left.set_speed(0.6)
    motor_right.set_speed(0.6)
    utime.sleep(2)

    # backward
    motor_left.set_speed(-0.6)
    motor_right.set_speed(-0.6)
    utime.sleep(2)

    # stop
    motor_left.stop()
    motor_right.stop()
    utime.sleep(2)
