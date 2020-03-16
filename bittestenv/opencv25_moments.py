# 윤곽선이나 이미지의 0차 모멘트부터 3차 모멘트까지 계산하는 알고리즘
# 공간 모멘트, 중심 모멘트, 정규화된 중심 모멘트, 질량중심 모멘트등을 계산

import cv2 as cv

src = cv.imread('D:\\pyproject\\bittestenv\\notebook\\images\\convex.png')
dst = src.copy()

gray = cv.cvtColor(src, cv.COLOR_RGB2GRAY)
ret, binary = cv.threshold(gray, 150, 255, cv.THRESH_BINARY_INV)

contours, hierarchy = cv.findContours(binary, cv.RETR_CCOMP, cv.CHAIN_APPROX_NONE)

for i in contours:
    M = cv.moments(i, False) # 배열, 이진화 이미지
    # 배열은 윤곽선 검출함수에서 반환되는 구조 또는 이미지 사용
    # 이진화 이미지는 입력된 배열 매개변수가 이미지일 경우 이미지의 픽셀 값들을 이진화 처리할 지 결정
    # True를 할당하면 이미지의 픽셀 값이 0이 아닌 값은 모두 1의 값으로 변경해 모멘트 계산
    # 모멘트 함수를 통해 면적 평균 분산 등을 간단하게 구할 수 있음

    cX = int(M['m10']/M['m00'])
    cY = int(M['m01']/M['m00'])

    cv.circle(dst, (cX, cY), 3, (255, 0, 0), -1)
    cv.drawContours(dst, [i], 0, (0, 0, 255), 2)

cv.imshow('dst', dst)

cv.waitKey(0)
cv.destroyAllWindows()