import ijson

import pymongo

class Json_Mongo():

    __mongo_client = None
    __mongo_db = None
    __mongo_col = None
    
    mongo_col = None

    #"mongodb://mongoadmin:mongoadmin@localhost:47017/"
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

    def read_jsonfile(self, file_name):
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


if __name__ == '__main__':
    jm = Json_Mongo('mongodb://mongoadmin:mongoadmin@localhost:47017/', 'nunu', 'movie')
    jm.read_jsonfile('/Users/pengtao/work/tmp/movie.json')
