#Reading and displaying the image
#RGB(Colored Image!!)
#RGB has 3 channels(red,gree,blue)
#RGB and BGR is same(both are colored image)

import cv2

#read the image
img = cv2.imread('cat.jpg')

print(img.shape)#(980, 1468, 3)
print(img.ndim)#3


# #To display the image
# cv2.imshow("this is image",img)

# cv2.waitKey(3000)#image closes within 3 seconds



while True:
    #display image
    cv2.imshow("image",img)
    
    #press 'q' to quit the image
    if cv2.waitKey(1) == ord('q'):
        break
    
cv2.destroyAllWindows()



