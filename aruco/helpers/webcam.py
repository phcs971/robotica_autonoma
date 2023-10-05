import cv2
from time import time
import numpy as np

class WebcamVideoStream:
    def __init__(self):
        self.cap = cv2.VideoCapture(1)
        self.frameTime = time()
        self.started = False
        if not self.cap.isOpened():
            raise IOError("Cannot open webcam")
        
    def get_frame(self):
        ret, frame = self.cap.read()
        self.size = frame.shape
        return frame
    
    def fps(self, frame):
        fps = 1 / (time() - self.frameTime)
        self.frameTime = time()

        cv2.rectangle(frame, (0, 0), (140, 40), (255, 255, 255), -1)
        cv2.putText(frame, f"FPS {int(fps)}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)

    def get_blank_image(self):
        return np.zeros((self.size[0], self.size[1], 4), dtype=np.uint8)
    
    def __del__(self):
        self.cap.release()