import cv2 as cv2
import time
import numpy as np

# Creating a VideoCapture object
# This will be used for image acquisition later in the code.
cap = cv2.VideoCapture("video.mp4")
 
# We give some time for the camera to warm-up!
time.sleep(3)
 
background=0
 
for i in range(30):
  ret,background = cap.read()
 
# Laterally invert the image / flip the image.
background = np.flip(background,axis=1)
# im = cv2.resize(background,(500,500))
# cv2.imshow('image',im)
# cv2.waitKey(0)


# Capturing the live frame
ret, img = cap.read()
 
# Laterally invert the image / flip the image
img  = np.flip(img,axis=1)
 
# converting from BGR to HSV color space
hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
 
# Range for lower red
lower_red = np.array([0,120,70])
upper_red = np.array([10,255,255])
mask1 = cv2.inRange(hsv, lower_red, upper_red)
 
# Range for upper range
lower_red = np.array([170,120,70])
upper_red = np.array([180,255,255])
mask2 = cv2.inRange(hsv,lower_red,upper_red)
 
# Generating the final mask to detect red color
mask1 = mask1+mask2