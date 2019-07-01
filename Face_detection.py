import cv2

clf=cv2.CascadeClassifier('face.xml')

def photo_Face_detect():
    image=input("Enter Image Name(with extension):")
    cap=cv2.imread(image)
    cap=cv2.resize(cap,(int(cap.shape[0]/2),int(cap.shape[1]/4)))
    face=clf.detectMultiScale(cap,1.09,5)
    for x,y,w,h in face:
        cv2.rectangle(cap,(x,y),(x+h,y+w),(255,255,255),1)
    cv2.imshow("face2",cap[y:y+w,x:x+h])
    if cv2.waitKey(0) & 0xff==ord('\r'):
        exit(0)
def Live_face_detect():
    video=cv2.VideoCapture(0)
    while True:
        frame=video.read()[1]
        face=clf.detectMultiScale(frame,1.09,5)
        for x,y,w,h in face:
            cv2.rectangle(frame,(x,y),(x+w,y+h),(255,255,255),1)
        cv2.imshow("Face_detector",frame)
        key=cv2.waitKey(1)
        if key==ord('\r'):
            break
    cv2.destroyAllWindows()
    video.release()



print('''1.Live
2.Photo

Choose one:''')
choice=int(input())
if choice==2:
    photo_Face_detect()
elif choice==1:
    Live_face_detect()
    


