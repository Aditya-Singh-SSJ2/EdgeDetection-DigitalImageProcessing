import cv2
import numpy as np

# Load the image
img = cv2.imread('image.jpg', cv2.IMREAD_GRAYSCALE)
img = cv2.resize(img, (360, 480))

# Define the 3x3 vertical edge kernel
vertical_edge_kernel = np.array([[-1,  2, -1],
                                 [-1,  2, -1],
                                 [-1,  2, -1]])

# Define the 3x3 horizontal edge kernel
horizontal_edge_kernel = np.array([[-1, -1, -1],
                                   [ 2,  2,  2],
                                   [-1, -1, -1]])

# Perform convolution using the vertical edge kernel
vertical_edges = cv2.filter2D(img, -1, vertical_edge_kernel)

# Perform convolution using the horizontal edge kernel
horizontal_edges = cv2.filter2D(img, -1, horizontal_edge_kernel)

# Combine both edges
combined_edges = cv2.addWeighted(vertical_edges, 0.5, horizontal_edges, 0.5, 0)

# Display the original and combined edge images
cv2.imshow('Original', img)
cv2.imshow('Combined Edge Detection', combined_edges)
cv2.waitKey(0)
cv2.destroyAllWindows()