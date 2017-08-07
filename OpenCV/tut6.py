import cv2
import numpy as numpy
img = cv2.imread('moon.jpg')

retval, threshold = cv2.threshold(img, 12 , 255 , cv2.THRESH_BINARY)
grayscale = cv2.cvtColor(img , cv2.COLOR_BGR2GRAY)
retval2, threshold2 = cv2.threshold(grayscale, 12 , 255 , cv2.THRESH_BINARY)

gaus = cv2.adaptiveThreshold(grayscale,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY,115,1)


cv2.imshow('guas', gaus)
cv2.imshow('gray',grayscale)
cv2.imshow('image',img)
cv2.imshow('threshold', threshold)
cv2.waitKey(0)
cv2.destroyAllWindows()
