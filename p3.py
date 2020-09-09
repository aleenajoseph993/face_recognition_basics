from google.colab.patches import cv2_imshow
img = cv2.imread('ah.png')
crop_img = img[70:200, 300:500]
cv2_imshow(img)
cv2_imshow(crop_img)
mod_img = cv2.rectangle(img,(300,50),(500,200),(255,0,0),5)
cv2_imshow(mod_img)
cv2.waitKey(0)
cv2.destroyAllWindows()