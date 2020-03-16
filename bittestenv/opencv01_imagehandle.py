import cv2

img_color = cv2.imread('D:\\pyproject\\bittestenv\\notebook\\images\\jamong.jpg', cv2.IMREAD_COLOR)

cv2.namedWindow('Show image')
cv2.imshow('Show image', img_color)
cv2.waitKey(0)

img_gray = cv2.cvtColor(img_color, cv2.COLOR_BGR2GRAY)
cv2.imshow('Show grayscaleimage', img_gray)
cv2.waitKey(0)

cv2.imwrite('D:\\pyproject\\bittestenv\\notebook\\images\\jamong2.jpg', img_gray)
cv2.destroyAllWindows()