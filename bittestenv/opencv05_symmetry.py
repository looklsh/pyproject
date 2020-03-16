import cv2 as cv

src = cv.imread('D:/pyproject/bittestenv/notebook/images/glass.jpg', cv.IMREAD_COLOR)
dst = cv.flip(src, 1)
# flipcode(대칭방법)==0: 상하 대칭, flipcode(대칭방법)==1: 좌우 대칭
# 상수를 0보다 낮은값을 입력하면 상하대칭으로 간주하고 1보다 큰 값을 입력하면 좌우대칭으로 간주함
cv.imshow('src', src)
cv.imshow('dst', dst)

cv.waitKey(0)
cv.destroyAllWindows()