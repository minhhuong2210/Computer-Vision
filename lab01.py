import math
# importing cv2
import cv2
 
# path
path = 'spine.jpg'
img = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
(row, col) = img.shape[0:2]
for i in range(row):
    for j in range(col):
        img[i][j] = math.sqrt(img[i][j]) * 16
cv2.imshow("spine", img) 
cv2.waitKey(0)
cv2.destroyAllWindows()


