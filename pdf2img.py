from pdf import *
from path import *
# from image import *

set_default_dirs()

src_pdf_path = '00_src_pdf'
src_img_path = '01_src_img'
trg_img_path = '02_trg_img'
trg_pdf_path = '03_trg_pdf'

# pdfs to images
for pdf in get_all_paths(src_pdf_path, src_img_path, "*.pdf"):
    trg_dir = pdf.replace(src_pdf_path, src_img_path)
    trg_dir = trg_dir.replace(".pdf", "")
    mkdir(trg_dir)
    pdf_to_images(pdf, trg_dir)

# images to gray
