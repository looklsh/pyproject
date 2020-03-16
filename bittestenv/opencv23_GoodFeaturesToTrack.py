# 코너 검출 알고리즘은 정확하게는 트래킹 하기 좋은 지점을 코너라 부름
# 꼭짓점은 트래킹 하기 좋은 지점이 되어 다각형이나 객체의 꼭짓점을 검출하는데 사용

import cv2 as cv

src = cv.imread('D:\\pyproject\\bittestenv\\notebook\\images\\coffee.jpg')
dst = src.copy()

gray = cv.cvtColor(src, cv.COLOR_BGR2GRAY)
corners = cv.goodFeaturesToTrack(gray, 100, 0.01, 5, blockSize=3, useHarrisDetector=True, k=0.03) # 코너 검출
# 입력이미지, 코너 최대값, 코너품질, 최소거리, 마스크, 블록크기, 해리스코너검출기 유/무, 해리스 코너계수
# 이미지는 단일채널 이미지
# 검출할 최대 코너의 수를 제한, 코너 최대값보다 낮은 개수만 반환
# 코너품질은 반환할 코너의 최소 품질 설정: 0~1사이 값으로 할당할 수 있고 일반적으로는 0.01~0.10사이의 값 사용
# 최소거리는 검출된 코너들의 최소 근접 거리, 설정된 최소거리 이상의 값만 검출
# 마스크는 입력이미지와 같은 차원 사용, 마스크 요솟값이 0인 곳은 코너로 계산하지 않음
# 블록 크기는 코너를 계산할 때 고려하는 코너 주변 영역의 크기 의미
# 해리스 코너 계수는 해리스 알고리즘을 사용할 때 할당라묘 해리스 대각합의 감도계수를 의미
# 코너품질에서 가장 좋은 코너의 강도가  1000, 코너 품질이 0.01이하면 10 이하의 코너강도를 갖는 코너들은 검출하지 않음
# 최소거리가 5일 경우 거리가 5 이하인 코너점은 검출하지 않음

print(corners)

for i in corners:
    cv.circle(dst, tuple(i[0]), 3, (0, 0, 255), 2)

cv.imshow('dst', dst)

cv.waitKey(0)
cv.destroyAllWindows()