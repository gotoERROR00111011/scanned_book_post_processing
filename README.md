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

### Why

종이책을 스캔하여 pdf로 만든 책들의 용량을 줄이기 위해 시작한 프로젝트입니다.  

책 스캔은 페이지마다 이미지 형태로 저장되기 때문에 전자책에 비해서 용량이 압도적으로 큽니다.  
그래서 책을 계속 스캔하면 용량 부담이 커진다는 점이 문제가 있었습니다.  
또한 한권의 용량이 크면 전자책 뷰어가 로딩하는데 오래걸리는 문제점도 있었습니다.  

### 아이디어 1 - width, height 축소

일반적으로 생각할 수 있는 가장 심플한 해결책입니다.  

width, height 를 각각 절반으로 줄이면 단순 계산으로 용량을 1/4 으로 줄일 수 있습니다.  
하지만 유의미하게 용량을 줄이려면 크기 축소가 과하게 일어날 우려가 있기 때문에 제외시켰습니다.

### 아이디어 2 - 이미지 압축 방식 활용

다른 방법인 이미지 압축을 활용한 방법입니다.  

이미지 저장은 크게 다음 3가지가 있습니다.  
- 원본저장(BMP)
- 무손실압축(PNG)
- 손실압축(JPG)

일반적으로 손실압축이 더 높은 압축률을 가진다고 알고 있습니다.  
데이터에 손실을 주면서까지 압축을 하기 때문입니다.  

하지만 책 데이터의 특성(흑,백)을 활용해 더 활용할 방법을 떠올려 그 방법을 적용했습니다.

### 이미지 데이터 압축

데이터의 압축은 반복되는 데이터를 더 작은 데이터로 표현하는 방법으로 이루어집니다.  
`AAAAABBBBBBBC -> A5B7C1` 처럼 반복되는 수를 입력하는 방법이 있습니다.  

이미지를 압축하는 방식은 다음과 같이 생각할 수 있습니다.  

데이터가 다음과 같은 상태입니다.  
- (검은색),(빨간색),(빨간색),(빨간색),(빨간색),(흰색)  
- (0,0,0),(255,0,0),(255,0,0),(255,0,0),(255,0,0),(255,255,255)  
- (00000000,00000000,00000000),(11111111,00000000,00000000),(11111111,00000000,00000000),(11111111,00000000,00000000),(11111111,00000000,00000000),(11111111,11111111,11111111)  

이 이미지 데이터를 한번 읽으며 색의 종류의 수를 계산합니다.  
- 검은색 = (0,0,0) = (00000000,00000000,00000000)  
- 빨간색 = (255,0,0) = (11111111,00000000,00000000)  
- 흰색 = (255,255,255) = (11111111,11111111,11111111)  

색의 종류에 id를 부여합니다.  
- 검은색 = 00
- 빨간색 = 01
- 흰색 = 10

원본 데이터를 id에 매핑합니다.  
- (00)(01)(01)(01)(01)(10)

원본 데이터와 비교하여 압축률을 확인할 수 있습니다.  
|원본|압축|
|---|---|
|12 bit|144 bit|
|000101010110|000000000000000000000000111111110000000000000000111111110000000000000000111111110000000000000000111111110000000000000000111111111111111111111111)|

색의 종류 이외의 특정 기준에 따라 반복되는 패턴을 찾을 수 도 있습니다.  
- 0, 1 의 반복 - 00:0000000000000000, 01:0000000011111111, 10:00000000, 11:11111111
- 색 반복 - 000:흑백흑백흑백, 001:적청녹적청녹, 010:흑백적청녹, 011:흑, 100:백, 101:적, 110:청, 111:녹 

### 데이터 압축 방식과 책 스캔 이미지

책 스캔 이미지는 보통 흑백입니다.  
컬러도 있지만, 가진 책 대부분이 흑백인 점을 우선시하여 컬러책은 제외하기로 합니다.  

그리고 이전에 알아본 압축 방식을 생각해보면 다음을 고려해야 합니다.  
- 반복이 많으면 압축 효율이 높다.
- 색의 종류가 적으면 효율이 높다.

책은 이 상황에 딱 맞습니다.  
- 흰색 배경의 반복
- 컬러(RGB)에 비해 적은 색의 종류

그런데 여기서 jpg에 대해서 생각할 점이 있습니다.  
흔히들 디지털 풍화라고 부르는, jpg 포맷으로 반복 캡쳐를 하는 경우를 생각해봅시다.  
jpg는 손실압축 과정에서 노이즈가 발생합니다.  
이는 지금 적용시키려는 최적화에 방해가 됩니다.  
따라서 지금 상황에는 png가 적합하다고 판단하였습니다.  

하지만 스캔의 경우 순수한 흑백이 아니고, 노이즈도 있기 전처리를 해주어야 합니다.  
그리고 0~255, 256가지 색상은 책에는 필요 이상으로 많기 때문에 색의 종류를 제한하는 처리를 해주었습니다.  

```py
# 0~255 => [0, 25, 50, 75, 100, 125, 150, 175, 200, 225, 255]
def histogram_compress(img):
    img = np.array(img/25, dtype=np.int) * 25
    img[img > 235] = 255
    img = np.array(img, dtype=np.float32)
    return img
```

### 결과

- 956 페이지
- 1390 * 1840

|원본(PNG)|원본(JPG)|JPG 압축|PNG 압축|
|---|---|---|---|
|1.05 GB|197 MB|366 MB|107 MB|

원본 pdf를 만들때는 jpg 이미지를 사용했었습니다.  
그래서 원본을 png로 바로 저장하면 용량이 증가합니다.  
그리고 png에 특화된 처리 이후 데이터를 jpg로 저장하면 오히려 용량이 증가하는 것을 확인할 수 있었습니다.

결론적으로 책의 컨텐츠 유형에 따라 차이는 있지만, 원본의 1/2 ~ 1/5 까지 압축하는데 성공했습니다.


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
