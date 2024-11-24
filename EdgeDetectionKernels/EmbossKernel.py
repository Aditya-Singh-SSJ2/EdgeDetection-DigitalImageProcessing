import cv2
import numpy as np

# Load the image
img = cv2.imread('image.jpg', cv2.IMREAD_GRAYSCALE)
img = cv2.resize(img, (360, 480))

# Define the 3x3 emboss kernel
emboss_kernel = np.array([[-2, -1,  0],
                          [-1,  1,  1],
                          [ 0,  1,  2]])

# Perform convolution using the emboss kernel
embossed_img = cv2.filter2D(img, -1, emboss_kernel)

# Display the original and embossed images
cv2.imshow('Original', img)
cv2.imshow('Emboss Detection', embossed_img)
cv2.waitKey(0)
cv2.destroyAllWindows()