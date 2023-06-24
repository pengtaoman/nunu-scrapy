#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 11 23:22:01 2023

@author: pengtao
"""
# In[1]:
import json

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

import ijson
# In[1]:
class PanFlask():
    categories = [
        '剧情', '喜剧', '动作', '爱情', '科幻', '悬疑', '惊悚', '恐怖', '犯罪', '同性', '音乐', '歌舞', '传记', '历史', '战争', '西部', '奇幻', '冒险',
        '灾难', '武侠', '伦理'
    ]

    countries = [
        '中国大陆', '美国', '香港', '台湾', '日本', '韩国', '英国', '法国', '德国', '意大利', '西班牙', '印度', '泰国', '俄罗斯', '伊朗', '加拿大', '澳大利亚',
        '爱尔兰', '瑞典', '巴西', '丹麦'
    ]

    movie_data = pd.DataFrame()
    teleplay_data = pd.DataFrame()

    def load_movie_data(self):
        PanFlask.movie_data = pd.read_json("../json/movie.json")
        PanFlask.teleplay_data = pd.read_json("../json/teleplay.json")
        # PanFlask.movie_data = pd.read_json("../json/movie.json")
        PanFlask.movie_data.loc[:, "year"] = PanFlask.movie_data["year"].str.replace("(", "").astype('str')
        PanFlask.movie_data.loc[:, "year"] = PanFlask.movie_data["year"].str.replace(")", "").astype('int32')
        (PanFlask.movie_data.rate).apply(lambda x: float(x))
        
        PanFlask.teleplay_data.loc[:, "year"] = PanFlask.teleplay_data["year"].str.replace("(", "").astype('str')
        PanFlask.teleplay_data.loc[:, "year"] = PanFlask.teleplay_data["year"].str.replace(")", "").astype('int32')
        (PanFlask.teleplay_data.rate).apply(lambda x: float(x))

    def getdata(self):
        return PanFlask.movie_data.head().to_string()

    def search_movie(self, page, **que):

        md = PanFlask.movie_data
        # print('M'*100)
        # print(len(md.index))
        # print(que['name'])
        # print('M' * 100)

        if que['name'] != '':
            md = md[md.name.str.contains(que['name'])]
        if que['year'] != '':
            md = md[md.year == int(que['year'])]
        if que['category'] != '':
            md = md[md.category.str.join('-').str.contains(que['category'])]
        if que['rate'] != '':
            # md = md[(md.rate >= int('6')) & (md.rate < int('6') + 1)]
            md = md[(md.rate >= int(que['rate'])) & (md.rate < int(que['rate']) + 9)]
        if que['actor'] != '':
            md = md[md.actor.str.join('-').str.contains(que['actor'])]
        if que['country'] != '':
            md = md[md.country.str.join('-').str.contains(que['country'])]

        md = md[(int(page) - 1) * int(40): (int(page) * int(40))]
        # print('V'*100)
        # print(len(md.index))
        # print('V' * 100)
        # # print(md)
        # print('D' * 100)
        # # return md
        return md.iterrows()


    def search_teleplay(self, page, **que):

        md = PanFlask.teleplay_data
        # print('M'*100)
        # print(len(md.index))
        # print(que['name'])
        # print('M' * 100)

        if que['name'] != '':
            md = md[md.name.str.contains(que['name'])]
        if que['year'] != '':
            md = md[md.year == int(que['year'])]
        if que['category'] != '':
            md = md[md.category.str.join('-').str.contains(que['category'])]
        if que['rate'] != '':
            md = md[(md.rate >= int(que['rate'])) & (md.rate < int(que['rate']) + 9)]
        if que['actor'] != '':
            md = md[md.actor.str.join('-').str.contains(que['actor'])]
            md = md[md.country.str.join('-').str.contains(que['country'])]

        md = md[(int(page) - 1) * int(40): (int(page) * int(40))]
        # print('V'*100)
        # print(len(md.index))
        # print('V' * 100)
        # print(md)
        # print('D' * 100)
        # return md
        return md.iterrows()

#if __name__ == '__main__':
# In[1]:
pp = PanFlask()
pp.load_movie_data()
    
    # df = pp.movie_data
# In[1]:
query = {
    'name': '',
    'year': '',
    'country': '中国大陆',
    'director': '',
    'category': '犯罪',
    'rate': '',
    'actor': ''
    }
# In[1]:
md = None
md = PanFlask.teleplay_data
# print('M'*100)
# print(len(md.index))
# print(que['name'])
# print('M' * 100)

if query['name'] != '':
    md = md[md.name.str.contains(query['name'])]
if query['year'] != '':
    md = md[md.year == int(query['year'])]
if query['category'] != '':
    #if query['category'] in md.category
    #md = md[md.category.str.join('-').str.contains(query['category'])]
    # print(query['category'] + '#######################################################')
    # print(len(md.category))
    #md = md[md.category.str=='[\'剧情\', \'爱情\', \'同性\']']
    md['isCatagory'] = md['category'].apply(lambda x: query['category'] in x)
    md = md[md['isCatagory'] == True] 
if query['rate'] != '':
    md = md[(md.rate >= int(query['rate'])) & (md.rate < int(query['rate']) + 9)]
if query['actor'] != '':
    md['isActor'] = md['actor'].apply(lambda x: query['actor'] in x)
    md = md[md['isActor'] == True] 
    # md = md[md.actor.str.join('-').str.contains(query['actor'])]
if query['country'] != '':
    md['isCountry'] = md['country'].apply(lambda x: query['country'] in x)
    md = md[md['isCountry'] == True] 
    # md = md[md.country.str.join('-').str.contains(query['country'])]
    


# for index, row in md.iterrows():
#     print(type(row[1]))
        
    #while im in md:
    #    im.

    #md = md[(int(page) - 1) * int(40): (int(page) * int(40))]
    # print('V'*100)
    # print(len(md.index))
    # print('V' * 100)
    # print(md)
    # print('D' * 100)
    # return md
 
    #itr = pp.search_teleplay(1, **query)
    # tu = next(itr)
    
# In[1]:  
    # print(type(tu[1]))
    # print(type(tu[1].to_json()))
    # print(type(json(tu[1].to_json())))
    # print(tu[1].to_json())
    # js = tu[1].to_json()
    # print(tu[1].to_json())
    # print(tu[1]['name'])

    # kkkk = json.loads(tu[1].to_json())
    # print(type(kkkk))
