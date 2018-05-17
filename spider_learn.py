import numpy as np
import cv2

# 加载一张彩色图片不包含alpha通道
img = cv2.imread('demo.jpg', 1)