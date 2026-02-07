from machine import Pin, PWM
import utime

class ESCMotor:
    def __init__(self, pin, freq=50):
        self.pwm = PWM(Pin(pin))
        self.pwm.freq(freq)
        self.stop()

    def _set_us(self, microseconds):
        # 20 ms period → 50 Hz
        duty = int(microseconds * 65535 / 20000)
        self.pwm.duty_u16(duty)

    def set_speed(self, speed):
        """
        speed ∈ [-1.0, 1.0]
        """
        speed = max(-1.0, min(1.0, speed))

        pulse = int(1500 + speed * 500)
        self._set_us(pulse)

    def stop(self):
        self._set_us(1500)
