import os
import cv2
import numpy as np


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


def get_ratio(img):
    h, w = (img.shape[0], img.shape[1])
    w = w/h
    h = 1
    return h, w


def histogram_compress(img):
    img = np.array(img/25, dtype=np.int) * 25
    img[img > 235] = 255
    img = np.array(img, dtype=np.float32)
    return img


def remove_background(img, thresh=150):
    #img = resize(img)
    h = int(img.shape[0]/12)
    w = int(img.shape[1]/8)
    clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(h, w))
    equalized = clahe.apply(img)
    # equalized = cv2.equalizeHist(img)

    _, threshold = cv2.threshold(equalized, thresh, 255, cv2.THRESH_BINARY)
    img = cv2.add(img, threshold)
    return img


def convert_page(src_path, mode):
    ff = np.fromfile(src_path, np.uint8)
    img = cv2.imdecode(ff, mode)
    img = remove_background(img)
    return resize(img)
