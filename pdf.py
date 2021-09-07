import os
import img2pdf
#import PyPDF2

from pdf2image import convert_from_path

"""
# pdf 페이지 내부의 이미지 추출 기능
# 일부 png 확장자등에서 에러 발생

def page_to_image(page: "PageObject", trg_path: str) -> None:
    try:
        xObject = page['/Resources']['/XObject'].getObject()

        for obj in xObject:
            if xObject[obj]['/Subtype'] == '/Image':
                size = (xObject[obj]['/Width'], xObject[obj]['/Height'])
                #data = xObject[obj].getObject()
                data = xObject[obj]._data

                if xObject[obj]['/ColorSpace'] == '/DeviceRGB':
                    mode = "RGB"
                else:
                    mode = "P"

                img = open(f"{trg_path}.png", "wb")
                img.write(data)
                img.close()

                '''
                if xObject[obj]['/Filter'] == '/FlateDecode':
                    img = Image.frombytes(mode, size, data)
                    img.save(f"{trg_path}.png")
                elif xObject[obj]['/Filter'] == '/DCTDecode':
                    img = open(f"{trg_path}.jpg", "wb")
                    img.write(data)
                    img.close()
                elif xObject[obj]['/Filter'] == '/JPXDecode':
                    img = open(f"{trg_path}.jp2", "wb")
                    img.write(data)
                    img.close()    
                '''
            break
    except:
        return


def pdf_to_images(src_path: str, trg_dir: str) -> None:
    pdf = PyPDF2.PdfFileReader(open(src_path, 'rb'), strict=False)

    for page_num in range(pdf.getNumPages()):
        page = pdf.getPage(page_num)

        page_num = str(page_num)
        while len(page_num) < 4:
            page_num = "0" + page_num

        trg_path = os.path.join(trg_dir, page_num)
        page_to_image(page, trg_path)
"""


def pdf_to_images(src_path: str, trg_dir: str) -> None:
    convert_from_path(src_path, output_folder=trg_dir, fmt='jpg')


def images_to_pdf(images: list, trg_path: str) -> None:
    with open(trg_path, "wb") as f:
        f.write(img2pdf.convert([image for image in images]))
