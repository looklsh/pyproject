# 이미지 피라미드란 이미지의 크기를 변화시켜 원하는 단계까지 샘플링하는 작업
# 영상이나 이미지를 확대 축소 가능
import cv2 as cv

src = cv.imread('D:\\pyproject\\bittestenv\\notebook\\images\\fruits.jpg', cv.IMREAD_COLOR)
height, width, channel = src.shape
dst = cv.pyrUp(src, dstsize=(width*2, height*2), borderType=cv.BORDER_DEFAULT)
# cv.pyrUp으로 이미지를 2배 확대할 수 있음
# (원본이미지, 결과이미지크기, 픽셀외삽법)
# 픽셀 외삽법은 이미지를 확대나 축소 할 경우 영역밖 픽셀은 추정해서 값을 할당해야 함
# 이미지 밖의 픽셀을 외삽하는데 사용되는 테두리 모드 - 외삽 방식 설정
dst2 = cv.pyrDown(src)
# 피라미드 함수에서 픽셀외삽법은 cv.BORDER_DEFAULT만 사용가능
# 이미지를 1/4배, 1/8배, 4배, 8배등의 배율을 사용해야 하는 경우 반복문을 이용하여 적용
cv.imshow('src', src)
cv.imshow('dst', dst)
cv.imshow('dst2', dst2)

cv.waitKey(0)
cv.destroyAllWindows()