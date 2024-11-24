import cv2
import numpy as np

# Load the image
img = cv2.imread('image.jpg', cv2.IMREAD_GRAYSCALE)
img = cv2.resize(img, (360, 480))

# Define the 3x3 vertical edge kernel
vertical_edge_kernel = np.array([[-1,  2, -1],
                                 [-1,  2, -1],
                                 [-1,  2, -1]])

# Perform convolution using the vertical edge kernel
convolved_img = cv2.filter2D(img, -1, vertical_edge_kernel)

# Display the original and convolved images
cv2.imshow('Original', img)
cv2.imshow('Vertical Edge Detection', convolved_img)
cv2.waitKey(0)
cv2.destroyAllWindows()