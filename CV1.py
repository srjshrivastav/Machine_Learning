import cv2,random

img1=cv2.imread('try1.jpg',1)
img2=cv2.imread('try.jpeg',1)
x=random.randint(0,300)
y=random.randint(0,300)
h=50
w=100
print(x,y,x+h,x+w)

crop1=img1[x:x+h,y:y+w]
tmp=crop1.copy()
crop2=img2[x:x+h,y:y+w]

img1[x:x+h,y:y+w]=crop2
img2[x:x+h,y:y+w]=tmp

cv2.imshow('pic1',img1)
cv2.imshow('pic2',img2)
cv2.waitKey(0)