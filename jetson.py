import numpy as np
import cv2

#https://github.com/ArduCAM/MIPI_Camera/tree/master/Jetson
 
def predefined_settings(
    capture_width=3280,
    capture_height=2464,
    display_width=820,
    display_height=616,
    framerate=21,
    flip_method=2,

    #capture_width=1280,
    #capture_height=720,
    #display_width=640,
    #display_height=360,
    #framerate=60,
    #flip_method=0,
):
    return (
        "nvarguscamerasrc ! "
        "video/x-raw(memory:NVMM), "
        "width=(int)%d, height=(int)%d, "
        "format=(string)NV12, framerate=(fraction)%d/1 ! "
        "nvvidconv flip-method=%d ! "
        "video/x-raw, width=(int)%d, height=(int)%d, format=(string)BGRx ! "
        "videoconvert ! "
        "video/x-raw, format=(string)BGR ! appsink"
        % (
            capture_width,
            capture_height,
            framerate,
            flip_method,
            display_width,
            display_height,
        )
    )

def cam_launching():
    cam = cv2.VideoCapture(predefined_settings(), cv2.CAP_GSTREAMER)
    if cam.isOpened() == False:
        print("Kamera taninmadi!")
    return cam
