import cv2

def nothing(x):
    pass

cv2.namedWindow('Binary')
cv2.createTrackbar('threshold', 'Binary', 0, 255, nothing)
cv2.setTrackbarPos('threshold', 'Binary', 127)

img_color = cv2.imread('D:\\pyproject\\bittestenv\\notebook\\images\\redball.jpg', cv2.IMREAD_COLOR)
cv2.imshow('Color', img_color)
cv2.waitKey(0)

img_gray = cv2.cvtColor(img_color, cv2.COLOR_BGR2GRAY)
cv2.imshow('Gray', img_gray)
cv2.waitKey(0)

while True:
    low = cv2.getTrackbarPos('threshold', 'Binary')
    ret, img_binary = cv2.threshold(img_gray, low, 255, cv2.THRESH_BINARY)
    cv2.imshow('binary', img_binary)

    if cv2.waitKey(1) & 0xFF == 27:
        break

cv2.destroyAllWindows()




