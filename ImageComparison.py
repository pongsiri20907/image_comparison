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

# Find contour Original image
original_edges = cv2.Canny(original_blur, 20, 70)
contours, heirarchy = cv2.findContours(original_edges, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
original_line = cv2.HoughLinesP(original_edges, 1, np.pi/180, 50, maxLineGap=50)
if original_line is not None:
    for line in original_line:
        x1, y1, x2, y2 = line[0]
        if y1 == y2 and x2 - x1 > 150:
            cv2.line(original_cropped, (12, 80), (249, 80), (12, 250, 0), 2)                # Top y = 80 (100%)
            cv2.line(original_cropped, (x1, y1), (x2, y2), (0, 0, 255), 2)                  # Detect scale
            cv2.line(original_cropped, (12,540), (249, 540), (0, 250, 0), 2)                # Low y = 540 (0%)
            print("x1 ",x1," x2", x2)

# Calulate percentage of area
#percentage_Area = (compare_area/original_area)*100
#print("Percentage of area = ", f'{percentage_Area:.2f}', " %")

# Send mqtt
#client.publish("test", f'{percentage_Area:.2f}', 0)

# Show image
cv2.imshow("Original", original_cropped)

cv2.waitKey(0)
cv2.destroyAllWindows()
