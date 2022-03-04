import cv2
import numpy as np

# Import image
image_original = cv2.imread('./image/3.png')
image_compare = cv2.imread('./image/1.png')

# Preprocessing
image_original = cv2.cvtColor(image_original, cv2.COLOR_RGB2GRAY)
image_compare = cv2.cvtColor(image_compare, cv2.COLOR_RGB2GRAY)

# Convert to binary
_,image_original = cv2.threshold(image_original, 0, 60, cv2.THRESH_BINARY)
_,image_compare = cv2.threshold(image_compare, 0, 60, cv2.THRESH_BINARY)

# Resize image
image_original = cv2.resize(image_original, (250,250))
image_compare = cv2.resize(image_compare, (250,250))

# Compare image
if image_original.shape == image_compare.shape:
    image_difference = cv2.subtract(image_original, image_compare)
    print(image_difference)
else:
    print("Shape not equal !")

# Create line
cv2.line(image_difference,(0,125),(250,125),(255,0,0),1)

# Show image
cv2.imshow("Original", image_original)
cv2.imshow("Image_Compare", image_compare)
cv2.imshow("Image_Difference", image_difference)

# Holding Window
cv2.waitKey(0)
cv2.destroyAllWindows()