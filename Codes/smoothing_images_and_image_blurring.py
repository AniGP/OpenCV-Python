import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

img1 = cv.imread('lena.jpg')
img1 = cv.cvtColor(img1, cv.COLOR_BGR2RGB)
# img2 = cv.imread('opencv-logo.png')
# img3 = cv.imread('water.png')
# img4 = cv.imread('Halftone_Gaussian_Blur.jpg')

kernel = np.ones((5, 5), np.float32)/25
dst = cv.filter2D(img1, -1, kernel)
blur = cv.blur(img1, (5,5))
gblur = cv.GaussianBlur(img1, (5,5), 0)
median = cv.medianBlur(img1, 5)
bilateralFilter = cv.bilateralFilter(img1, 9, 75, 75)

titles = ['image', '2DConvolution', 'blur', 'GuassianBlur', 'median', 'bilateralFilter']
images = [img1, dst, blur, gblur, median, bilateralFilter ]

for i in range(6):
    plt.subplot(2, 3, i+1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])

plt.show()