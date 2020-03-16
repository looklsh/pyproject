import cv2 as cv

capture = cv.VideoCapture('D:\\pyproject\\bittestenv\\notebook\\images\\mydesk.mp4')

while True:
    if(capture.get(cv.CAP_PROP_POS_FRAMES) == capture.get(cv.CAP_PROP_FRAME_COUNT)):
        # 현재 프레임 개수 = 총 프레임 개수
        capture.open('D:\\pyproject\\bittestenv\\notebook\\images\\mydesk.mp4')
        # 같을 경우 마지막 프레임이므로 다시 파일을 불러온다
    ret, frame = capture.read()
    cv.imshow('VideoFrame', frame)

    if cv.waitKey(33) > 0: # 33ms마다 프레임을 재생
            break

capture.release()
cv.destroyAllWindows()

# https://076923.github.io/posts/Python-opencv-4/

