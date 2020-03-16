# 다각형 근사
# 영상이나 이미지의 윤곽점을 압축해 다각형으로 근사하기 위해 사용
# 윤곽선의 근사 다각형을 검출 할 수 있음

import cv2 as cv

src = cv.imread('D:\\pyproject\\bittestenv\\notebook\\images\\phone.jpg', cv.IMREAD_COLOR)

gray = cv.cvtColor(src, cv.COLOR_BGR2GRAY)
ret, binary = cv.threshold(gray, 0, 255, cv.THRESH_BINARY)
binary = cv.bitwise_not(binary)

contours, hierarchy = cv.findContours(binary, cv.RETR_LIST, cv.CHAIN_APPROX_TC89_KCOS)

for contour in contours: # 반복문을 사용하여 색인값과 하위 윤곽선 정보로 반복
    epsilon = cv.arcLength(contour, True) * 0.02 # 근사치 정확도를 계산 하기 위해 윤곽선 전체 길이의 2%로 활용
    # .arcLength(윤곽선, 폐곡선)으로 윤곽선의 전체 길이 계산
    # 윤곽선은 검출된 윤곽선들이 저장된 numpy 배열
    # 폐곡선을 True로 사용하면 윤곽선이 닫혀 최종길이가 더 길어짐
    # print(epsilon)
    approx_poly = cv.approxPolyDP(contour, epsilon, True)
    # 윤곽선들의 윤곽점들로 근사해 근사 다각형으로 반환
    # 근사치 정확도는 입력된 다각형(윤곽선)과 반환될 근사화된 다각형 사이의 최대 편차 간격
    # 값이 낮을 수록 원본 윤곽과 유사
    for approx in approx_poly: # 근사 다각형을 반복해 근사점을 이미지 위에 표시
        cv.circle(src, tuple(approx[0]), 3, (255, 0, 0), -1)

cv.imshow('src', src)

cv.waitKey(0)
cv.destroyAllWindows()

# 다각형 근사는 더클라스-패커 알고리즘을 사용
# 반복과 끝점을 이용해 선분으로 구성된 윤곽선들을 더 적은 수의 윤곽점으로 동일하거나 비슷한 윤곽선으로 데시메이트
# 근사치 정확도의 값으로 기존 다각형과 윤곽점이 압축된 다각형의 최대 편차를 고려해 다각형을 근사
# 데시메이트: 알정간격으로 샘플링된 데이터를 기존 간격보다 더 큰 샘플링 간격으로 다시 샘플링 하는 것