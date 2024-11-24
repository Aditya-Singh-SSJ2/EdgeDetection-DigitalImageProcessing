import cv2
import numpy as np

# Load the image
img = cv2.imread('image.jpg', cv2.IMREAD_GRAYSCALE)
img = cv2.resize(img, (360, 480))

# Define the 3x3 outline kernel
outline_kernel = np.array([[-1, -1, -1],
                           [-1,  8, -1],
                           [-1, -1, -1]])

# Perform convolution using the outline kernel
outlined_img = cv2.filter2D(img, -1, outline_kernel)

# Display the original and outlined images
cv2.imshow('Original', img)
cv2.imshow('Outline Detection', outlined_img)
cv2.waitKey(0)
cv2.destroyAllWindows()