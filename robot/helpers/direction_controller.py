from helpers.l298n import L298N
import time

class DirectionController:
    def __init__(self):
        self.h = L298N()


    def forward(self, duration: float = 0.0):
        self.h.left_direct()
        self.h.right_direct()
        if (duration > 0):
            time.sleep(duration)
    

    def reverse(self, duration: float = 0.0):
        self.h.left_reverse()
        self.h.right_reverse()
        if (duration > 0):
            time.sleep(duration)
    

    def turn_left(self, duration: float = 0.0):
        self.h.left_reverse()
        self.h.right_direct()
        if (duration > 0):
            time.sleep(duration)
    

    def turn_right(self, duration: float = 0.0):
        self.h.left_direct()
        self.h.right_reverse()
        if (duration > 0):
            time.sleep(duration)
    

    def full_break(self, duration: float = 0.0):
        self.h.left_break()
        self.h.right_break()
        if (duration > 0):
            time.sleep(duration)
    