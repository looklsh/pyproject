import datetime
import cv2 as cv

capture = cv.VideoCapture('D:\\pyproject\\bittestenv\\notebook\\images\\mydesk.mp4')
fourcc = cv.VideoWriter_fourcc(*'XVID')
record = False

while True:
    if(capture.get(cv.CAP_PROP_POS_FRAMES) == capture.get(cv.CAP_PROP_FRAME_COUNT)):
        capture.open('D:\\pyproject\\bittestenv\\notebook\\images\\mydesk.mp4')
    ret, frame = capture.read()
    cv.imshow('VideoCapture', frame)

    now = datetime.datetime.now().strftime('%d_%H-%M-%S') # 날짜, 시간, 분, 초
    key = cv.waitKey(33)

    if key == 27: # esc
        print('종료')
        break
    elif key == 48: # 0
        print('캡쳐')
        cv.imwrite('D:\\' + str(now) + '.png', frame)
    elif key == 49: # 1
        print('녹화 시작')
        record = True
        video = cv.VideoWriter('D:\\' + str(now) + '.avi', fourcc, 20.0, (frame.shape[1], frame.shape[0]))
        # FPS = 20: 영상이 바뀌는 속도 즉 화면의 부드러움 의미
    elif key == 50: # 2
        print('녹화 중지')
        record = False
        video.release()

    if record == True:
        print('녹화 중')
        video.write(frame)

capture.release()
cv.destroyAllWindows()
