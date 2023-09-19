from pyfirmata import ArduinoMega, util
from helpers.direction_controller import  DirectionController
from time import sleep

port = '/dev/cu.usbmodem1413301'

board = ArduinoMega(port)

led = board.get_pin('d:13:o')

direction = DirectionController(board)

while True:
    print("ON")
    board.digital[13].write(1)
    sleep(1)
    print("OFF")
    board.digital[13].write(0)
    sleep(1)