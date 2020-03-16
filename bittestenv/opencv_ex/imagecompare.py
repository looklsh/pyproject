import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

class compareImg:
    def __init__(self):
        pass

    def readImg(self, filepath):
        img = cv.imread(filepath, cv.IMREAD_GRAYSCALE)
        cv.namedWindow('root', cv.WINDOW_NORMAL) # 윈도우 생성
        cv.imshow('root', img) # 윈도우에 이미지 띄우기
        cv.waitKey(5000) # 5초 기다림, 아무키나 입력하면 대기 종료
        cv.destroyAllWindows()
        return img

    def run(self):
        # 이미지 파일 경로 설정
        filepath1 = r'D:\\pyproject\\bitopencv\\images\\gajua_ga.png'
        filepath2 = r'D:\\pyproject\\bitopencv\\images\\gajua_ga.png'

        # 이미지 객체 가져옴
        img1 = self.readImg(filepath1)
        img2 = self.readImg(filepath2)

if __name__ == '__main__':
    cImg = compareImg()
    cImg.run()

