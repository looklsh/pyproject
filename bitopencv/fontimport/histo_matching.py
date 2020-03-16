import cv2 as cv
import numpy as np

# 그레이스케일 이미지 얻음
# img = cv.imread('../images/ara.jpg', cv.IMREAD_COLOR)
# gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
#
# cv.imshow('gray', gray)
#
# cv.imwrite('../images/grayara.jpg', gray)
#
# cv.waitKey(0)
# cv.destroyAllWindows()

bins = np.arange(256).reshape(256, 1)


def draw_histogram(img):
    h = np.zeros((img.shape[0], 256), dtype=np.uint8)


    hist_item = cv.calcHist([img], [0], None, [256], [0, 256])
    # images: uint8 or float32 타입의 이미지를 사용해야 하며 []안에 입력해야 함
    # channels: 히스토그램을 계산할 채널의 인덱스이며 []안에 입력해야함, 그레이스케이면[0], 컬러면 [0],[1],[2]중 하나 사용
    # 각각 파란색, 녹색, 빨간색 의미
    # mask: 마스크 이미지, 전체 이미지에 대한 히스토그램을 구할거면 None을 사용
    #       이미지 일부분에 대한 히스토그램을 구하려고 하면 마스크 이미지를 생성하여 제공해야 함
    # histsize: 계산할 히스토그램(bin)의 개수, []안에 입력해야 함, 여기서 전체영역이면 [256]
    # ranges: 히스토그램을 계산할 범위, 여기서 전체 픽셀 강도 범위를 계산하면 [0, 256]


    cv.normalize(hist_item, hist_item, 0, 255, cv.NORM_MINMAX)
    hist = np.int32(np.around(hist_item))

    for x, y in enumerate(hist):
        cv.line(h, (x,0+10), (x,y+10), (255,255,255))
        print(x, y)

    cv.line(h, (0,0+10), (0,5), (255,255,255))
    cv.line(h, (255,0+10), (255,5), (255,255,255))
    y = np.flipud(h) # Flip array in the up/down direction, 행은 보존하면서~

    return y

img = cv.imread('../images/sea.png', cv.IMREAD_COLOR)
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

line = draw_histogram(gray)
result1 = np.hstack((gray, line))
cv.imshow('result1', result1)

cv.waitKey(0)
cv.destroyAllWindows()



