scrapy crawl teleplay -o teleplay.json

cd ./web
uvicorn fapi:app --reload



#安装uwsgi
# clang: error: no such file or directory: '/Users/pengtao/miniconda3/envs/nunu-scrapy/lib/python3.9/config-3.9-darwin/libpython3.9.a'
# 使用如下方式解决：
#cd /Users/pengtao/miniconda3/envs/nunu-scrapy/lib/python3.9/config-3.9-darwin/
#sudo ln -s ../../../lib/libpython3.9.dylib libpython3.9.a
#export LD_LIBRARY_PATH=/usr/local/anaconda/lib/


docker run -d --name nunu1 -p 8088:8088 pengtaoman/nunu:v0.4