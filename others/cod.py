#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 14 11:18:23 2023

@author: pengtao
"""

# In[1]:
import pandas as pd
import numpy as np
import itertools


import timeit
import sys

data = np.array(['a','b','c','d'])
s = pd.Series(data)
print(s)


df = pd.read_json('json/movie.json')
df=df.head(10000)
print(df.axes)
df['moviename']=df['name']
df['movie_id']=df.index

df.loc[:, "year"] = df["year"].str.replace("(", "").astype('str')
df.loc[:, "year"] = df["year"].str.replace(")", "").astype('int32')
(df.rate).apply(lambda x: float(x))


category_list=list(itertools.chain.from_iterable(df['category'].values))
category_list = np.unique(category_list)

df_category=pd.DataFrame({'category':category_list})
df_category['cid']=df_category.index

actor_list=list(itertools.chain.from_iterable(df['actor'].values))
actor_list = np.unique(actor_list)
print(type(actor_list))
df_actor=pd.DataFrame({'actor':actor_list})
df_actor['aid']=df_actor.index


print(sys.getsizeof(df))

# df['category']=df['|'.join(df['category'])]


# df['category'] = df["category"].apply(lambda x: '|'.join(x),args=())

# df_name=df['category'].str.split('|',expand=True)

# In[1]:
df_category_temp=df['category'].apply(pd.Series)
df_category_temp

#使用stack行转列
df_category_temp=df_category_temp.stack()
     
df_category_temp = df_category_temp.reset_index(level=1, drop=True)
df_category_temp
df_category_temp.name='category'
df_new = df.drop(['category'], axis=1).join(df_category_temp)
df_new

# In[1]:
########
df_country_temp=df['country'].apply(pd.Series)
df_country_temp

#使用stack行转列
df_country_temp=df_country_temp.stack()
     
df_country_temp = df_country_temp.reset_index(level=1, drop=True)
df_country_temp
df_country_temp.name='country'
df_new = df_new.drop(['country'], axis=1).join(df_country_temp)
df_new

# In[1]:

print(sys.getsizeof(df_new))
# df_new = df_new.drop(['summary','name','director', 'actor','moviename','link'], axis=1)
print(sys.getsizeof(df_new))


# In[1]:

ddd = {'name':['asdf','asdf'],'age':['111','2222']}
ddddf = pd.DataFrame(ddd)

categories = {'category':[
    '剧情', '喜剧', '爱情','音乐', '歌舞', '传记', '冒险', '奇幻', '科幻', '悬疑', '惊悚', '恐怖', '犯罪', '历史', '战争', '灾难', '西部',  '动作','武侠',
     '伦理', '同性'], 'category_id':[i for i in range(1, 22, 1)]
}
cate_df = pd.DataFrame(categories)



countries = {'country':[
    '中国大陆','香港', '台湾', '美国', '英国', '法国', '加拿大', '澳大利亚', '德国', '意大利', '爱尔兰','西班牙', '俄罗斯', '伊朗','印度', '泰国', 
     '瑞典', '巴西', '丹麦','日本', '韩国',],'country_id':[i for i in range(1, 22, 1)]}

coun_df = pd.DataFrame(countries)


# In[1]:

    
df_category_merge = pd.merge(df_new, cate_df, how='left', on=['category'])

df_category_merge = pd.merge(df_category_merge, coun_df, how='left', on=['country'])

df_category_merge['category_id'] = df_category_merge['category_id'].fillna(-1)
df_category_merge['country_id'] = df_category_merge['country_id'].fillna(-1)
# In[1]:

# df_category_merge = df_category_merge.drop(['category'], axis=1)
# df_category_merge = df_category_merge.drop(['country'], axis=1)

# In[1]:

print(sys.getsizeof(df_category_merge))

# In[1]:
movie_be_compare = df_category_merge.iloc[8]
# df_category_merge.drop(['relate'], axis=1)

# df_category_merge['category_id']=df_category_merge['category_id'].apply(lambda x: x * 100)
# df_category_merge['rate']=df_category_merge['rate'].apply(lambda x: int(x))
# df_category_merge['rate'].astype(int)
df_final = df_category_merge
df_category_merge = df_category_merge.drop(['summary','director', 'actor','moviename','link', 'movie_id','year'], axis=1)
#‘  pearson   ’, ‘   kendall   ’, ‘   spearman   ’
similarity_movies = df_category_merge.corrwith(movie_be_compare, axis=1,
                                          method='kendall', numeric_only=True)
df_category_merge['relate']=similarity_movies



# ddddddd = pd.concat([df_category_merge, similarity_movies])
# similarity_movies['0']

# df_category_merge.corr('kendall')



# In[1]:

# 相关性的示例代码
datafff = np.array([[5, 5, 3, 3, 4], [3, 4, 5, 5, 4],
                 [3, 4, 3, 4, 5], [5, 5, 3, 4, 4]])
dfffff = pd.DataFrame(datafff, columns=['The Shawshank Redemption',
                                 'Forrest Gump', 'Avengers: Endgame',
                                 'Iron Man', 'Titanic '],
                  index=['user1', 'user2', 'user3', 'user4'])
# Compute correlation between user1 and other users
user_to_compare = dfffff.iloc[0]

#‘pearson’, ‘kendall’, ‘spearman’
similarity_with_other_users = dfffff.corrwith(user_to_compare, axis=1,
                                          method='pearson')



similarity_with_other_users = similarity_with_other_users.sort_values(
    ascending=False)
# Compute correlation between 'The Shawshank Redemption' and other movies
movie_to_compare = dfffff['The Shawshank Redemption']
similarity_with_other_movies = dfffff.corrwith(movie_to_compare, axis=0)
similarity_with_other_movies = similarity_with_other_movies.sort_values(
    ascending=False)



# In[1]:
data = [
{
    "state": "Florida",
    "shortname": "FL",
    "info": {"governor": "Rick Scott"},
    "counties": [
        {"name": "Dade", "population": 12345},
        {"name": "Broward", "population": 40000},
        {"name": "Palm Beach", "population": 60000},
    ],
},
{
    "state": "Ohio",
    "shortname": "OH",
    "info": {"governor": "John Kasich"},
    "counties": [
        {"name": "Summit", "population": 1234},
        {"name": "Cuyahoga", "population": 1337},
    ],
},
]
result = pd.json_normalize(
data, "counties", ["state", "shortname", ["info", "governor"]]
)

# In[1]

df = pd.DataFrame([[0, 2, 3], [0, 4, 1], [10, 20, 30]], columns=['A', 'B', 'C'])
print(df)
print(df.iat[1, 1])
print(df.at[1, 'B'])

print(df.axes)
print(df.ndim)


