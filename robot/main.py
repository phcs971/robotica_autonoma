import RPi.GPIO as GPIO
from helpers.hcsr04 import HCSR04
from helpers.led import LED
from helpers.direction_controller import DirectionController
from helpers.aruco import ArucoDetector
from picamera2 import Picamera2
import libcamera
import time, logging
import cv2

# LOGGING CONFIG

logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')

# CONSTANTS

FRONT_LIMIT = 7.5 #cm
LATERAL_LIMIT = 4 #cm

TURN_180_DEGREES = 0.95 #s
TURN_90_DEGREES = 0.35 #s
SMALL_TURN = 0.05 #s
WAIT_TO_TURN = 0.04 #s

# SETUP
 
GPIO.setmode(GPIO.BCM)

cam = Picamera2()
cam.start()

front_sensor = HCSR04(18, 24, "Front")
left_sensor = HCSR04(2, 3, "Left")
right_sensor = HCSR04(6, 13, "Right")

aruco = ArucoDetector()

led = LED(19)

dc = DirectionController()

def main():
    logging.info("START")
    while True: loop()
        

def loop():
    led.periodic_toggle(1)
    # GET DISTANCES
    ft = front_sensor.distance()
    lt = left_sensor.distance()
    rt = right_sensor.distance()

    # GET IMAGE
    cap = cam.capture_array()
    img = cv2.cvtColor(cap, cv2.COLOR_BGRA2GRAY)

    # DETECT MARKERS
    aruco.detect_markers(img)
    
    # HANDLE MOVIMENT
    if (ft > FRONT_LIMIT):
        dc.forward()
        if (lt < LATERAL_LIMIT):
            dc.turn_right(SMALL_TURN)
        if (rt < LATERAL_LIMIT):
            dc.turn_left(SMALL_TURN)
    else:
        lastMarker = aruco.last
        if (lastMarker == 1):
            dc.turn_left(TURN_90_DEGREES)
            aruco.last = None
        elif (lastMarker == 2):
            dc.turn_right(TURN_90_DEGREES)
            aruco.last = None
        elif (lt < FRONT_LIMIT and rt < FRONT_LIMIT):
            dc.turn_left(TURN_180_DEGREES)
        elif (lt > rt):
            dc.turn_left(TURN_90_DEGREES)
        else:
            dc.turn_right(TURN_90_DEGREES)
        dc.full_break()
    time.sleep(.005)

    logging.debug("\n")
    

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        None
    except Exception as e:
        logging.error(e)
    finally:
        GPIO.cleanup()
        logging.info("\nSTOP")