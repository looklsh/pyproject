# -*- encoding: utf-8 -*-
from PIL import Image
from pytesseract import *



filename = r'../images/poster/finance.jpg'
image = Image.open(filename)
text = image_to_string(image, lang='kor+eng')

with open('D:\\pyproject\\bitopencv\\images\\poster_ocr\\finance_ocr.txt', 'w') as f:
    f.write(text)
