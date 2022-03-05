import cv2
import numpy as np

img = cv2.imread('./image/original.png')
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, tresh = cv2.threshold(img_gray, 127, 255, 0)

# Find contour
contours, hierarchy = cv2.findContours(tresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
print("Number of countour = " + str(len(contours)))

# Draw contours 
cv2.drawContours(img, contours, 4, (0, 0, 255), 1)

# Show Image
cv2.imshow("Original", img)
cv2.imshow("imgGray", img_gray)
cv2.imshow("imgEdge", tresh)

cv2.waitKey(0)
cv2.destroyAllWindows()