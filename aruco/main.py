from helpers.webcam import *
from helpers.aruco import *
from helpers.tracker import Tracker
from time import time

webcam = WebcamVideoStream()
tracker = Tracker()
detector = ArucoDetector(tracker)


def main():
    while True:
        frame = webcam.get_frame()
        frame = detector.detect_markers(frame)
        frame = tracker.draw(frame)
        frame = cv2.flip(frame, 1)
        webcam.fps(frame)

        cv2.imshow('frame', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    save()

def save():
    frame = webcam.get_blank_image()
    frame = tracker.draw(frame, all_positions=True)
    frame = cv2.flip(frame, 1)
    cv2.imwrite(f"output/{int(time())}.png", frame)


def close():
    webcam.__del__()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        pass
    finally:
        close()