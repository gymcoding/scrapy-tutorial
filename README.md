# Scrapy Tutorial
Python 크롤링 오픈소스 프레임워크인 Scrapy의 튜토리얼 실습 코드입니다.

# Requirements
- [Python](https://www.python.org/)
- [Scrapy](https://scrapy.org/)
- [VSCode 툴](https://code.visualstudio.com/)

# Install
```sh
git clone https://github.com/gymcoding/scrapy-tutorial.git
```

# Getting started
```sh
scrapy crawl movie
```

# Settings
## ITEM_PIPELINES
- `tutorial.pipelines.CsvPipeline`
    - CSV로 저장하는 파이프라인
- `tutorial.pipelines.XmlPipeline`
    - XML로 저장하는 파이프라인
- `tutorial.pipelines.JsonPipeline`
    - Json로 저장하는 파이프라인
- `scrapy.pipelines.images.ImagesPipeline`
    - 이미지를 저장하는 파이프라인
