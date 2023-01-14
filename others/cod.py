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


df = pd.read_json('../json/movie.json')
print(df.axes)
df['moviename']=df['name']
# list lll = df['category'].to_list()

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

# In[1]:
    
    
#使用stack行转列
df_category_temp=df_category_temp.stack()

# In[1]:
    

 

    
df_category_temp = df_category_temp.reset_index(level=1, drop=True)
df_category_temp
df_category_temp.name='category'
df_new = df.drop(['category'], axis=1).join(df_category_temp)
df_new

# In[1]:

print(sys.getsizeof(df_new))
df_new.drop(columns=['summary'])
print(sys.getsizeof(df_new))

# In[1]:
    
df_category_merge = pd.merge(df_new, df_category, how='left', on=['category'])
df_category_merge

# In[1]:
    
print(sys.getsizeof(df_category_merge))







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


