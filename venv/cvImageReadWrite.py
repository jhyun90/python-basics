import cv2

img = cv2.imread('/Users/i-mac/Downloads/hello.jpg', cv2.IMREAD_COLOR)
cv2.imshow('HELLO', img)
cv2.waitKey(0)

cv2.destroyAllWindows()

img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow('HELLO_', img_gray)
cv2.waitKey(0)
