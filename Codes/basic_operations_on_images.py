import numpy as np
import cv2

img = cv2.imread('messi5.jpg')
img1 = cv2.imread('opencv-logo.png')

print(img.shape) # returns a tuple of number of rows, columns and channels
print(img.size) # returns total number of pixels that is accessed
print(img.dtype) # returns image datatype that is obtained

b, g, r = cv2.split(img)
img=cv2.merge((b, g, r))

ball = img[280:340, 330:390]
img[273:333, 100:160] = ball

img = cv2.resize(img, (512, 512))
img1 = cv2.resize(img1, (512, 512))

# dst = cv2.add(img, img1);
dst = cv2.addWeighted(img, 0.9, img1, 0.1, 0);

cv2.imshow('Image', dst)

# cv2.imshow('Image', dst) # shows an error, since the size of the two images are not matching ( before using resize() )
cv2.waitKey(0)
cv2.destroyAllWindows()
