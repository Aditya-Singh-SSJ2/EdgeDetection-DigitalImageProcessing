import cv2
import numpy as np

# Load the image
img = cv2.imread('image.jpg', cv2.IMREAD_GRAYSCALE)
img = cv2.resize(img, (360, 480))

# Apply Canny edge detector
edges = cv2.Canny(img, 100, 200)

# Display the original and Canny edge images
cv2.imshow('Original', img)
cv2.imshow('Canny Edge Detection', edges)
cv2.waitKey(0)
cv2.destroyAllWindows()