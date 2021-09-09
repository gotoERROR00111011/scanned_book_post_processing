<!--
- Title
- Banner
- Badges
- Short Description
- Long Description
- Table of Contents
- Security
- Background
- Install
- Usage
- Extra Sections
- API
- Maintainers
- Thanks
- Contributing
- License
-->

<!--Title-->

# scanned_book_post_processing

<!-- Banner-->
<!--
<div align="center">
  <img src="images/banner.png">
</div>
-->

<!-- Badges-->
<!--
[![Python](https://img.shields.io/pypi/pyversions/tensorflow.svg?style=plastic)](https://badge.fury.io/py/tensorflow)
-->

<!-- Short or Long Description-->

vFlat 으로 scan 한 책을 post processing

<!-- Table of Contents-->

## Contents

1. [Background](##Background)
1. [Install](##Install)
1. [Usage](##Usage)
1. [API](##API)
1. [Maintainers](##Maintainers)
1. [Contributing](##Contributing)
1. [License](##License)

<!-- Security-->

<!-- Background-->

## Background

vFlat의 경우 스마트폰 카메라로 촬영하기 때문에 빛, 그림자 등으로 문제가 생긴다. 또한 정보 대비 용량이 크다. 스캔한 pdf 파일을 후처리 하여 위의 문제를 해결하는 것을 목표로 하는 프로젝트이다.

<!-- Install-->

## Install

### Dependencies

```
# windows 10
# anaconda
# python 3.8.5
pip install -r requirements.txt
conda install -c conda-forge poppler
```

<!-- Usage-->

## Usage

```sh
$python path.py
$python pdf_to_img.py
$python img_to_pdf.py
```

1. `path.py`를 실행하여 디렉토리 생성
1. `00_src_pdf`에 변환할 pdf 파일 삽입
1. `pdf_to_img.py`를 실행하여 pdf를 이미지로 변환
1. `01_src_img`(color) 표지 등 색이 필요한 이미지를 `02_trg_img`(gray) 로 이동
1. `img_to_pdf.py` 실행

<!-- Extra Sections-->

<!-- API-->

<!-- Maintainers-->

## Maintainers

[@gotoERROR00111011](https://github.com/gotoERROR00111011).

<!-- Thanks-->

<!-- Contributing-->

## Contributing

### Contributors

This project exists thanks to all the people who contribute.
<a href="https://github.com/gotoERROR00111011/scanned_book_post_processing/graphs/contributors"><img src="https://avatars.githubusercontent.com/u/20670685?s=60&v=4" /></a>

<!-- License-->

## License

UNLICENSE
