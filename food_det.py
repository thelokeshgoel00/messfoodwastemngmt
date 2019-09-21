import cv2
#import numpy as np
from PIL import Image
# function to get the gray color pixel's location 
def gray_pixels(image):
    # minimum and maximum range of gray color
    r_min=50
    r_max=110
    g_min=50
    g_max=110
    b_min=50
    b_max=110
    # creating a set of pixels within the range
    gray_pix=set()
    img=Image.open(image)
    rgb=img.convert('RGB')
    # traversing through all pixels
    for i in range(img.size[0]):
        for j in range(img.size[1]):
            r,g,b=rgb.getpixel((i,j))
            if r>=r_min and r<=r_max and g>=g_min and g<=g_max and b>=b_min and b<=b_max:
                gray_pix.add((i,j))
# returning the locations of all gray pixels
    return len(gray_pix)



img='C:/Users/user/Desktop/sports.jpg'
#cv2.namedWindow("image",cv2.WINDOW_NORMAL)
#
#=set()
plate=gray_pixels(img)

#plate=len(gray_pix)
img=cv2.imread(img,1)
total=0
for row in img:
        for elem in row:
                total=total+1
                #print(elem)
                '''if elem==0:
                        black=black+1
                elif elem>250:
                        white=white+1'''
                

#cv2.waitKey(0)
food=total-plate
percentage=food/total
print(food)
print(total)
print("Food wasted is ")
print(percentage)
if cv2.waitKey(0) == ord('q'):
	cv2.destroyAllWindows()
