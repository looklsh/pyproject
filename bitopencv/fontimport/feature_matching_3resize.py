#-*- encoding: utf8 -*-

import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

class compareImg:
    def __init__(self):
        pass

    def readImg(self, filepath):
        # cv2에서 utf8 경로 처리 못해서 Python 에서 불러와서 imdecode
        with open(filepath, "rb") as f:
            bytes = bytearray(f.read())

        bytes = np.asarray(bytes, dtype=np.uint8)
        imgg = cv.imdecode(bytes, cv.IMREAD_GRAYSCALE)
        ret, imgb = cv.threshold(imgg, 80, 255, cv.THRESH_BINARY)
        return imgb

    def diffImg(self, img1, img2):
        # Initiate SIFT detector
        orb = cv.ORB_create()
        # ORB는 키포인트 검출을 위해 FAST를, 알고리즘 성능형상을 위해 많은 수정을 가한 BRIEF 디스크립터를 혼합 적용한
        # 알고리즘임
        # 키포인트를 찾기 위해 FAST를 사용하며 찾은 키포인트들 중 최상위 N개를 추출하기 위해 다양한 스케일의 피라미드 적용
        # 회전 불편 특성 추출하기 위해 조정된 BRIEF 디스크립터를 적용

        # find the keypoints and descriptors with SIFT
        kp1, des1 = orb.detectAndCompute(img1, None)
        kp2, des2 = orb.detectAndCompute(img2, None)

        # create BFMatcher object
        bf = cv.BFMatcher_create(cv.NORM_HAMMING, crossCheck=True)

        # Match descriptors
        matches = bf.match(des1, des2)

        # Sort them in the order of their distance
        matches = sorted(matches, key=lambda x:x.distance)

        # BFMatcher with default params
        bf = cv.BFMatcher()
        matches = bf.knnMatch(des1, des2, k=2)

        # Apply ratio test
        good = []
        for m, n in matches:
            if m.distance < 0.75 * n.distance:
                good.append([m])

        # Draw first 10 matches
        knn_image = cv.drawMatchesKnn(img1, kp1, img2, kp2, good, None, flags=2)
        print(good)
        plt.imshow(knn_image)
        plt.show()

    def run(self):
        # 이미지 파일 경로 설정
        # filepath1 = cv.imdecode(np.fromfile(u'.\\abc\\ga\\malgun_ga.png',
        #                                     np.uint8), cv.IMREAD_UNCHANGED)
        filepath1 = "../images/gajua_ga.png"

        # filepath1 = "./abc/ga/malgun_ga.png"

        # filepath2 = cv.imdecode(np.fromfile(u'.\\abc\\ga\\malgun_ga.png',
        #                                     np.uint8), cv.IMREAD_UNCHANGED)
        filepath2 = './abc/가/HANSolM_가.png'
        # filepath2 = "./abc/ga/malgun_ga.png"

        # 이미지 객체 가져옴
        img1 = self.readImg(filepath1)
        img2 = self.readImg(filepath2)
        # img2 = cv.resize(img2, dsize=(0, 0), fx=0.7, fy=0.5, interpolation=cv.INTER_AREA)
        # cv.imwrite('./copyga1.png', img2)


        # 2개의 이미지 비교
        self.diffImg(img1, img2)

if __name__ == '__main__':
    cImg = compareImg()
    cImg.run()



