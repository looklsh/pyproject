# 기하학적 변환
# 영상이나 이미지를 펼치거나 좁힐 수 있음
# warpperspective의 경우 4개의 점을 매핑
# warpaffine의 경우 3개의 점을 매핑

import numpy as np
import cv2 as cv

src = cv.imread('D:\\pyproject\\bittestenv\\notebook\\images\\harvest.jpg', cv.IMREAD_COLOR)
height, width, channel = src.shape

src_point = np.array([[300, 200], [400, 200], [500, 500], [200, 500]], dtype=np.float32)
dst_point = np.array([[0, 0], [width, 0], [width, height], [0, height]], dtype=np.float32)
# 원본 이미지에서 4점 변환할 src_point와 결과 이미지의 위치가 될  dst_point를 선언
# 좌표 순서는 좌상, 우상, 우하, 좌하 순서
# numpy형태, 좌표 순서는 원본 순서와 동일해야 함
# dtype을 float32로 해야 사용가능
matrix = cv.getPerspectiveTransform(src_point, dst_point)
# 기하학적 변환을 위해 함수 사용하여 매트릭스 생성
print(matrix)
dst = cv.warpPerspective(src, matrix, (width, height))
# 이미지 변환: 저장된 매트릭스 값을 이용하여 이미지 변환
# 보간법, 픽셀외삽법을 추가 파라미터로 사용할 수 있음

cv.imshow('dst', dst)

cv.waitKey(0)
cv.destroyAllWindows()