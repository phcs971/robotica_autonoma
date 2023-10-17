import RPi.GPIO as GPIO
from helpers.hcsr04 import HCSR04
from helpers.led import LED
from helpers.direction_controller import DirectionController
import time

FRONT_LIMIT = 10 #cm
LATERAL_LIMIT = 3 #cm

TURN_180_DEGREES = 0.95 #s
TURN_90_DEGREES = 0.5 #s
SMALL_TURN = 0.1 #s

 
GPIO.setmode(GPIO.BCM)

front_sensor = HCSR04(18, 24, "Front")
left_sensor = HCSR04(2, 3, "Left")
right_sensor = HCSR04(17, 27, "Right")

led = LED(19)

dc = DirectionController()

def main():
    print("START")
    while True: loop()
        

def loop():
    led.periodic_toggle(1)
    ft = front_sensor.distance()
    lt = left_sensor.distance()
    rt = right_sensor.distance()
    if (ft > FRONT_LIMIT):
        dc.forward()
        if (lt < LATERAL_LIMIT):
            dc.turn_right(SMALL_TURN)
        if (rt < LATERAL_LIMIT):
            dc.turn_left(SMALL_TURN)
    else:
        if (lt < FRONT_LIMIT and rt < FRONT_LIMIT):
            dc.turn_left(TURN_180_DEGREES)
        if (lt > rt):
            dc.turn_left(TURN_90_DEGREES)
        else:
            dc.turn_right(TURN_90_DEGREES)
        dc.full_break()
    time.sleep(.01)
    

if __name__ == '__main__':
    try:
        main()
        print("STOP")
    except:
        GPIO.cleanup()