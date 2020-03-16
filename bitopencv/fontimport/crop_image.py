# 마우스 클릭으로 drag&drop해서 ROI추출

import argparse
import cv2 as cv

# Points들을 저장할 리스트와 crop이 실행 되었는지 저장할 boolean변수를 선언
refPt = []
cropping = False

def click_and_crop(event, x, y, flags, param): # callback함수 선언, 클릭 이벤트마다 콜백 함수가 실행
    # refPt와 cropping 변수를 global로 만듬
    global refPt, cropping

    # 왼쪽 마우스가 클릭되면 (x, y)좌표 기록을 시작하고
    # cropping = True로 만들어줌
    if event == cv.EVENT_LBUTTONDOWN:
        refPt = [(x, y)]
        cropping = True

    # 왼쪽 마우스 버튼이 놓여지면 (x, y)좌표 기록을 하고 cropping작업을 끝냄
    # 이 때 crop한 영역을 보여줌
    elif event == cv.EVENT_LBUTTONUP:
        refPt.append((x, y))
        cropping = False

        # ROI사각형을 이미지에 그림
        cv.rectangle(image, refPt[0], refPt[1], (0, 255, 0), 2)
        cv.imshow('image', image)

        # 여기까지 프로세싱은 마우스 왼쪽 클릭이 되면 좌표 저장
        # 마우스 왼쪽 클릭이 놓아지면 놓아진 좌표지점 저장하고 이미지에 사각형 표시

# argument parser를 구성해주고 입력받은 argument는 parse함
ap = argparse.ArgumentParser() # ArgumentParser는 명령행을 파이썬 데이터형으로 파싱하는데 필요한 모든정보를 담고 있음
ap.add_argument('-i', '--D:/pyproject/bitopencv/images/beer.jpg', required=True, help='Path to the image')
# ArgumentParser에 프로그램 인자에 대한 정보를 채우려면 add_argument()메서드 호출하면 됨
args = vars(ap.parse_args()) # ArgumentParser는 parse_args()메서드를 통해 인자를 파싱
# 명령행을 검사하고 각 인자를 적절한 형으로 변환한 다음 적절한 액션을 호츨

# 이미지를 load함
image = cv.imread(args['image'])
# 원본 이미지를 clone하여 복사해 둠
clone = image.copy()
# 새 윈도우 창을 만들고 그 윈도우 창에 click_and_crop함수를 세팅
cv.namedWindow('image')
cv.setMouseCallback('image', click_and_crop)


'''
키보드에서 다음을 입력받아 수행
- q: 작업을 끝냄
- r: 이미지를 초기화
- c: ROI사각형을 그리고 좌표를 출력
'''

while True:
    # 이미지를 출력하고 key입력을 기다림
    cv.imshow('image', image)
    key = cv.waitKey(1) & 0xFF

    # 만약 r이 입력되면 crop할 영역을 리셋
    if key == ord('r'):
        image = clone.copy()

    # 만약 c가 입력되고 ROI박스가 정확하게 입력되었다면
    # 박스의 좌표를 출력하고 CROP한 영역을 출력
    elif key == ord('c'):
        if len(refPt) == 2:
            roi = clone[refPt[0][1]:refPt[1][1], refPt[0][0]:refPt[1][0]]
            print(refPt)
            cv.imshow('ROI', roi)
            cv.waitKey(0)
    # 만약 q가 입력되면 작업을 끝냄
    elif key == ord('q'):
        break

cv.destroyAllWindows()

