# Python program to explain cv2.imread() method
 
# importing cv2
import cv2
 
# path
path = 'gray_image.jpg'
 
# Using cv2.imread() method
# Using 0 to read image in grayscale mode
img = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
 
# Displaying the image
cv2.imshow('gray_scale', img)
cv2.waitKey(0)
cv2.destroyAllWindows()