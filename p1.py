 
import cv2
img = cv2.imread('ah.png')
crop_img = img[70:200, 300:500]
cv2.imshow("original image",img)
cv2.imshow("cropped image", crop_img)
cv2.waitKey(0)
cv2.distroyallwindow(s)