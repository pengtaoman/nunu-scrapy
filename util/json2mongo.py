import keyword

import ijson

import pymongo


class Json_Mongo():
    __mongo_client = None
    __mongo_db = None
    __mongo_col = None

    mongo_col = None

    # "mongodb://mongoadmin:mongoadmin@localhost:47017/"
    def __init__(self, mongo_url, mongo_db, mongo_col):
        '''

        :param mongo_url: mongodb url
        :param mongo_db: mongdb database name
        :param mongo_col: mongdb col name
        '''
        self.__mongo_client = pymongo.MongoClient(mongo_url)
        self.__mongo_db = self.__mongo_client[mongo_db]
        self.__mongo_col = self.__mongo_db[mongo_col]

    def insert_mongo(self, json_item):
        self.__mongo_col.insert_one(json_item)

    def json2mongo(self, file_name):
        with open(file_name, 'r', encoding='utf-8') as f:
            obj = ijson.items(f, 'item')
            cnt = 0
            while True:
                try:
                    # print(obj.__next__())
                    self.insert_mongo(obj.__next__())
                except StopIteration as e:
                    print("数据读取完成")
                    break


def queryjsonfile(file_name, **kwargs):
    with open(file_name, 'r', encoding='utf-8') as f:
        obj = ijson.items(f, 'item')
        cnt = 0
        while True:
            try:
                objec = obj.__next__()
                ische = 0
                for k, v in kwargs.items():
                    if v == '':
                        ische = ische + 1
                        continue
                    if isinstance(objec[k], list):
                        if len([1 for ele in objec[k] if ele.find(v) != -1]) > 0:
                            ische = ische + 1
                    if isinstance(objec[k], str) and objec[k].find(v) != -1:
                        ische = ische + 1
                if ische == len(kwargs):
                    ische = 0
                    yield objec
            except StopIteration as e:
                print("数据读取完成")
                break

def condi():
    print()

if __name__ == '__main__':
    # jm = Json_Mongo('mongodb://mongoadmin:mongoadmin@localhost:47017/', 'nunu', 'movie')
    # jm.json2mongo('/Users/pengtao/work/tmp/movie.json')
    query = {
        'name': '',
        'year': '',
        'country': '日本',
        'category': '伦理',
        'rate': '6',
        'actor': ''
        }
    for mm in queryjsonfile('/Users/pengtao/work/tmp/movie.json', **query):
        print(mm)
