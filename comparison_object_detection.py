import cv2
import numpy as np

# Import image
image_original = cv2.imread('./image/original.png')
image_compare = cv2.imread('./image/2.png')

# Preprocessing
image_original = cv2.cvtColor(image_original, cv2.COLOR_RGB2GRAY)
image_compare = cv2.cvtColor(image_compare, cv2.COLOR_RGB2GRAY)

# Resize image
image_original = cv2.resize(image_original, (250,250))
image_compare = cv2.resize(image_compare, (250,250))

# Compare image
if image_original.shape == image_compare.shape:
    image_difference = cv2.subtract(image_original, image_compare)
else:
    print("Shape not equal !")

# Convert to binary
_,image_original = cv2.threshold(image_original, 25, 30, cv2.THRESH_BINARY)
_,image_compare = cv2.threshold(image_compare, 25, 50, cv2.THRESH_BINARY)
_,image_difference = cv2.threshold(image_difference, 20, 150, cv2.THRESH_BINARY)

# Show image
cv2.imshow("Original", image_original)
cv2.imshow("Image_Compare", image_compare)
cv2.imshow("Image_Difference", image_difference)

# Holding Window
cv2.waitKey(0)
cv2.destroyAllWindows()