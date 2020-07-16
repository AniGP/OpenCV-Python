import cv2
import numpy as np

img = cv2.imread('lena.jpg')
layer = img.copy()
guassian_pyramid_list = [layer]

for i in range(6):
    layer = cv2.pyrDown(layer)
    guassian_pyramid_list.append(layer)
    cv2.imshow(str(i), layer)

layer = guassian_pyramid_list[5]
cv2.imshow('Upper Level Guassian Pyramid', layer)
laplacian_pyramid_list = [layer]


for i in range(5, 0, -1):
    guassian_extended = cv2.pyrUp(guassian_pyramid_list[i])
    laplacian = cv2.subtract(guassian_pyramid_list[i-1], guassian_extended)
    cv2.imshow(str(i), laplacian)

cv2.imshow('Original Image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

