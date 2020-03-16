import cv2 as cv

src = cv.imread('D:\\pyproject\\bittestenv\\notebook\\images\\crow.jpg', cv.IMREAD_COLOR)

dst = cv.cvtColor(src, cv.COLOR_BGR2GRAY)

cv.imshow('src', src)
cv.imshow('dst', dst)

cv.waitKey(0)
cv.destroyAllWindows()