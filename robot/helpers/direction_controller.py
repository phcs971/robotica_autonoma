from helpers.l298n import L298N
import pyfirmata

class DirectionController:
    def __init__(self, board: pyfirmata.Board):
        self.h = L298N(board)


    def forward(self):
        self.h.left_direct()
        self.h.right_direct()
    

    def reverse(self):
        self.h.left_reverse()
        self.h.right_reverse()
    

    def turn_left(self):
        self.h.left_reverse()
        self.h.right_direct()
    

    def turn_right(self):
        self.h.left_direct()
        self.h.right_direct()
    

    def full_break(self):
        self.h.left_break()
        self.h.right_break()
    