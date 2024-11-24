import cv2
import numpy as np

# Load the image
img = cv2.imread('image.jpg', cv2.IMREAD_GRAYSCALE)
img = cv2.resize(img, (360, 480))

# Define the Prewitt kernels
prewitt_kernel_x = np.array([[-1, 0, 1],
                             [-1, 0, 1],
                             [-1, 0, 1]])

prewitt_kernel_y = np.array([[-1, -1, -1],
                             [ 0,  0,  0],
                             [ 1,  1,  1]])

# Apply Prewitt operator in the x direction
prewitt_x = cv2.filter2D(img, -1, prewitt_kernel_x)

# Apply Prewitt operator in the y direction
prewitt_y = cv2.filter2D(img, -1, prewitt_kernel_y)

# Combine the two Prewitt results
prewitt_combined = cv2.magnitude(prewitt_x, prewitt_y)

# Convert the result back to uint8
prewitt_combined = np.uint8(prewitt_combined)

# Display the original and Prewitt images
cv2.imshow('Original', img)
cv2.imshow('Prewitt Edge Detection', prewitt_combined)
cv2.waitKey(0)
cv2.destroyAllWindows()