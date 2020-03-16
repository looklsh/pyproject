import cv2 as cv

src = cv.imread('D:\\pyproject\\bittestenv\\notebook\\images\\jadu.jpg', cv.IMREAD_COLOR)

dst = cv.blur(src, (5, 5), anchor=(-1, -1), borderType=cv.BORDER_DEFAULT)
# 원본이미지, (커널x크기, 커널y크기), 앵커포인트, 픽셀 외삽법
# 커널크기는 이미지에 흐림 효과를 적용할 크기를 설정, 크기가 클수록 많이 흐려짐
# 앵커포인트는 커널에서의 중심점을 의미, (-1, -1)로 사용할 경우 자동으로 커널의 중심점으로 할당

cv.imshow('src', src)
cv.imshow('dst', dst)

cv.waitKey(0)
cv.destroyAllWindows()