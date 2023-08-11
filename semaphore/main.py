import cv2
import numpy as np
import os
import sys

def get_video(filename: str):
    cap = cv2.VideoCapture(filename)
    return cap

def rgb(filename: str):
    cap = get_video(filename)

    output_path = "outputs/" + filename.split("/")[1]
    if os.path.exists(output_path):
        os.remove(output_path)

    fps = cap.get(cv2.CAP_PROP_FPS)
    frameSize = (int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)), int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))
    codec = cv2.VideoWriter_fourcc(*'avc1')


    output =  cv2.VideoWriter(output_path, codec, fps, frameSize)
    success, frame = cap.read()
    
    while(success):
        # convert to rgb
        copy = frame.copy()
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                     
        # black out pixels that are mostly blue
        blue = frame[:,:,2]
        blueAvg = np.average(blue)
        for i in range(len(blue)):
            for j in range(len(blue[i])):
                if blue[i][j] > blueAvg:
                    frame[i][j] = [0,0,0]


        red = frame[:,:,0]
        green = frame[:,:,1]


        greenAvg = np.average(green)
        redAvg = np.average(red)
        yellowAvg = (greenAvg + redAvg) / 2

        if (greenAvg > redAvg and greenAvg > yellowAvg):
            cv2.putText(frame, "GO", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
        elif (redAvg > greenAvg and redAvg > yellowAvg):
            cv2.putText(frame, "STOP", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
        elif (yellowAvg > greenAvg and yellowAvg > redAvg):
            cv2.putText(frame, "SLOW DOWN", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
        
        # output.write(copy)
        output.write(cv2.cvtColor(frame, cv2.COLOR_RGB2BGR))
        

        success, frame = cap.read()
        # success = False
    output.release()

def hsv(filename: str):
    print(1)

def main():
    try:
        filename = "assets/" + sys.argv[1] + ".mp4"
        type = sys.argv[2]
        if type == "rgb":
            rgb(filename)
        elif type == "hsv":
            hsv(filename)
        else:
            raise Exception("Invalid Type")
    except:
        print("Invalid Arguments\n")
        print("python main.py <filename> <type>\n")
        print("Filenames: video1, video2, video3")
        print("Types: rgb, hsv")
        return

if __name__ == '__main__':
    main()