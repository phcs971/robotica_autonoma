from time import time;
from random import randint
import cv2

### CONFIG ###

### How many seconds the position will be show on the screen
### 0 - show all positions
POSITION_PERSISTENCE = 10

### How many positions will be used to calculate the average position
### 1 - use only the current position
POSITION_AVERAGE = 2

COLORS = [
    (255, 0, 0),
    (0, 255, 0),
    (0, 0, 255),
    (255, 255, 0),
    (0, 255, 255),
    (255, 0, 255),
    (255, 255, 255),
    (128, 128, 0),
    (128, 0, 128),
    (0, 128, 128),
    (128, 255, 0),
    (128, 0, 255),
    (0, 128, 255),
    (255, 128, 0),
    (255, 0, 128),
    (0, 255, 128),
    (128, 255, 255),
    (255, 128, 255),
    (255, 255, 128),
]
next_color = 0

class Position:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y
        self.time = time()

    def __str__(self): 
        return f"({self.x}, {self.y})"

class TrackingObject:
    def __init__(self, id, x, y):
        global next_color
        self.positions = [Position(x, y)]
        self.id = id
        self.color = COLORS[next_color]
        next_color += 1
        if next_color >= len(COLORS):
            next_color = 0

    def get_positions(self):
        if (POSITION_PERSISTENCE == 0):
            return self.positions
        positions = []
        for position in self.positions:
            if time() - position.time < POSITION_PERSISTENCE:
                positions.append(position)
            else: break
        return positions
    
    def add(self, x, y):
        if len(self.positions) == 0:
            self.positions.append(Position(x, y))
            return
        
        if (POSITION_AVERAGE == 1):
            self.positions.insert(0, Position(x, y))
            return
        
        positions = self.positions[:POSITION_AVERAGE-1]

        x_positions = [position.x for position in positions]
        x_positions.insert(0, x)

        y_positions = [position.y for position in positions]
        y_positions.insert(0, y)

        x = sum(x_positions) / len(x_positions)
        y = sum(y_positions) / len(y_positions)
        
        self.positions.insert(0, Position(int(x), int(y)))

class Tracker:
    def __init__(self):
        self.objects = []

    def add(self, id, x, y):
        for obj in self.objects:
            if obj.id == id:
                obj.add(x, y)
                return obj
        obj = TrackingObject(id, x, y)
        self.objects.append(obj)
        return obj

    def draw(self, frame, all_positions=False):
        for obj in self.objects:
            color = obj.color if frame.shape[2] == 3 else (obj.color[0], obj.color[1], obj.color[2], 255)
            positions =  obj.positions if all_positions else obj.get_positions()
            if len(positions) > 1:
                for i in range(len(positions) - 1):
                    cv2.line(frame, (positions[i].x, positions[i].y), (positions[i + 1].x, positions[i + 1].y), color, 2)
            if len(positions) > 0:
                cv2.circle(frame, (positions[-1].x, positions[-1].y), 4, color, -1)
                cv2.circle(frame, (positions[0].x, positions[0].y), 4, color, -1)
                frame = cv2.flip(frame, 1)
                cv2.putText(frame, str(obj.id), (frame.shape[1] - positions[0].x, positions[0].y - 15), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)
                frame = cv2.flip(frame, 1)
        return frame