from matplotlib import pyplot as plt
import numpy as np
import argparse
import cv2 

ap = argparse.ArgumentParser()
# đường dẫn đến file encodings đã lưu
ap.add_argument("-i", "--image", required=True, help="path to the test image")

args = vars(ap.parse_args())
image = cv2.imread(args["image"], cv2.IMREAD_GRAYSCALE)
a = image
def Median_Threshold(img):
    # Obtain the size of the image
    (rows, cols) = img.shape[0:2]
    
    # Find the mid point
    mid = (rows * cols) // 2
    
    # Sort the pixel into an array
    tmp = sorted(img.flatten())
    
    # Select the median pixel   
    th = tmp[mid]
    
    # Apply the threshold on the image
    out_img = (img > th).astype('uint8') * 255
    
    cv2.imshow('so sanh ket qua',out_img)
output = Median_Threshold(a)

histr = cv2.calcHist([output],[0],None,[256],[0,256])
plt.plot(histr)
plt.show()
