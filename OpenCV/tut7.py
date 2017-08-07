import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while(1):
    _, frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    lower_red = np.array([10,70,80])
    upper_red = np.array([20,255,100])
    
    mask = cv2.inRange(hsv, lower_red, upper_red)
    res = cv2.bitwise_and(frame,frame, mask= mask)
    # All color smoothing methods
    # bilateral = cv2.bilateralFilter(res,15,75,75)
    # kernel = np.ones((15,15), np.float32)/ 255
    # smoothed = cv2.filter2D(res, -1,kernel)
    # blur = cv2.GaussianBlur(res, (15,15),0)
    # median = cv2.medianBlur(res,10)
    # cv2.imshow('median',median)
    # cv2.imshow('blur',blur)
    # cv2.imshow('smoothed',smoothed)
    # cv2.imshow('frame',frame)
    

    kernel = np.ones((5,5), np.uint8)
    erosion = cv2.erode(mask, kernel,iterations = 1)
    dilation = cv2.dilate(mask, kernel,iterations = 1)
    opening = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
    closing = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)

    cv2.imshow('Opening',opening)
    cv2.imshow('Closing',closing)
    cv2.imshow('mask',mask)
    cv2.imshow('res',res)
    cv2.imshow('erosion',erosion)
    cv2.imshow('dilation',dilation)
    # cv2.imshow('bilateral',bilateral)
    
    if cv2.waitKey (1) & 0xFF==ord('q'):
    	break

cv2.destroyAllWindows()
cap.release()