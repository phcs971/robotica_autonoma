import cv2
import cv2.aruco as aruco

class ArucoDetector:
    def __init__(self):
        self.dict = aruco.getPredefinedDictionary(aruco.DICT_4X4_100)
        self.params = aruco.DetectorParameters()

    def detect_markers(self, image):
        (corners, ids, rejected) = cv2.aruco.detectMarkers(image, self.dict, parameters=self.params)
        selectedId = None
        if len(corners) > 0:
            # flatten the ArUco IDs list
            ids = ids.flatten()
            markerSize = 0
            # loop over the detected ArUCo corners
            for (markerCorner, markerID) in zip(corners, ids):
                # extract the marker corners (which are always returned in
                # top-left, top-right, bottom-right, and bottom-left order)
                corners = markerCorner.reshape((4, 2))

                # compute square perimeter
                peri = cv2.arcLength(corners, True)

                if (peri > markerSize):
                    markerSize = peri
                    selectedId = marketID
                
                print("[INFO] ArUco marker ID: {}".format(markerID))
        return selectedId

