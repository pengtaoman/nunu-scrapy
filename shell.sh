scrapy crawl teleplay -o teleplay.json

cd ./web
uvicorn fapi:app --reload


