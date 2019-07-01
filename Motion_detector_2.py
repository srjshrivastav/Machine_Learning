import cv2
cam=cv2.VideoCapture(0)

#DEtect Motion
frame=cam.read()[1]
frame1=cam.read()[1]
frame2=cam.read()[1]

#Now Creating Image diff

def image_diff(x,y,z):
    #difference between x and y---gray and gray1-------d1
    d1=cv2.absdiff(x,y)
    #difference between y and z---gray1 and gray2-------d2
    d2=cv2.absdiff(y,z)
    #absolute diff. b/w d1 and d2
    final=cv2.bitwise_and(d1,d2)
    return final

#Now applying Function
while cam.isOpened():
    status,img=cam.read()
    motion=image_diff(frame,frame1,frame2) 
    frame=frame1
    frame1=frame2
    frame2=img
    cv2.imshow('Motion',motion)
    if cv2.waitKey(1) & 0xff==ord('\r'):
        break


cv2.destroyAllWindows()
cam.release()