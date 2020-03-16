import cv2 as cv
import numpy as np

src = np.zeros((768, 1366, 3), dtype=np.uint8)

cv.line(src, (100, 100), (1200, 100), (0, 0, 255), 3, cv.LINE_AA)
# 선 그리기
# 선형타입은 선의 연결성을 의미
cv.circle(src, (300, 300), 50, (0, 255, 0), cv.FILLED, cv.LINE_4)
# 원그리기
# 내부를 채우는 경우 cv.filled사용
cv.rectangle(src, (500, 200), (1000, 400), (255, 0 , 0), 5, cv.LINE_8)
# 사각형 그리기
cv.ellipse(src, (1200, 300), (100, 50), 0, 90, 180, (255, 255, 0), 2)
#타원 그리기
# 이미지, (x, y), (lr, sr), 각도, 시작각도, 종료각도, (b, g, r), 두께, 선형타입
# 중심에서 가장 먼 거리를 가지는 lr과 가장 가까운 거리를 가지는 sr의 타원을 각도만큼 기울어진 타원을 생성
# 시작각도와 종료 각도를 설정하여 호의 형태로 그리며 (b,g,r)색상, 두께굵기의 타원을 그림
# 선형타입은 설정하지 않아도 사용할 수 있음

pts1 = np.array([[100, 500], [300, 500], [200, 600]]) # numpy형태로 저장된 위치 좌표
# n개의 점이 저장된 경우 n각형을 그릴 수 있음
pts2 = np.array([[600, 500], [800, 500], [700, 600]])
cv.polylines(src, [pts1], True, (0 ,255, 255), 2)
# 다각형 그리기
cv.fillPoly(src, [pts2], (255, 0, 255), cv.LINE_AA)
# 내부가 채워진 다각형 그리기

cv.putText(src, 'LEESEUNGHWE', (900, 600), cv.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 3)
# 문자 그리기
# 문자 위치는 좌표의 좌측하단을 기준으로 생성

cv.imshow('src', src)

cv.waitKey(0)
cv.destroyAllWindows()

# 선형타입 종류
# cv2.FILLED: 내부 채우기
# cv2.LINE_4: 4점 이웃 연결
# cv2.LINE_8: 8점 이웃 연결
# cv2.LINE_AA: AntiAlias

# 글꼴 종류
# cv2.FONT_HERSHEY_SIMPLEX: 보통 크기의 산세리프 글꼴
# cv2.FONT_HERSHEY_PLAIN: 작은 크기의 산세리프 글꼴
# cv2.FONT_HERSHEY_DUPLEX: 보통 크기의 산세리프 글꼴	정교함
# cv2.FONT_HERSHEY_COMPLEX: 보통 크기의 세리프 글꼴
# cv2.FONT_HERSHEY_TRIPLEX: 보통 크기의 세리프 글꼴	정교함
# cv2.FONT_HERSHEY_COMPLEX_SMALL: 작은 크기의 손글씨 글꼴
# cv2.FONT_HERSHEY_SCRIPT_SIMPLEX: 보통 크기의 손글씨 글꼴
# cv2.FONT_HERSHEY_SCRIPT_COMPLEX: 보통 크기의 손글씨 글꼴	정교함
# cv2.FONT_ITALIC: 기울임 꼴

# 추가 옵션
# shift : 좌표를 Shift(비트 연산)만큼 이동시켜 표시합니다.
# offset : 좌표를 (x, y)만큼 이동시켜 표시합니다.
