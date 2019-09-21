import numpy as np
import cv2
im=cv2.imread("C:/Users/user/Desktop/r2.jpg")
imgray=cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
imgray = cv2.Canny(imgray, 30, 200)
#ret,thresh=cv2.threshold(imgray,10,20,cv2.THRESH_BINARY)
contours,hierarchy=cv2.findContours(imgray,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
cv2.drawContours(im,contours,-1,(255,255,0),3)

# scale_percent = 20 # percent of original size
# width = int(im.shape[1] * scale_percent / 100)
# height = int(im.shape[0] * scale_percent / 100)
# dim = (width, height)
# resize image
# resized = cv2.resize(im, dim, interpolation = cv2.INTER_AREA)

# #cv2.resize()
cv2.imshow('frame',im)
max=0
count=0
for i in range(len(contours)):
    cnt=contours[i]
    area=cv2.contourArea(cnt)
    print(area)
    if max<area:
        max=area
thresh=max/4
for i in range(len(contours)):
    cnt=contours[i]
    area=cv2.contourArea(cnt)
    if area>thresh:
        count=count+1
'''print contours
print hierarchy'''
#print(sec_max)
if count>2:
    print("alert")
else:
    print("no alert")
print(max)
cv2.waitKey(0)
