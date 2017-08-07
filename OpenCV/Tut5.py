import numpy as np
import cv2

img1 = cv2.imread('soldier.png')
img2 = cv2.imread('hanzo.jpg')
#Threshold Settings
rows, cols,channels = img2.shape
roi = img1[0:rows,0:cols]

img2Gray = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

ret, mask = cv2.threshold(img2Gray, 220,255, cv2.THRESH_BINARY_INV)
cv2.imshow('mask',mask)
#bitwise operation and operational editing
mask_inv = cv2.bitwise_not(mask)
img1_bg = cv2.bitwise_and(roi , roi , mask=mask_inv)
img2_fg = cv2.bitwise_and(img2 , img2 , mask=mask)

dst = cv2.add(img1_bg, img2_fg)
img1[0:rows,0:cols]=dst

cv2.imshow('res', img1)
#Rendering two images to mix them.
# add = img1 + img2
# add = cv2.add(img1,img2)
weigh = cv2.addWeighted (img1 , .6 ,img2 , .4 , 0)



cv2.imshow("add", weigh)
cv2.waitKey(0)
cv2.destroyAllWindows()