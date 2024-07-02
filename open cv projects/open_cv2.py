#To convert RBG IMAGE to GRAY SCALE image

import cv2

#how to read the image
#Method 1: to conver rgb to gray scale
# img = cv2.imread('cat.jpg',0)




#Method 2: to convert rgb to gray scale
img = cv2.imread("cat.jpg")
gray_img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
#dimension of gray image(2 dimension) | rgb dimension(3 dimension)
print(gray_img.ndim)#2 dim



cv2.imshow("gray image: ",gray_img)
cv2.waitKey(3000)#3seconds


