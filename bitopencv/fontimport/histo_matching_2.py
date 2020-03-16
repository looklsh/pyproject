import cv2 as cv
import numpy as np

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

    # draw curve
    hist, bin = np.histogram(img.flatten(), 256, [0, 256]) # flatten()은 다차원 배열을 1차원 배열로 평평하게 해주는 함수
    cdf = hist.cumsum() # 히스토그램의 누적합
    cdf_normalized = cdf * float(hist.max()) / cdf.max()
    cv.normalize(cdf_normalized, cdf_normalized, 0, 255, cv.NORM_MINMAX)
    hist = np.int32(np.around(cdf_normalized))
    pts = np.int32(np.column_stack((bins, hist))) # 두 개의 1차원 배열을 세로로 붙여서 2차원 배열 만들기
    pts += [257, 10]
    print(pts)

    cv.line(h, (0+257,0+10), (0+257,5),(255,255,255))
    cv.line(h, (255+257,0+10), (255+257,5), (255,255,255))
    cv.polylines(h, [pts], False, (255,255,255))


    return y

img = cv.imread('./abc/ga/HANSolM_ga.png', cv.IMREAD_COLOR)
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

line = draw_histogram(gray)
result1 = np.hstack((gray, line))
cv.imshow('result1', result1)

# equ = cv.equalizeHist(gray)
hist, bin = np.histogram(img.flatten(), 256, [0, 256])
cdf = hist.cumsum()
cdf_mask = np.ma.masked_equal(cdf, 0) # cdf의 값이 0인 경우 mask처리를 하여 계산에서 제외시킴
cdf_mask = (cdf_mask - cdf_mask.min()) * 255 / (cdf_mask.max() - cdf_mask.min())
# 누적합의 최대값,최소값을 이용하여 히스토그램이 넓게 분포되도록 만들어주는 룩업 테이블을 만듬
cdf = np.ma.filled(cdf_mask, 0).astype('uint8') # mask처리를 했던 부분을 다시 0으로 변환
equ = cdf[gray]
# 룩업 테이블을 그레이스케일 이미지에 적용하여 히스토그램 평활화가 적용된 이미지를 얻음

line = draw_histogram(equ)
result2 = np.hstack((equ, line))
cv.imshow('result2', result2)

cv.waitKey(0)
cv.destroyAllWindows()