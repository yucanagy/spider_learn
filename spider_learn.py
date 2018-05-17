import numpy
import cv2

img = cv2.imread('images/5.jpg', 0)
cv2.namedWindow('window_name',cv2.WINDOW_AUTOSIZE)
cv2.imshow('window_name',img)
cv2.waitKey(0)
cv2.destroyAllWindows()