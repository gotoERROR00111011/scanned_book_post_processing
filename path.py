import os

from glob import glob


def mkdir(path: str) -> None:
    if not os.path.exists(path):
        os.mkdir(path)


def get_dirs(path: str) -> list:
    """[summary]

    Args:
        path (str): [path of root directory]

    Returns:
        list: [all directories]
    """
    dirs = [path]
    for d in dirs:
        for filename in os.listdir(d):
            filepath = os.path.join(d, filename)
            if os.path.isdir(filepath):
                dirs.append(filepath)
    return dirs


def get_files(path: str, extention: str = "*") -> list:
    """[summary]

    Args:
        path (str): [path of directory]
        extention (str, optional): [filename extention : jpg, png, ...]. Defaults to "*"(all).

    Returns:
        list: [files path list]
    """
    files = []
    for filename in glob(os.path.join(path, extention)):
        files.append(filename)
    return files


def set_default_dirs():
    mkdir("00_src_pdf")
    mkdir("01_src_img")
    mkdir("02_gray_img")
    mkdir("03_result_pdf")
