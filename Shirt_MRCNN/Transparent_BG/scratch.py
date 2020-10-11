# This file just used for trial purpose

import numpy as np
import cv2
from matplotlib import pyplot as  plt
img=cv2.imread(r'/samples/EDI/dataset/GT/FS0.jpg', cv2.IMREAD_GRAYSCALE)
#cv2.imwrite('C:/Users/Prathmesh/Documents/MATLAB/download.png',img)
img=cv2.resize(img,(600,600))
img=~img

#imgray = cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
gray_filtered = cv2.bilateralFilter(img, 7, 0, 50)
cv2.imshow('img_ol',gray_filtered)

edges = cv2.Canny(img, 60, 120)

edges_filtered = cv2.Canny(gray_filtered, 0, 120)
cv2.imshow('img_mol',edges)


imgray=~edges_filtered

ret, thresh= cv2.threshold(imgray,10,255,0)
contours,hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
x=cv2.drawContours(imgray,contours,1,(0,55,0),3)
cv2.imshow("x",x)
cv2.waitKey()
cv2.destroyAllWindows()