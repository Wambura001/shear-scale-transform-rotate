import cv2
import numpy as np

# Read the image
path = r'G:\+++++KDU\11. Spring_2025\3. Computer Vision_Sophomore A\Lectures\CV Practical\CV_Image_1.jpeg'
image = cv2.imread(path)
cv2.imshow('Original Image', image)

# Get the dimensions of the image (height and width)
rows, cols = image.shape[:2]

#################### Scaling, Translation, and Shearing Image ####################

# Create the affine transformation matrix for Scaling, Translation, and Shearing
matrix = np.float32([
    [1.25, 0.25, 20],  
    [0.25, 0.75, 10] ]) 

# Apply the affine transformation with warpAffine
image = cv2.warpAffine(image, matrix, (int(cols * 1.5), int(rows * 1.75)))
cv2.imshow('Scaled, Translated, and Sheared Image', image)

#################### Rotation of the Scaled, Translated, and Sheared Image ####################

Ro_rows, Ro_cols = image.shape[:2]
angle = -45  # Angle in degrees (counterclockwise)
scale = 1.0  # Scale factor (1.0 means no scaling)
center = (cols / 2, rows / 2)  # Center of rotation (image center)
rotation_matrix = cv2.getRotationMatrix2D(center, angle, scale)
image=cv2.warpAffine(image, rotation_matrix, (Ro_cols, Ro_rows))

# Save and display the result

cv2.imshow('Rotated Image with Affine Transformation', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
