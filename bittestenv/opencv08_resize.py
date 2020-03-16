import cv2 as cv

src = cv.imread('D:\\pyproject\\bittestenv\\notebook\\images//champagne.jpg', cv.IMREAD_COLOR)

dst = cv.resize(src, dsize=(640, 480), interpolation=cv.INTER_AREA)
# (원본이미지, 결과이미지크기, 보간법)
# 결과 이미지 크기는 튜플형
# 보간법은 이미지의 크기를 변경하는 경우 변형된 이미지의 픽셀은 추정해서 값을 할당
dst2 = cv.resize(src, dsize=(0, 0), fx=0.3, fy=0.7, interpolation=cv.INTER_LINEAR)
# (원본이미지크기, 결과이미지크기, 가로비, 세로비, 보간법)
# 결과이미지(0, 0)크기를 설정하지 않은 경우 가로비와 세로비를 이용하여 비율 조절
# 결과이미지크기와 가로비 세로비가 모두 설정된 경우 결과 이미지크기 값으로 이미지의 크기가 조절

cv.imshow('src', src)
cv.imshow('dst', dst)
cv.imshow('dst2', dst2)

cv.waitKey(0)
cv.destroyAllWindows()

# interpolation 속성
# - cv.INTER_NEAREST: 이웃 보간법
# - cv.INTER_LINEAR: 쌍 선형 보간법
# - cv.INTER_LINEAR_EXACT: 비트 쌍 선형 보간법
# - cv.INTER_CUBIC: 바이큐빅 보간법
# - cv.INTER_AREA: 영역 보간법
# - cv.INTER_LANCZOS4: Lanczos 보간법

# 기본적으로 cv.INTER_LINEAR가 많이 사용
# 이미지를 확대하는 경우: cv.INTER_CUBIC, cv.INTER_LINEAR 가장 많이 사용
# 이미지를 축소하는 경우: cv.INTER_AREA 를 가장 많이 사용
# cv.INTER_AREA에서 이미지를 확대하는 경우 cv.INTER_NEAREST과 비슷한 결과를 반환