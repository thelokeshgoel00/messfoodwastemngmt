#importing necessary libraries
import numpy as np
import cv2
# reading image
im=cv2.imread("C:/Users/user/Desktop/9.jpg")
# converting image to gray scale
imgray=cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
# canning image to remove noises
imgray = cv2.Canny(imgray, 30, 200)
#finding contours in the image
contours,hierarchy=cv2.findContours(imgray,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
# now drawing the contours
cv2.drawContours(im,contours,-1,(255,255,0),3)

#cv2.imshow('frame',im)
#initailisng max to zero
max=0
# maintaining a counter
count=0
# iterating through the contours
for itr in range(len(contours)):
    cnt=contours[itr]
    #getting area of each contour
    area=cv2.contourArea(cnt)
    #print(area)
    if max<area:
        max=area
#got the maximum area which is actually the area of plate
# setting a threshold area
thresh=max/7
# calculating the food covered area of plate
for itr in range(len(contours)):
    cnt=contours[itr]
    area=cv2.contourArea(cnt)
    if area>thresh and area!=max :
        count=count+1
if count>2:
    print("alert")
else:
    print("no alert")
cv2.waitKey(0)
