import numpy as np
import cv2

img = cv2.resize(cv2.imread('media/soccer_practice.jpg', 0), (0,0), fx = 0.8, fy = 0.8)
template = cv2.resize(cv2.imread('media/shoe.PNG', 0), (0,0), fx=0.8, fy=0.8)

h,w = template.shape

methods = [cv2.TM_CCOEFF, cv2.TM_CCOEFF_NORMED, cv2.TM_CCORR,
          cv2.TM_CCORR_NORMED, cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]

for method in methods:
    img2 = img.copy()

    result = cv2.mathTemplate(img2, template, method)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

    if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
        location = min_loc
    else:
        location = max_loc

    bottom_right = (location[0] + w, location[1] + h)


