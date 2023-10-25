import RPi.GPIO as GPIO
import time, logging

class HCSR04:
    def __init__(self, trigger: int, echo: int, name: str):
        self.trigger = trigger
        self.echo = echo
        self.name = name

        GPIO.setup(self.trigger, GPIO.OUT)
        GPIO.setup(self.echo, GPIO.IN)    

    def distance(self):
        # set Trigger to HIGH
        GPIO.output(self.trigger, True)
    
        # set Trigger after 0.01ms to LOW
        time.sleep(0.00001)
        GPIO.output(self.trigger, False)
    
        StartTime = time.time()
        StopTime = time.time()
    

        # save StartTime
        timeout = time.time()
        while GPIO.input(self.echo) == 0:
            StartTime = time.time()
            if StartTime - timeout > 1:
                break
    
        # save time of arrival
        timeout = time.time()
        while GPIO.input(self.echo) == 1:
            StopTime = time.time()
            if StopTime - timeout > 1:
                break
    
        # time difference between start and arrival
        TimeElapsed = StopTime - StartTime
        # multiply with the sonic speed (34300 cm/s)
        # and divide by 2, because there and back
        distance = (TimeElapsed * 34300) / 2

        logging.debug(f"{self.name} distance - %.1f cm" % distance)
    
        return distance

    def print_distance(self):
        dist = self.distance()
        print (f"{self.name} Distance = %.1f cm" % dist)