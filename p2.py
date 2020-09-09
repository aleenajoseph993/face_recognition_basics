 import cv2
img = cv2.imread('ah.png')
cv2.imshow("original image",img)
mod_img = cv2.rectangle(img,(300,50),(500,200),(255,0,0),5)
cv2.imshow("modified image",mod_img)
cv2.waitKey(0)
cv2.distroyallwindow(s)