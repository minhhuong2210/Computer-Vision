import cv2
import numpy as np
import argparse
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image1", required=True, help="path to the test image")
ap.add_argument("-j", "--image2", required=True, help="path to the test image")
args = vars(ap.parse_args())
img1 = cv2.resize(cv2.imread((args["image1"])),dsize=(492,492))
img2 = cv2.resize(cv2.imread((args["image2"])),dsize=(492,492))
img = np.concatenate((img1, img2), axis=1)
cv2.imshow('output', img)
cv2.waitKey(0)
cv2.destroyAllWindows()