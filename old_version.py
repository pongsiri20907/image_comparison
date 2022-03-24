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
original = cv2.imread("./image/M1.jpg")
img_compare = cv2.imread("./image/M1.jpg")

# Preprocessing Original image
original_cropped = original[180:800, 530:800]
original_gray = cv2.cvtColor(original_cropped, cv2.COLOR_BGR2GRAY)
original_blur = cv2.GaussianBlur(original_gray, (5,5), 0)

# Preprocessing Compare image
# compare_cropped = original[180:800, 520:800]
# compare_blur = cv2.GaussianBlur(compare_cropped, (3,3), 0)
# img_compare_HSV = cv2.cvtColor(compare_blur, cv2.COLOR_BGR2HSV)

# Find contour Original image
# ret, original_bin = cv2.threshold(original_blur, 75, 255, cv2.THRESH_BINARY)
original_edges = cv2.Canny(original_blur, 20, 70)
contours, heirarchy = cv2.findContours(original_edges, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
original_line = cv2.HoughLinesP(original_edges, 1, np.pi/180, 50, maxLineGap=50)
if original_line is not None:
    for line in original_line:
        x1, y1, x2, y2 = line[0]
        if y1 == y2 and x2 - x1 > 150:
            cv2.line(original_cropped, (x1, y1), (x2, y2), (0, 0, 255), 2)
            print("x1 ",x1," x2", x2)
    

# # Find contour area Original image
# for contour in contours:
#     original_area = cv2.contourArea(contour)

# # Draw Contour Original image
# cv2.drawContours(original, contours, -1, (0, 0, 255), 2)
# print("Original area = ", original_area)

# Color detection and find compare_area
# lower = np.array([50, 50, 50])
# upper = np.array([250, 255, 250])
# mask = cv2.inRange(img_compare_HSV, lower, upper)
# contours, heirarchy = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE )
# for contour in contours:
#     compare_area = cv2.contourArea(contour)
# print("Compare area = ", compare_area)
# cv2.drawContours(img_compare, contours, -1, (0, 255, 0), 1)

# Calulate percentage of area
#percentage_Area = (compare_area/original_area)*100
#print("Percentage of area = ", f'{percentage_Area:.2f}', " %")

# Send mqtt
#client.publish("test", f'{percentage_Area:.2f}', 0)

# Show image
cv2.imshow("Original", original_cropped)
# cv2.imshow("Compare", mask)
# cv2.imshow("Color Detection", mask)

cv2.waitKey(0)
cv2.destroyAllWindows()
