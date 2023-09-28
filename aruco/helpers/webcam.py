import cv2

class WebcamVideoStream:
    def __init__(self):
        self.cap = cv2.VideoCapture(1)
        if not self.cap.isOpened():
            raise IOError("Cannot open webcam")
        
    def get_frame(self):
        ret, frame = self.cap.read()
        return frame
    
    def __del__(self):
        self.cap.release()