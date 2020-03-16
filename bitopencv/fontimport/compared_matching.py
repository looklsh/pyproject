import cv2
import numpy as np

def load_image(file_path):
    with open(file_path):
        with open(file_path, "rb") as f:
            bytes = bytearray(f.read())
        bytes = np.array(bytes, dtype=np.uint8)
        img = cv2.imdecode(bytes, cv2.IMREAD_ANYCOLOR)
        return img

def compare(fname1, fname2):
    img1 = load_image(fname1)
    img2 = load_image(fname2)
    keypoints = detect_keypoints(img1)
    print("keypoints", keypoints)
    img1_with_keypoints = cv2.drawKeypoints(img1, keypoints, None)
    cv2.imshow("FAST", img1_with_keypoints)
    cv2.waitKey()
    cv2.destroyAllWindows()

def detect_keypoints(image):
    grayscale = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    gftt = cv2.GFTTDetector_create()
    keypoints = gftt.detect(grayscale, None)
    print("This image has {} keypoints:".format(len(keypoints)))
    return keypoints

def main():
    file_path1 = "./abc/가/HANSolM_가.png"
    file_path2 = "../images/CaptureFont/gajua_ga.png"
    compare(file_path1, file_path2)

if __name__ ==  "__main__":
    main()
