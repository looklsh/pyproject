import cv2 as cv

# src = cv.imread('D:\\pyproject\\bittestenv\\notebook\\images\\tomato.jpg', cv.IMREAD_COLOR)
# hsv = cv.cvtColor(src, cv.COLOR_BGR2HSV)
# h, s, v = cv.split(hsv)
#
# cv.imshow('h', h)
# cv.imshow('s', s)
# cv.imshow('v', v)
#
# cv.waitKey(0)
# cv.destroyAllWindows()

src = cv.imread('D:\\pyproject\\bittestenv\\notebook\\images\\tomato.jpg', cv.IMREAD_COLOR)
hsv = cv.cvtColor(src, cv.COLOR_BGR2HSV)
h, s, v = cv.split(hsv)

h = cv.inRange(h, 8, 20) # hue의 범위를 조정하여 특정 색상만 출력할 수 있음
# inRange함수(단일채널이미지, 최소값, 최대값)를 이용하여 범위를 설정
# 주황색은 8~20 범위임
orange = cv.bitwise_and(hsv, hsv, mask=h)
# 해당 마스크를 이미지 위에 덧씌워 해당부분만 출력
# bitwise_and(원본, 원본, mask=단일채널이미지)이용하여 마스크만 덧씌움
orange = cv.cvtColor(orange, cv.COLOR_HSV2BGR)
# 다시 hsv->bgr로 변경
cv.imshow('src', src)
cv.imshow('orange', orange)

cv.waitKey(0)
cv.destroyAllWindows()

# 색상(h): 0~180 의 값을 지님
# 채도(s): 0~255
# 명도(v): 0~255