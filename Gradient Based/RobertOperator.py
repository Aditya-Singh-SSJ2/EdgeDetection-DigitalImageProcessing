import cv2
import numpy as np

# Load the image
img = cv2.imread('image.jpg', cv2.IMREAD_GRAYSCALE)
img = cv2.resize(img, (360, 480))

# Define the Roberts cross kernels
roberts_cross_x = np.array([[ 1,  0],
                            [ 0, -1]])

roberts_cross_y = np.array([[ 0,  1],
                            [-1,  0]])

# Apply Roberts operator in the x direction
roberts_x = cv2.filter2D(img, -1, roberts_cross_x)

# Apply Roberts operator in the y direction
roberts_y = cv2.filter2D(img, -1, roberts_cross_y)

# Combine the two Roberts results
roberts_combined = cv2.magnitude(roberts_x, roberts_y)

# Convert the result back to uint8
roberts_combined = np.uint8(roberts_combined)

# Display the original and Roberts images
cv2.imshow('Original', img)
cv2.imshow('Roberts Edge Detection', roberts_combined)
cv2.waitKey(0)
cv2.destroyAllWindows()