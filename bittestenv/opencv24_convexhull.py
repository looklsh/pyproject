# 윤곽선( points, contours)의 경계면을 둘러싸는 다각형을 구하는 알고리즘
# 반환 결과는 윤곽선 검출효과와 동일한 형식, 스크랜스키 알고리즘을 이용해 입력된 좌표들의 볼록한 외곽을 찾음

import cv2 as cv

src = cv.imread('D:\\pyproject\\bittestenv\\notebook\\images\\convex.png')
dst = src.copy()

gray = cv.cvtColor(src, cv.COLOR_RGB2GRAY)
ret, binary = cv.threshold(gray, 150, 255, cv.THRESH_BINARY_INV)

contours, hierarchy = cv.findContours(binary, cv.RETR_CCOMP, cv.CHAIN_APPROX_NONE)

for i in contours:
    hull = cv.convexHull(i, clockwise=True) # 윤곽선, 방향
    # 방향: 검출된 볼록껍질의 볼록점들의 인덱스 순서 의미
    # 볼록껍질 함수는 단일형태에서만 검출 가능, 그러므로 반복문으로 단일형테의 윤곽선 구조에서 볼록껍질 검출
    # 윤곽선 구조는 윤곽선 검출 함수의 반환값과 형태가 동일하면 임의의 배열에서도 검출 가능
    # 방향이 True면 시계방향
    cv.drawContours(dst, [hull], 0, (0, 0, 255), 2)
    # print(i)
    print(hull)

cv.imshow('dst', dst)

cv.waitKey(0)
cv.destroyAllWindows()

# convex hull은 스크랜스키(sklansky) 알고리즘 사용
# 경계 사각형의 정점(vertex)검출
# 경계면은 둘러싸는 다각형은 경계 사각형 내부에 포함되며 해당 정점을 볼로점으로 검출
# 영역 내부에도 다양한 윤곽점들이 존재하므로 여기서 볼록껍질을 이루는 볼록점들을 선별해서 선택