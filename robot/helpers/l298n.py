import RPi.GPIO as GPIO

class L298N:
    def __init__(self):
        self.IN2 = 16 # green
        self.IN1 = 20 # yellow
        self.IN4 = 21 # blue
        self.IN3 = 26 # red

        GPIO.setup(self.IN1, GPIO.OUT)
        GPIO.setup(self.IN2, GPIO.OUT)
        GPIO.setup(self.IN3, GPIO.OUT)
        GPIO.setup(self.IN4, GPIO.OUT)

    def left_direct(self):
        GPIO.output(self.IN1, True)
        GPIO.output(self.IN2, False)

    def left_reverse(self):
        GPIO.output(self.IN1, False)
        GPIO.output(self.IN2, True)

    def left_break(self):
        GPIO.output(self.IN1, True)
        GPIO.output(self.IN2, True)

    def right_direct(self):
        GPIO.output(self.IN3, True)
        GPIO.output(self.IN4, False)

    def right_reverse(self):
        GPIO.output(self.IN3, False)
        GPIO.output(self.IN4, True)

    def right_break(self):
        GPIO.output(self.IN3, True)
        GPIO.output(self.IN4, True)
