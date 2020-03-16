import cv2 as cv

src = cv.imread('D:\\pyproject\\bittestenv\\notebook\\images\\whitebutterfly.jpg', cv.IMREAD_COLOR)

dst = cv.bitwise_not(src) # 이미지 색상을 반전

cv.imshow('src', src)
cv.imshow('dst', dst)

cv.waitKey(0)
cv.destroyAllWindows()