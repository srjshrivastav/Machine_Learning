import cv2
import sys

img=cv2.imread('Flower3.jpg',1)
cv2.rectangle(img,(500,500),(400,300),color=(0,0,255),thickness=3)

cv2.imshow('Image',img)
#compression
cv2.imwrite('comp.jpg',img,[cv2.IMWRITE_JPEG_QUALITY,-1])
cv2.waitKey(0)