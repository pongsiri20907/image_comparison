import cv2
import numpy as np
from http import client
import paho.mqtt.client as paho
import sys

# Mqtt
client = paho.Client()
if client.connect("localhost", 1883, 60) != 0:
    print("Cannot connect to Mqtt Broker !")
    sys.exit(-1)

# Import image
original = cv2.imread("./image/original.png")
img_compare = cv2.imread("./image/original.png")

# Preprocessing
original_gray = cv2.cvtColor(original, cv2.COLOR_BGR2GRAY)
img_compare_HSV = cv2.cvtColor(img_compare, cv2.COLOR_BGR2HSV)

# Find contour Original image
ret, original_edge = cv2.threshold(original_gray, 127, 255, 0)
contours, heirarchy = cv2.findContours(original_edge, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE )

# Find contour area Original image
for contour in contours:
    original_area = cv2.contourArea(contour)
print("Original area = ", original_area)

# Draw Contour Original image
cv2.drawContours(original, contours, 4, (0, 255, 0), 1)

# Color detection and find compare_area
lower = np.array([50, 50, 50])
upper = np.array([130, 255, 255])
mask = cv2.inRange(img_compare_HSV, lower, upper)
contours, heirarchy = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE )
for contour in contours:
    compare_area = cv2.contourArea(contour)
print("Compare area = ", compare_area)
cv2.drawContours(img_compare, contours, -1, (0, 255, 0), 1)

# Calulate percentage of area
percentage_Area = (compare_area/original_area)*100
print("Percentage of area = ", f'{percentage_Area:.2f}', " %")

# Send mqtt
client.publish("test", f'{percentage_Area:.2f}', 0)

# Show image
cv2.imshow("Original", original)
cv2.imshow("Compare", img_compare)
cv2.imshow("Color Detection", mask)

cv2.waitKey(0)
cv2.destroyAllWindows()
