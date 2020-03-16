import cv2 as cv

src = cv.imread('D:\\pyproject\\bittestenv\\notebook\\images\\geese.jpg', cv.IMREAD_COLOR)

gray = cv.cvtColor(src, cv.COLOR_RGB2GRAY)
ret, dst = cv.threshold(gray, 100, 255, cv.THRESH_BINARY) # ret, dst를 이용해 이진화 결과를 저장
# ret에는 임계값이 저장
# cv.threshold(그레이스케일이미지, 임계값, 최댓값, 임계값 종류)를 이용하여 이진화 이미지로 변경
# 임계값은 이미지의 흑백을 나눌 기준값(100보다 이하면 0, 100이상이면 최댓값으로 변경)
# 임계값 종류를 이용해 이진화할 방법 설정

cv.imshow('dst', dst)

cv.waitKey(0)
cv.destroyAllWindows()

# cv2.THRESH_BINARY: 임계값 이상 = 최댓값 임계값 이하 = 0
# cv2.THRESH_BINARY_INV: 임계값 이상 = 0 임계값 이하 = 최댓값
# cv2.THRESH_TRUNC: 임계값 이상 = 임계값 임계값 이하 = 원본값
# cv2.THRESH_TOZERO: 임계값 이상 = 원본값 임계값 이하 = 0
# cv2.THRESH_TOZERO_INV: 임계값 이상 = 0 임계값 이하 = 원본값
# cv2.THRESH_MASK: 흑색 이미지로 변경
# cv2.THRESH_OTSU: Otsu 알고리즘 사용
# cv2.THRESH_TRIANGLE: Triangle 알고리즘 사용