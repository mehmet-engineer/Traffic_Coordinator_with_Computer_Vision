# General Traffic Coordinator Algorithm

The algorithm is designed to give unmanned aerial vehicles the ability to act as traffic controllers. It has been specifically developed by myself in Python language to be integrated into the camera of Quadcopter UAVs (drone). Today, many vehicle drivers usurp the rights of other drivers by using the safety lane, causing the sense of justice in traffic to be shaken. The task algorithm of the Traffic Coordinator UAV, which was developed as a solution to this problem, consists of 3 separate parts: vehicle detection, safety lane detection and inspection. The course of the vehicles in the lane can be monitored in a single software cycle. The images of the vehicles when they violate the lane can be taken in high resolution via the UAV camera. These violation photos are sent instantly to the relevant institution via e-mail.

![resim](https://github.com/mehmet-engineer/General_Traffic_Coordinator_Algorithm/blob/master/algoritma.png)


YOLO V4 Tiny object detection algorithm is used for the recognition of traffic vehicles. The detected land vehicles are evaluated in 3 different categories as cars, buses and heavy vehicles. The software is counted according to the classes of vehicles. Thus, the traffic density is determined.
For Vehicle Detection and YOLO V4 -> https://github.com/mehmet-engineer/YOLO_V4_Car_Control_Algorithm

![resim](https://github.com/mehmet-engineer/General_Traffic_Coordinator_Algorithm/blob/master/arac_tespit.png)


“Hough Line” theory is used for safety lane detection. According to the position of the detected lanes, the course of the vehicles can be monitored and instant notification can be provided when a violation occurs.

For Lane Detection and HoughLine Theory -> https://github.com/mehmet-engineer/OpenCV_Lane_Detection

![resim](https://github.com/mehmet-engineer/General_Traffic_Coordinator_Algorithm/blob/master/serit.png)

