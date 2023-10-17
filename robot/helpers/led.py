import RPi.GPIO as GPIO
import time

class LED:
    def __init__(self, pin):
        self.pin = pin
        self.state = False
        self.timestamp = time.time() 
        
        GPIO.setup(self.pin, GPIO.OUT)

    def toggle(self):
        self.set(not self.state)

    def set(self, state):
        self.state = state
        GPIO.output(self.pin, state)
    
    def periodic_toggle(self, duration):
        if (time.time() - self.timestamp > duration):
            self.toggle()
            self.timestamp = time.time()