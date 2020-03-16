# 영상이나 이미지를 채널을 나누고 합치기 위해 사용
# 채널을 b, g, r로 분리하여 채널을 변환할 수 있음

import cv2 as cv
import numpy as np
# src = cv.imread('D:\\pyproject\\bittestenv\\notebook\\images\\sausage.jpg', cv.IMREAD_COLOR)
# b, g, r = cv.split(src)
# inversebgr = cv.merge((r, g, b)) # 나눠진 채널을 다시 병합
# # 채널을 변형한 뒤 다시 합치거나 순서를 변경하여 병합할 수 있음
# # 순서가 변경되면 원본 이미지와 다른 색상으로 표현됨
#
# cv.imshow('b', b)
# cv.imshow('g', g)
# cv.imshow('r', r)
# cv.imshow('inverse', inversebgr)

src = cv.imread('D:\\pyproject\\bittestenv\\notebook\\images\\sausage.jpg', cv.IMREAD_COLOR)
b = src[:,:,0]
g = src[:,:,1]
r = src[:,:,2]
# 이미지[높이, 너비, 채널]을 이용해 특정영역의 특정채널만 불러올 수 있음
# :,:,n을 입력하면 이미지 높이와 너비는 그대로 반환하고 n번째 채널만 반환하여 적용

height, width, channel = src.shape
zero = np.zeros((height, width, 1), dtype=np.uint8)
# 검은색 빈 공간 이미지가 필요할 땐 np.zeros를 이용해 빈 이미지를 생성 할 수 있음
#  b,  g, z 이미지를 병합할 경우 r채널 영역이 모두 흑백 이미지로 변경
bgz = cv.merge((b, g, zero))

cv.imshow('bgz', bgz)

cv.waitKey(0)
cv.destroyAllWindows()
