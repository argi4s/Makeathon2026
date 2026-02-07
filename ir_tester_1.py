from machine import Pin
import time

ir_right = Pin(6, Pin.IN)
ir_left = Pin(7, Pin.IN)



print("Waiting for IR signals...")

while True:
    if ir_right.value() == 0:
        if ir_left.value() == 0: # IR receivers usually go LOW when detecting signal
            print("Both")
        else:
            print("Right")
    else:
        if ir_left.value() == 0: # IR receivers usually go LOW when detecting signal
            print("Left")
        else:
            print("None")
        