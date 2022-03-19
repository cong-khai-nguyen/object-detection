import numpy as np
import cv2

img = cv2.resize(cv2.imread('media/soccer_practice.jpg', 0), (0,0), fx = 0.8, fy = 0.8)
template = cv2.resize(cv2.imread('media/shoe.PNG', 0), (0,0), fx=0.8, fy=0.8)

h,w = template.shape

