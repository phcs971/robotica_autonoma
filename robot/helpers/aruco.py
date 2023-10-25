import cv2
import cv2.aruco as aruco
import logging

class ArucoDetector:
    def __init__(self):
        self.dict = aruco.getPredefinedDictionary(aruco.DICT_4X4_100)
        self.params = aruco.DetectorParameters()
        self.last = None

    def detect_markers(self, image):
        # DETECTED MARKERS
        (corners, ids, rejected) = cv2.aruco.detectMarkers(image, self.dict, parameters=self.params)

        # FIND CLOSEST MARKER BASED ON MARKER RELATIVE SIZE
        selectedId = None
        if len(corners) > 0:
            ids = ids.flatten()
            markerSize = 0
            for (markerCorner, markerID) in zip(corners, ids):
                corners = markerCorner.reshape((4, 2))

                peri = cv2.arcLength(corners, True)

                if (peri > markerSize):
                    markerSize = peri
                    selectedId = markerID
                
        if (selectedId != None and selectedId != self.last):
            logging.info(f"DETECTED {selectedId}")
            self.last = selectedId
        return selectedId

