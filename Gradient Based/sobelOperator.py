import cv2
import numpy as np

# Load the image
img = cv2.imread('image.jpg', cv2.IMREAD_GRAYSCALE)
img = cv2.resize(img, (360, 480))

# Apply Sobel operator in the x direction
sobel_x = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=3)

# Apply Sobel operator in the y direction
sobel_y = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize=3)

# Combine the two Sobel results
sobel_combined = cv2.magnitude(sobel_x, sobel_y)

# Convert the result back to uint8
sobel_combined = np.uint8(sobel_combined)

# Display the original and Sobel images
cv2.imshow('Original', img)
cv2.imshow('Sobel Edge Detection', sobel_combined)
cv2.waitKey(0)
cv2.destroyAllWindows()