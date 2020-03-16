import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img = cv.imread('./abc/ga/HANSolM_ga.png', 0)
# hist = cv.calcHist([img], [0], None, [256], [0, 256])

color = ('b', 'g', 'r')
for i, col in enumerate(color):
    histr = cv.calcHist([img], [i], None, [256], [0, 256])
    plt.plot(histr, color=col)
    plt.xlim([0, 256])
    plt.ylim([0, 12500])

plt.show()
