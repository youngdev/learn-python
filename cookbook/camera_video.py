import sys
sys.path.append("\\Library\\Python\\2.7\\site-packages\\cv2")
from cv2.cv import *
from cv2 import *

# initialize the camera video
cam = VideoCapture(0)   # 0 -> index of camera
s, img = cam.read()
if s:    # frame captured without any errors
    namedWindow("cam-test",CV_WINDOW_AUTOSIZE)
    imshow("cam-test",img)
    waitKey(0)
    destroyWindow("cam-test")
