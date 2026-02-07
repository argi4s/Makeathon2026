from machine import Pin, PWM

class DCMotor:
    def __init__(self, in1_pin, in2_pin, pwm_pin, pwm_freq=1000):
        self.in1 = Pin(in1_pin, Pin.OUT)
        self.in2 = Pin(in2_pin, Pin.OUT)
        self.pwm = PWM(Pin(pwm_pin))
        self.pwm.freq(pwm_freq)
        self.stop()

    def set_speed(self, speed):
        """
        speed ∈ [-1.0, 1.0]
        """
        speed = max(-1.0, min(1.0, speed))

        if speed > 0:
            self.in1.value(1)
            self.in2.value(0)
        elif speed < 0:
            self.in1.value(0)
            self.in2.value(1)
        else:
            self.in1.value(0)
            self.in2.value(0)

        self.pwm.duty_u16(int(abs(speed) * 65535))

    def stop(self):
        self.in1.value(0)
        self.in2.value(0)
        self.pwm.duty_u16(0)
