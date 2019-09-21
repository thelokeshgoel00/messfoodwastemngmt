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