import cv2
from matplotlib import pyplot

img = cv2.imread('images/5.jpg', 0)

pyplot.imshow(img, cmap='gray', interpolation='bicubic')
pyplot.xticks([])
pyplot.yticks([])
pyplot.show()