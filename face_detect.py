import cv2
face_cap = cv2.CascadeClassifier("C:/Users/Mustafa/AppData/Local/Programs/Python/Python312/Lib/site-packages/cv2/data/haarcascade_frontalface_default.xml")
video_cap = cv2.VideoCapture(0) 
#runtime camera will be enabled
while True:
    ret , video = video_cap.read()
    color = cv2.cvtColor(video,cv2.COLOR_BGR2GRAY)
    face = face_cap.detectMultiScale(
        color,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(20,20),
        flags = cv2.CASCADE_SCALE_IMAGE
    )
    for(x,y,w,h) in face:
        cv2.rectangle(video,(x,y),(x+w,x+h),(0,225,0),2) #it will make sqare bracket
    cv2.imshow("video_live",video)
    if cv2.waitKey(10) == ord("c"): #press 'c' to close the window
     # any images can be stopped for a particcular time period
        break

video_cap.release() 

