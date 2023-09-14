import cv2
import numpy as np

def main():
    img = cv2.imread('circuito.jpg')

    # Convert to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    

    _, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)

    # remove upper right corner 180x180


    size = 240
    thresh[0:size, thresh.shape[1]-size:thresh.shape[1]] = 0

    # create T shape kernel
    shape = [
              [0,1,1,1,1,1,1,0,0],
              [0,1,1,1,1,1,1,1,0],
              [0,0,0,1,1,0,0,0,0],
              [0,0,0,1,1,0,0,0,0],
              [0,0,0,1,1,0,0,0,0],
              [0,0,0,1,1,0,0,0,0],
              [0,0,0,1,1,0,0,0,0],
              [0,0,0,1,1,0,0,0,0],
              [0,0,0,1,1,0,0,0,0],
              [0,0,0,0,1,0,0,0,0],
              [0,0,0,0,1,0,0,0,0],
            ]

    t = np.array(shape, dtype=np.uint8)
    
    # create reversed T shape kernel
    
    inv_t = np.array(shape[::-1], dtype=np.uint8)


    # apply kernel
    erode = cv2.erode(thresh, t, iterations=1)
    dilate = cv2.dilate(erode, inv_t, iterations=1)

    result = cv2.cvtColor(dilate, cv2.COLOR_GRAY2BGR)

    # count white objects
    contours, hierarchy = cv2.findContours(dilate, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    print('Total objects: {}'.format(len(contours)))

    # add dilate as overlay with opacity 0.5 in img
    overlay = img.copy()
    alpha = 0.5
    cv2.addWeighted(result, alpha, overlay, 1 - alpha, 0, overlay)

    # show image

    cv2.imshow('binary', overlay)
    cv2.waitKey(0)

    cv2.imwrite('result.png', overlay)

if __name__ == '__main__':
    main()