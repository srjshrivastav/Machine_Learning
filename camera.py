import cv2
import numpy as np
#starting camera
capture=cv2.VideoCapture(0)
plug=cv2.VideoWriter_fourcc(*'XVID')
out=cv2.VideoWriter('Video.avi',plug,40,(640,480))  # saving video
#print Camera is started or not
n=0
while capture.isOpened():
        status,img=capture.read() #it will  take first picture
        print(img.shape)
        #converting color
        gry=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        cv2.circle(img,(300,300),n+30,(20,0,255),-1)
        font=cv2.FONT_HERSHEY_COMPLEX
        cv2.putText(img,'HelloWorld',(200,150),font,2,(30,120,23),3)
        cv2.imshow("Live1",img)
        out.write(img)  # sending Data To video Writer
        cv2.imshow("Live",gry)
        n=n+1
        if cv2.waitKey(1) & 0xff==13:
            break  

cv2.destroyAllWindows()
capture.release()
