import cv2
import numpy as np

# Import image
image_original = cv2.imread('./image/original.png')
image_compare = cv2.imread('./image/3.png')

# Resize image
image_original = cv2.resize(image_original, (250,250))
image_compare = cv2.resize(image_compare, (250,250))

# Compare image
if image_original.shape == image_compare.shape:
    image_difference = cv2.subtract(image_original, image_compare)
    b, g, r = cv2.split(image_difference)
    print("[b, g, r] = ", b, g, r)
    if cv2.countNonZero(b) == 0 and cv2.countNonZero(g) == 0 and cv2.countNonZero(r) == 0:
        print("OK")
    else:
        print("Not OK !")
else:
    print("Shape not equal !")

# Show image
cv2.imshow("Original", image_original)
cv2.imshow("Image_Compare", image_compare)
cv2.imshow("Image_Difference", image_difference)

# Holding Window
cv2.waitKey(0)
cv2.destroyAllWindows()