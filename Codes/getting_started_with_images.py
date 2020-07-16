import cv2

# img = cv2.imread('lena.jpg',-1)
img = cv2.imread('lena.jpg',0)
# img = cv2.imread('lena.jpg',1)

print(img)

cv2.imshow('Image', img)
# cv2.waitKey(5000)
k=cv2.waitKey(0) # & 0xFF # is preferred to use in a 64-bit method

if k == 27: # value of esc key
    cv2.destroyAllWindows()
elif k == ord('s'):
    cv2.imwrite('lena_copy.png', img) # if 's' key is pressed

cv2.destroyAllWindows()