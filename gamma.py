import cv2 
import numpy as np
path = "rgb_image.jpg"
def gamma(path):
    img = cv2.imread(path, cv2.COLOR_BGR2RGB)
    (r, c) = img.shape[0:2]
    gamma = 4
    for i in range (r):
        for j in range(c):
            k = 2 # k la cac kenh, k =0:red, k=1: green, k=2:blue
            img[i,j,k] = 255 * (img[i,j,k]/255) ** (1/gamma) 
    return img
def concatenate(img1,img2):
    img_1 = cv2.resize(img1,dsize=(492,492))
    img_2 = cv2.resize(cv2.imread(img2),dsize=(492,492))
    img = np.concatenate((img_1, img_2), axis=1)
    cv2.imshow('output', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
# tinh CDF 
def getHist(image):
    image = cv2.imread(image)
    bgr_planes = cv2.split(image) #tách kênh màu 
    histSize = 256
    histRange = (0, 256) 
    accumulate = False
    b_hist = cv2.calcHist(bgr_planes, [0], None, [histSize], histRange, accumulate=accumulate)
    g_hist = cv2.calcHist(bgr_planes, [1], None, [histSize], histRange, accumulate=accumulate)
    r_hist = cv2.calcHist(bgr_planes, [2], None, [histSize], histRange, accumulate=accumulate)


    return r_hist #kênh đỏ

def getCDF(path):
    histogram = getHist(path)
    CDF=[]
    MxN = len(path) * len(path[0])
    temp = 0
    for i in range(len(histogram)):
        temp += histogram[i]
        CDF.append(temp/MxN)
    print(CDF)
    return CDF

# gamma(path)
# getCDF(path)
concatenate(gamma(path),path)