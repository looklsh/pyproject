from matplotlib import pyplot as plt
import numpy as np
import argparse
import cv2
#도스 창에서 명령어를 입력하기 위한 argparse
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True, help = "Path to the image file")
args = vars(ap.parse_args())
#image를 불러온다.
image = cv2.imread(args["image"])
cv2.imshow("image", image)
cv2.waitKey(0)

