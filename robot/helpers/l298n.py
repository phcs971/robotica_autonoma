import pyfirmata

class L298N:
    def __init__(self, board: pyfirmata.Board):
        self.IN1 = board.get_pin('d:2:o')
        self.IN2 = board.get_pin('d:3:o')
        self.IN3 = board.get_pin('d:4:o')
        self.IN4 = board.get_pin('d:5:o')

    def left_direct(self):
        self.IN1.write(1)
        self.IN2.write(0)

    def left_reverse(self):
        self.IN1.write(0)
        self.IN2.write(1)

    def left_break(self):
        self.IN1.write(1)
        self.IN2.write(1)

    def right_direct(self):
        self.IN3.write(1)
        self.IN4.write(0)

    def right_reverse(self):
        self.IN3.write(0)
        self.IN4.write(1)

    def right_break(self):
        self.IN3.write(1)
        self.IN4.write(1)
