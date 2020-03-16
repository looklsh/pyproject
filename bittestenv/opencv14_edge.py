import cv2 as cv

src = cv.imread('D:\\pyproject\\bittestenv\\notebook\\images\\wheat.jpg', cv.IMREAD_COLOR)
gray = cv.cvtColor(src, cv.COLOR_BGR2GRAY)

canny = cv.Canny(src, 100, 255) # 원본이미지, 임계값1, 임계값2, 커널크기, l2그라디언트
# 임계값1 이하에 포함된 가장자리는 가장자리에서 제외
# 임계값2는 임계값 이상에 포함된 가장자리는 가장지리로 간주
# 커널크기는 sobel마스크의 Aperture Size를 의미, 포함하지 않을 경우 자동으로 할당
# l2그라디언트는 l2 방식의 사용 유/무결정, 사용하지 않을 경우 자동으로 l1그라디언트 방식 사용

sobel = cv.Sobel(gray, cv.CV_8U, 1, 0, 3) # 그레이스케일, 정밀도, x미분, y미분, 커널, 배율, 델타, 픽셀외삽법
# 정밀도는 결과이미지의 정밀도-결과물이 달라질 수 있음
# x방향 미분은 이미지에서 x방향으로 미분할 값 설정
# y방향 미분은 이미지에서 y방향으로 미분할 값 설정
# 커널은 소벨 커널의 크기 설정 : 1, 3, 5, 7의 값 사용
# 배율은 계산된 미분값에 대한 배율값
# 델타는 계산 전 미분값에 대한 추가값
# x,y 방향 미분값의 합이 1이상이어야 하며 각각의 값은 0보다 커야 함

laplacian = cv.Laplacian(gray, cv.CV_8U, ksize=3) # 그레이스케일, 정밀도, 커널, 배율, 델타, 픽셀외삽법
# 커널은 2차 미분 필터의 크기 설정: 1, 3, 5, 7값 사용
# 커널의 값이 1일 경우 3x3 Aperture Size사용 (중심값=-4)

cv.imshow('canny', canny)
cv.imshow('sobel', sobel)
cv.imshow('laplacian', laplacian)

cv.waitKey(0)
cv.destroyAllWindows()

