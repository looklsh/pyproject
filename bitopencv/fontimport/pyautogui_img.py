import pyautogui as pg
import cv2 as cv


# print(pg.position( ))

# pg.moveTo(27, 433)
# pg.click(27, 433)

print(pg.position())

pg.screenshot('ree.jpg', region=(1510, 453, 100, 100))

# num1 = pg.locateCenterOnScreen('1.jpg')
# pg.click(num1)