import cv2
import numpy as np
# import matplotlib.pyplot as plt
cap = cv2.VideoCapture(0)
# fourcc = cv2.cv.FOURCC(*'VID')
# out = cv2.VideoWriter('output.avi',fourcc , 20.0 , (640,480))

while True:
	ret, frame = cap.read()
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	# out.write(frame)
	cv2.imshow('frame',frame)
	cv2.imshow('frame1',gray)

	if cv2.waitKey (1) & 0xFF==ord('q'):
		break

cap.release()
# out.release()
cv2.destroyAllWindows()

# img = cv2.imread("watch.jpg",cv2.IMREAD_GRAYSCALE)
#IMREAD_COLOR = 1 Code
#IMREAD_UNCHANGED = -1

# cv2.imshow("Image", img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
# cv2.imwrite ( same ) to save files.

# plt.imshow(img , cmap='gray', interpolation = 'bicubic' )
# plt.plot([50,100],[80,100],'c',linewidth=5)
# plt.show()

