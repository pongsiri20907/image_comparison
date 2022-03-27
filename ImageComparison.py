import cv2
import numpy as np
from http import client
import paho.mqtt.client as paho
import sys

# Setting parameter
y_top = 20
y_low = 543
ofset = 0.9
image_path = "./image/M1.jpg"

# Mqtt
client = paho.Client()
if client.connect("localhost", 1883, 60) != 0:
    print("Cannot connect to Mqtt Broker !")
    sys.exit(-1)

# Import image
original = cv2.imread(image_path)

# Preprocessing Original image
original_cropped = original[180:800, 530:800]
original_gray = cv2.cvtColor(original_cropped, cv2.COLOR_BGR2GRAY)
original_blur = cv2.GaussianBlur(original_gray, (5,5), 0)

# Find contour Original image
# Draw line
original_edges = cv2.Canny(original_blur, 20, 60)
contours, heirarchy = cv2.findContours(original_edges, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
original_line = cv2.HoughLinesP(original_edges, 1, np.pi/180, 50, maxLineGap=50)
if original_line is not None:
    for line in original_line:
        x1, y1, x2, y2 = line[0]
        if y1 == y2 and x2 - x1 > 150:
            cv2.line(original_cropped, (12, y_top), (249, y_top), (0, 250, 0), 1)               # Top level : 33
            cv2.line(original_cropped, (12, y1), (249, y2), (0, 0, 255), 1)                     # Detect scale
            cv2.line(original_cropped, (12,y_low), (249, y_low), (0, 250, 0), 1)                # Low y level : 0
            print("y1 ",y1," y2", y2)
            break

# Calulate percentage
scale_percentage = ((y_low - y1) / (y_low - y_top))*33 + ofset
print("Scale = ", scale_percentage)

# Send mqtt
client.publish("test", f'{scale_percentage:.2f}', 0)

# Show image
cv2.imshow("Original", original_cropped)
cv2.imshow("Edge", original_edges)

cv2.waitKey(0)
cv2.destroyAllWindows()
