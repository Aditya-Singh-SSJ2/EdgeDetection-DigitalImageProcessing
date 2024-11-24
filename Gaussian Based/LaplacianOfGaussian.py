import cv2
import numpy as np

# Load the image
img = cv2.imread('image.jpg', cv2.IMREAD_GRAYSCALE)
img = cv2.resize(img, (360, 480))

# Apply Gaussian blur to the image
blurred_img = cv2.GaussianBlur(img, (3, 3), 0)

# Apply Laplacian operator
laplacian = cv2.Laplacian(blurred_img, cv2.CV_64F)

# Convert the result back to uint8
laplacian = np.uint8(np.absolute(laplacian))

# Display the original and Laplacian of Gaussian images
cv2.imshow('Original', img)
cv2.imshow('Laplacian of Gaussian Edge Detection', laplacian)
cv2.waitKey(0)
cv2.destroyAllWindows()