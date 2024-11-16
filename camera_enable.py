import cv2
video_cap = cv2.VideoCapture(0) 
#runtime camera will be enabled
while True:
    ret , video = video_cap.read()
    cv2.imshow("video_live",video)
    if cv2.waitKey(10) == ord("c"): #press 'c' to close the window
     # any images can be stopped for a particcular time period
        break

video_cap.release() 

