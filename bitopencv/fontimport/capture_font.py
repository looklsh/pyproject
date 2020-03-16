import cv2 as cv

image = cv.imread('D:\\pyproject\\bitopencv\\images\\beer.jpg', cv.IMREAD_ANYCOLOR)

cv.namedWindow('beer', cv.WINDOW_NORMAL)
cv.resizeWindow('beer', 920, 1280)

cv.imshow('beer', image)



cv.waitKey(0)
cv.destroyAllWindows()

def im_trim(img):
    x = 230; y = 308;
    w = 157; h = 190;
    img_trim = img[y:y+h, x:x+w]
    cv.imwrite('D:\\pyproject\\bitopencv\\images\\org_trim.jpg', img_trim)
    return img_trim

org_image = cv.imread('D:\\pyproject\\bitopencv\\images\\beer.jpg')
trim_image = im_trim(org_image)