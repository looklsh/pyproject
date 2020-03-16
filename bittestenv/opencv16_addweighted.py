# 영상이나 이미지의 색상을 검출할 때 inRange의 영역이 한정되어 색상을 설정하는 부분이 한정되어 있음
# 특정 범위들을 병합할 때 사용
import cv2 as cv

src = cv.imread('D:\\pyproject\\bittestenv\\notebook\\images\\tomato.jpg', cv.IMREAD_COLOR)
hsv = cv.cvtColor(src, cv.COLOR_BGR2HSV)
h, s, v = cv.split(hsv)

lower_red = cv.inRange(hsv, (0,100,100), (5,255,255)) # 빨간색 영역: 0 ~ 5
upper_red = cv.inRange(hsv, (170,100,100), (180,255,255)) # 빨간색 영역: 170 ~ 180
# 다채널이미지, (채널1최소값, 채널2최소값, 채널3최소값), (채널1최대값, 채널2최대값, 채널3최대값)
# hsv형식이므로 각각의 h,s,v범위를 한 번에 설정
added_red = cv.addWeighted(lower_red, 1.0, upper_red, 1.0, 0.0) # 이미지1, 비율, 이미지2, 비율, 가중치
# 채널을 하나로 합침
# 그대로 함칠 것이므로 비율은 1.0, 가중치는 0 할당
red = cv.bitwise_and(hsv, hsv, mask=added_red)
red = cv.cvtColor(red, cv.COLOR_HSV2BGR)

cv.imshow('red', red)

cv.waitKey(0)
cv.destroyAllWindows()