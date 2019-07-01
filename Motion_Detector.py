import cv2
video=cv2.VideoCapture(0)
frame=video.read()[1]
frame2=video.read()[1]
while True:
    img=video.read()[1]
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    gray2=cv2.cvtColor(frame2,cv2.COLOR_BGR2GRAY)
    gray=cv2.GaussianBlur(gray,(51,51),0)
    gray2=cv2.GaussianBlur(gray2,(51,51),0)

    delta_frame=cv2.absdiff(gray,gray2)
    threshold_delta=cv2.threshold(delta_frame,20,255,cv2.THRESH_BINARY)[1]
    threshold_delta=cv2.dilate(threshold_delta,None,iterations=0)
    cnts,tr=cv2.findContours(threshold_delta,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)

    for cont in cnts:
        if cv2.contourArea(cont)<1000:
            continue
        (x,y,w,h)=cv2.boundingRect(cont)
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
    frame=frame2
    frame2=img

    cv2.imshow("Motion_detector",img)
    key=cv2.waitKey(1)
    if key==ord('\r'):
        break

video.release()
cv2.destroyAllWindows()