import cv2
import cv2.aruco as aruco
from helpers.tracker import Tracker

class ArucoDetector:
    def __init__(self, tracker: Tracker):
        self.dict = aruco.getPredefinedDictionary(aruco.DICT_4X4_100)
        self.params = aruco.DetectorParameters()
        self.tracker = tracker

    def detect_markers(self, image):
        (corners, ids, rejected) = cv2.aruco.detectMarkers(image, self.dict, parameters=self.params)
        if len(corners) > 0:
            # flatten the ArUco IDs list
            ids = ids.flatten()
            # loop over the detected ArUCo corners
            for (markerCorner, markerID) in zip(corners, ids):
                # extract the marker corners (which are always returned in
                # top-left, top-right, bottom-right, and bottom-left order)
                corners = markerCorner.reshape((4, 2))
                (topLeft, topRight, bottomRight, bottomLeft) = corners

                # convert each of the (x, y)-coordinate pairs to integers
                topRight = (int(topRight[0]), int(topRight[1]))
                bottomRight = (int(bottomRight[0]), int(bottomRight[1]))
                bottomLeft = (int(bottomLeft[0]), int(bottomLeft[1]))
                topLeft = (int(topLeft[0]), int(topLeft[1]))

                # compute and draw the center (x, y)-coordinates of the ArUco marker
                cX = int((topLeft[0] + bottomRight[0]) / 2.0)
                cY = int((topLeft[1] + bottomRight[1]) / 2.0)
                color = self.tracker.add(markerID, cX, cY).color

                # draw the bounding box of the ArUCo detection
                cv2.line(image, topLeft, topRight, color, 2)
                cv2.line(image, topRight, bottomRight, color, 2)
                cv2.line(image, bottomRight, bottomLeft, color, 2)
                cv2.line(image, bottomLeft, topLeft, color, 2)
                
                cv2.circle(image, (cX, cY), 4, color, -1)
                
                print("[INFO] ArUco marker ID: {}".format(markerID))
        return image

