from pdf import *
from path import *
from image import *

set_default_dirs()

src_pdf_path = '00_src_pdf'
src_img_path = '01_src_img'
trg_img_path = '02_trg_img'
trg_pdf_path = '03_trg_pdf'

dirs = get_dirs(trg_img_path)

for d in dirs:
    mkdir(d.replace(trg_img_path, trg_pdf_path))
    images = get_files(d, "*.*")
    if len(images) > 0:
        trg = d.replace(trg_img_path, trg_pdf_path) + ".pdf"
        images_to_pdf(images, trg)
