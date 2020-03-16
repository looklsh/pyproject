# -*- encoding: utf-8 -*-
from PIL import Image
from pytesseract import *
import cv2 as cv
import numpy as np


filename = r'../images/CaptureFont/beer_mo.png'
image = Image.open(filename)
print(image)
image = np.array(image)
dst = cv.resize(image, dsize=(400,400), interpolation=cv.INTER_CUBIC)

# print(type(dst), dst.shape)

grayscale = cv.cvtColor(dst, cv.COLOR_BGR2GRAY)
kernel_size_row = 3
kernel_size_col = 3
kernel = np.ones((5,5), np.uint8)

dilation_image = cv.dilate(grayscale, kernel, iterations=1)
# ret, img_result = cv.threshold(grayscale, 127, 255, cv.THRESH_BINARY)

cv.namedWindow('erosion_image', cv.WINDOW_NORMAL)
cv.imshow("erosionimg", dilation_image)
cv.waitKey()
# cv.imshow("img", dst)
# cv.waitKey()
text = image_to_string(dst, lang='kor+eng')
print("[", text, "]")

with open('D:\\pyproject\\bitopencv\\images\\poster_ocr\\mo_ocr.txt', 'w') as f:
    f.write(text)