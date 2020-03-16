# 영상이나 이미지의 크기를 원하는 크기로 조절

import cv2 as cv

# src = cv.imread('D:\\pyproject\\bittestenv\\notebook\\images\\pawns.jpg', cv.IMREAD_COLOR)
#
# dst = src.copy() # 이미지는 numpy형식과 동일
# dst = src[100:600, 200:700] # List형식과 동일
#
# cv.imshow('src', src)
# cv.imshow('dst', dst)
#
# cv.waitKey(0)
# cv.destroyAllWindows()


src = cv.imread('D:\\pyproject\\bittestenv\\notebook\\images\\pawns.jpg', cv.IMREAD_COLOR)

dst = src.copy()
roi = src[100:600, 200:700]
dst[0:500, 0:500] = roi # dst이미지에 해당영역을 붙여넣을 수 있음

cv.imshow('src',src)
cv.imshow('dst', dst)

cv.waitKey(0)
cv.destroyAllWindows()