import cv2
import numpy as np

apple = cv2.imread('apple.jpg')
orange = cv2.imread('orange.jpg')

print(apple.shape)
print(orange.shape)

apple_orange = np.hstack((apple[:, :256], orange[:, 256:]))
# cv2.imshow('Image', apple_orange)

# Generate Guassian Pyramid for Apple

apple_copy = apple.copy()
gp_apple = [apple_copy]

for i in range(6):
    apple_copy = cv2.pyrDown(apple_copy)
    gp_apple.append(apple_copy)

# Generate Guassian Pyramid for Orange

orange_copy = orange.copy()
gp_orange = [orange_copy]

# Generate Laplacian Pyramid for Apple

apple_copy = gp_apple[5]
lp_apple = [apple_copy]

for i in range(5, 0, -1):
    guassian_expanded = cv2.pyrUp(gp_apple[i])
    laplacian = cv2.subtract(gp_apple[i-1], guassian_expanded)
    lp_apple.append(laplacian)

for i in range(6):
    orange_copy = cv2.pyrDown(orange_copy)
    gp_orange.append(orange_copy)

# Generate Laplacian Pyramid for Orange

orange_copy = gp_orange[5]
lp_orange = [orange_copy]

for i in range(5, 0, -1):
    guassian_expanded = cv2.pyrUp(gp_orange[i])
    laplacian = cv2.subtract(gp_orange[i-1], guassian_expanded)
    lp_orange.append(laplacian)

# Now add left and right half images of each level

apple_orange_pyramid = []
n = 0

for apple_lap, orange_lap in zip(lp_apple, lp_orange):
    n += 1
    cols, rows, ch = apple_lap.shape
    laplacian = np.hstack((apple_lap[:, 0:int(cols/2)], orange_lap[:, int(cols/2):]))
    apple_orange_pyramid.append(laplacian)

# Reconstruct

apple_orange_reconstruct = apple_orange_pyramid[0]

for i in range(1, 6):
    apple_orange_reconstruct = cv2.pyrUp(apple_orange_reconstruct)
    apple_orange_reconstruct = cv2.add(apple_orange_pyramid[i], apple_orange_reconstruct)

cv2.imshow('Apple', apple)
cv2.imshow('Orange', orange)
cv2.imshow("Apple_Orange", apple_orange)
cv2.imshow("Apple_Orange_Reconstruct", apple_orange_reconstruct)
cv2.waitKey(0)
cv2.destroyAllWindows()