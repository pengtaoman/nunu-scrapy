import keyword

import ijson

import pymongo

categories = [
'剧情','喜剧','动作','爱情','科幻','悬疑','惊悚','恐怖','犯罪','同性','音乐','歌舞','传记','历史','战争','西部','奇幻','冒险','灾难','武侠','伦理'
]

countries = [
'中国大陆','美国','香港','台湾','日本','韩国','英国','法国','德国','意大利','西班牙','印度','泰国','俄罗斯','伊朗','加拿大','澳大利亚','爱尔兰','瑞典','巴西','丹麦'
]

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
    print('#'*40)
    print('读文件：' + file_name)
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
                    if k == 'rate':
                        if float(objec[k]) > float(v):
                            ische = ische + 1
                    elif isinstance(objec[k], str) and objec[k].find(v) != -1:
                        ische = ische + 1
                if ische == len(kwargs):
                    ische = 0
                    yield objec
            except StopIteration as e:
                print("数据读取完成")
                break

def queryjsonfilepage(file_name, frompage, topage, **kwargs):
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
                    if k == 'rate':
                        if float(objec[k]) > float(v):
                            ische = ische + 1
                    elif isinstance(objec[k], str) and objec[k].find(v) != -1:
                        ische = ische + 1
                if ische == len(kwargs):
                    ische = 0
                    cnt = cnt + 1
                    if cnt < int(frompage) or cnt > int(topage):
                        # print(cnt)
                        continue
                    objec['total'] = cnt
                    yield objec

            except StopIteration as e:
                print("数据读取完成")
                break

def condi():
    print()

if __name__ == '__main__':
    # jm = Json_Mongo('mongodb://mongoadmin:mongoadmin@localhost:47017/', 'nunu', 'teleplay')
    # jm.json2mongo('/Users/pengtao/work/tmp/teleplay.json')
    query = {
        'name': '',
        'year': '',
        'country': '',
        'category': '悬疑',
        'rate': '8',
        'actor': ''
        }
    for mm in queryjsonfilepage('/Users/pengtao/work/tmp/teleplay.json', 36, 45, **query):
        print(mm)
