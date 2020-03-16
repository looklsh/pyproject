# 윤곽선(컨투어) 검출하기 위해 사용
# 영상이나 이미지에서 외곽과 내곽의 윤곽선을 검출

import cv2 as cv

src = cv.imread('D:\\pyproject\\bittestenv\\notebook\\images\\contours.png', cv.IMREAD_COLOR)
gray = cv.cvtColor(src, cv.COLOR_BGR2GRAY)

ret, binary = cv.threshold(gray, 127, 255, cv.THRESH_BINARY)
binary = cv.bitwise_not(binary)
# 윤곽선을 검출하는 주된 요소는 하얀색의 객체를 검출
# 배경은 검은색이며 검출하려는 물체는 하얀색의 성질을 띄게끔 변형
# 이진화 처리 후 반전 시켜 검출하려는 물체를 하얀색의 성질을 띄도록 변환

contours, hierarchy = cv.findContours(binary, cv.RETR_CCOMP, cv.CHAIN_APPROX_NONE)
# findContours함수로 이진화 이미지에서 윤곽선을 검색
# 이진화 이미지, 검색방법, 근사화방법
# 반환 값으로 윤곽선, 계층 구조를 반환
# 윤곽선은 numpy구조 배열, 검출된 윤곽선의 지점들이 담겨짐
# 계층 구조는 윤곽선의 계층 구조
# 각 윤곽선에 해당하는 속성 정보들이 담겨있음

for i in range(len(contours)): # 반복문을 사용하여 검출된 윤곽선을 그리며 해당 윤곽선의 계층 구조를 표시
    cv.drawContours(src, [contours[i]], 0, (0, 0, 255), 1) # 검출된 윤곽선을 그림
    # 이미지, 윤곽선, 윤곽선 인덱스, 색, 두께, 선형타입
    # 윤곽선은 검출된 윤곽선들이 저장된 numpy 배열
    # 윤곽선 인덱스는 검출된 윤곽선 배열에서 몇번째 인덱스의 윤곽선을 그릴지 의미
    # 윤곽선 인덱스가 0이면 0번째 인덱스의 윤곽선을 그림
    # 하지만 윤곽선 인수를 대괄호로 다시 묶으면 0번째 인덱스가 최대값이 배열로 변경
    # [윤곽선], 0 == 윤곽선, -1   -1은 윤곽선 배열 모두를 의미
    cv.putText(src, str(i), tuple(contours[i][0][0]), cv.FONT_HERSHEY_COMPLEX, 0.8, (0, 255, 0), 1)

    print(i, hierarchy[0][i])
    cv.imshow('src', src)
    cv.waitKey(0)

cv.destroyAllWindows()

# 검색 방법
# cv2.RETR_EXTERNAL : 외곽 윤곽선만 검출하며, 계층 구조를 구성하지 않습니다.
# cv2.RETR_LIST : 모든 윤곽선을 검출하며, 계층 구조를 구성하지 않습니다.
# cv2.RETR_CCOMP : 모든 윤곽선을 검출하며, 계층 구조는 2단계로 구성합니다.
# cv2.RETR_TREE : 모든 윤곽선을 검출하며, 계층 구조를 모두 형성합니다. (Tree 구조)

# 근사화 방법
# cv2.CHAIN_APPROX_NONE : 윤곽점들의 모든 점을 반환합니다.
# cv2.CHAIN_APPROX_SIMPLE : 윤곽점들 단순화 수평, 수직 및 대각선 요소를 압축하고 끝점만 남겨 둡니다.
# cv2.CHAIN_APPROX_TC89_L1 : 프리먼 체인 코드에서의 윤곽선으로 적용합니다.
# cv2.CHAIN_APPROX_TC89_KCOS : 프리먼 체인 코드에서의 윤곽선으로 적용합니다.

# 계층구조는 윤곽선을 포함관계의 여부
# hierarchy에 담겨져 있음
# [다음 윤곽선, 이전 윤곽선, 내곽 윤곽선, 외곽 윤곽선]
# 윤곽선의 정보가 -1이 아니라면 서로 동등한 계층