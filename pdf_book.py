"""
workflow
1. pdf to images (color and gray)
2. handwork (select color or gray)
3. images to pdf
4. 이 코드는 grayscale png -> pdf -> png 변환은 실패한다.
   변환해야 한다면 LibreOffice Draw -> 내보내기 -> HTML 을 사용하면 된다.
"""

import os
import cv2
import numpy as np

from pdf import *
from path import *
from image import *


if __name__ == "__main__":
    mode = ["0_original", "1_pdf_to_images", "2_convert_gray",
            "3_convert_color", "4_images_to_pdf"]
    select = 4

    if mode[select] == "1_pdf_to_images":
        src_path = mode[0]
        trg_path = mode[1]
        pdfs = get_all_paths(src_path, trg_path, "*.pdf")

        for pdf in pdfs:
            trg_dir = pdf.replace(src_path, trg_path)
            trg_dir = trg_dir.replace(".pdf", "")
            mkdir(trg_dir)
            pdf_to_images(pdf, trg_dir)

    if mode[select] == "2_convert_gray":
        src_path = mode[1]
        trg_path = mode[2]
        images = get_all_paths(src_path, trg_path, "*.png")

        for image in images:
            trg = image.replace(src_path, trg_path)
            img = convert_page(image, cv2.IMREAD_GRAYSCALE)
            img = histogram_compress(img)
            #img = remove_finger(img)
            imwrite(trg, img)

    if mode[select] == "3_convert_color":
        src_path = mode[1]
        #trg_path = mode[3]
        trg_path = mode[2]
        images = get_all_paths(src_path, trg_path, "*.png")

        for image in images:
            trg = image.replace(src_path, trg_path)
            img = convert_page(image, cv2.IMREAD_COLOR)
            imwrite(trg, img)

    if mode[select] == "4_images_to_pdf":
        src_path = mode[2]
        trg_path = mode[4]
        dirs = get_dirs(src_path)

        for d in dirs:
            mkdir(d.replace(src_path, trg_path))
            images = get_files(d, "*.png")
            if len(images) > 0:
                trg = d.replace(src_path, trg_path) + ".pdf"
                images_to_pdf(images, trg)
