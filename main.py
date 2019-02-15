import cv2 as cv2
import time
import numpy as np

# Reading the video
video = cv2.VideoCapture("video.mp4")
 

time.sleep(3)
 
background=0
count = 0
 
for i in range(30):
  ret,background = video.read()

background = np.flip(background,axis=1)
 
while (video.isOpened()):
  ret, img = video.read()

  if not ret:
    break
  
  count+=1
  img = np.flip(img,axis=1)

  hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

  lowerRed = np.array([0,120,70])
  upperRed = np.array([10,255,255])

  mask1 = cv2.inRange(hsv, lowerRed, upperRed)

  mask1 = cv2.morphologyEx(mask1, cv2.MORPH_OPEN, np.ones((3,3),np.uint8),iterations=2)

  mask1 = cv2.dilate(mask1,np.ones((3,3),np.uint8),iterations = 1)

  mask2 = cv2.bitwise_not(mask1)

  res1 = cv2.bitwise_and(background, background, mask = mask1)
  res2 = cv2.bitwise_and(img, img, mask = mask2)
  finalOutput = cv2.addWeighted(res1,1,res2,1,0)

  cv2.imshow('img', finalOutput)
  k = cv2.waitKey(10)
  if k == 27:
    break


