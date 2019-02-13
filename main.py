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