from helpers.webcam import *
from helpers.aruco import *

webcam = WebcamVideoStream()
detector = ArucoDetector()

if __name__ == '__main__':
    while True:
        frame = webcam.get_frame()
        frame = detector.detect_markers(frame)
        cv2.imshow('frame', cv2.flip(frame, 1))

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    webcam.__del__()
    cv2.destroyAllWindows()