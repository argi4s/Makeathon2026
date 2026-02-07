from motor import DCMotor

class DifferentialDrive:
    def __init__(self, left_motor, right_motor):
        self.left = left_motor
        self.right = right_motor

    def set_speed(self, linear, angular):
        """
        linear: forward speed  [-1.0, 1.0]
        angular: turn rate     [-1.0, 1.0]
        """
        left_speed = linear - angular
        right_speed = linear + angular

        self.left.set_speed(left_speed)
        self.right.set_speed(right_speed)

    def stop(self):
        self.left.stop()
        self.right.stop()
