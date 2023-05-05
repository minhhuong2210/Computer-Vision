import cv2
import numpy as np

# Load ảnh đầu vào
img = cv2.imread('C:\\Users\\hp\\Documents\\Nam3\\term2\\ComputerVision\\lab06\\morphological_image.png', 0)


# Tạo kernel cho phép co
kernel = np.ones((10,10),np.uint8)

# Thực hiện phép co
erosion = cv2.erode(img,kernel,iterations = 1)

# Tạo kernel cho phép giãn
kernel = np.ones((5,5),np.uint8)

# Thực hiện phép giãn
dilation = cv2.dilate(img,kernel,iterations = 1)

# Hiển thị kết quả
cv2.imshow('Input', img)
cv2.imshow('Erosion', erosion)
cv2.imshow('Dilation', dilation)
cv2.waitKey(0)
cv2.destroyAllWindows()
