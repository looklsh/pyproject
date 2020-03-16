import cv2 as cv

src = cv.imread('D:\\pyproject\\bittestenv\\notebook\\images\\ara.jpg', cv.IMREAD_COLOR)

height, width, channel = src.shape # 높이, 너비, 채널값 저장, 높이와 너비 이용해 회전 중심점을 설정
matrix = cv.getRotationMatrix2D((width/2, height/2), 90, 1) # 중심좌표, 화전각도, 이미지확대배율
# 중심점은 tuple형태이며 기준점을 설정
# 변환행렬을 만들 때 getRotationMatrix2D 사용
dst = cv.warpAffine(src, matrix, (width, height)) # 원본이미지, 배열, (결과이미지너비, 결과이미지높이) 회전함수 적용
# 결과 이미지의 너비와 높이로 크기가 선언되며 배열에 따라 이미지가 회전
# 변환행렬을 실제 이미지에 적용하여 어파인 변환을 할 때 warpAffine함수 사용
cv.imshow('src', src)
cv.imshow('dst', dst)
cv.waitKey(0)

cv.destroyAllWindows()
