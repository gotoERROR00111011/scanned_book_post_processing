import cv2
import numpy as np


def get_ratio(img):
    h, w = (img.shape[0], img.shape[1])
    w = w/h
    h = 1
    return h, w


def remove_background(img, thresh=220):
    if len(img.shape) == 2:
        _, threshold = cv2.threshold(img, thresh, 255, cv2.THRESH_BINARY)
    else:
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        _, threshold = cv2.threshold(gray, thresh, 255, cv2.THRESH_BINARY)
        threshold = cv2.cvtColor(threshold, cv2.COLOR_GRAY2BGR)
    img = cv2.add(img, threshold)
    return img


def histogram_compress(img):
    #img = np.array(img/5, dtype=np.int) * 5
    img = np.array(img/25, dtype=np.int) * 25
    img[img > 235] = 255
    img = np.array(img, dtype=np.float32)
    return img


def resize(img, height=1200):
    h, w = get_ratio(img)
    h = int(height * h)
    w = int(height * w)
    return cv2.resize(img, dsize=(w, h), interpolation=cv2.INTER_AREA)


def imwrite(trg_path, img):
    # 한국어 경로 문제 처리
    extension = os.path.splitext(trg_path)[1]
    result, encoded_img = cv2.imencode(extension, img)
    with open(trg_path, mode='w+b') as f:
        encoded_img.tofile(f)


def convert_page(src_path, mode):
    ff = np.fromfile(src_path, np.uint8)
    img = cv2.imdecode(ff, mode)
    #img = remove_background(img)
    return resize(img)


def remove_finger(img):
    h, w = (img.shape[0], img.shape[1])
    top, bottom = (0, h)
    left, right = (0, w)
    img = img[:, left + 30: right - 30]
    return img
