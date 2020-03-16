from PIL import Image
import pytesseract
import argparse
import cv2 as cv
import os

image = cv.imread('C:\\Users\\BIT\\Desktop\\poster\\beer.jpg', cv.IMREAD_COLOR)
gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)

filename = '{}.jpg'.format(os.getpid())
cv.imwrite(filename, gray)

pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

text = pytesseract.image_to_string(Image.open(filename))
os.remove(filename)

print(text)