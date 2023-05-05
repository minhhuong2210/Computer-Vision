import cv2
import numpy as np
import matplotlib.pyplot as plt


def show_image_with_result(image, result_image):
    ghep_anh = np.concatenate((image, result_image), axis=1)
    scale = 2/3
    height = int(len(ghep_anh)*scale)
    width = int(len(ghep_anh[0])*scale)
    ket_qua = cv2.resize(ghep_anh,(width,height))
    cv2.imshow('so sanh ket qua', ket_qua)
    cv2.waitKey(0)
    cv2.destroyAllWindows()    



def getHist(image):
    hist = np.zeros(256) 
    (r,c) = image.shape[0:2]
    for i in range(r):
        for j in range(c):
            hist[image[i][j]] += 1 #coongj 1 vao gtri hist tuong ung
    return hist

#cộng dồn giá trị 
def getCDF(histogram, gray_image):#gray image da dc doc
    CDF=[]
    MxN = len(gray_image) * len(gray_image[0]) #co ma tran
    temp = 0 #mat do
    for i in range(len(histogram)):
        temp += histogram[i] #cong sau
        CDF.append(temp/MxN) 
    return CDF


def findPos(val, CDF):#val = giá trị cdf1[i]
    for i in range(len(CDF)):
        if CDF[i-1] <= val <= CDF[i]:
            return i


def getLUT(CDF1,CDF2): #look up table
    lut = []
    for i in range(len(CDF1)):
        lut.append(findPos(CDF1[i], CDF2))
    return lut

gray_image1 = cv2.imread('gray1.jpg',cv2.IMREAD_GRAYSCALE)
copy_image1 = cv2.imread('gray1.jpg',cv2.IMREAD_GRAYSCALE)
gray_image2 = cv2.imread('gray2.jpg',cv2.IMREAD_GRAYSCALE)


histogram1 = getHist(gray_image1)
histogram2 = getHist(gray_image2)


CDF1 = getCDF(histogram1,gray_image1)
CDF2 = getCDF(histogram2,gray_image2)


LUT = getLUT(CDF1, CDF2)


# print(CDF1)
# print(CDF2)
# print(LUT)



#thuc hien can bang anh clone_gray_image1
for i in range(len(gray_image1)):
    for j in range(len(gray_image1)):
        copy_image1[i][j] = LUT(copy_image1[i][j])



show_image_with_result(gray_image1,copy_image1)

histogramResult = getHist(copy_image1)



plt.plot(histogramResult, color='k')
# plt.plot(histogram2, color='k')
plt.show()










