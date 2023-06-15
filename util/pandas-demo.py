#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 11 09:48:10 2023

@author: pt
"""
# In[2]:
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
# In[2]:
ratings_data = pd.read_csv("/Volumes/860EVO/work/json/ml-latest-small/ratings.csv")
ratings_data.head()

movie_names = pd.read_csv("/Volumes/860EVO/work/json/ml-latest-small/movies.csv")
movie_names.head() 


movie_data = pd.merge(ratings_data, movie_names, on='movieId')

# ms = movie_data.groupby('title')['rating'].mean().head()
ms = movie_data.groupby('title')['rating'].mean()
ms = ms.sort_values(ascending=False).head()
# In[2]:
'''
这些电影现已根据评分的降序排序。然而有一个问题是，如果只有一个用户对电影做了评价且分数为五星，这部电影就会排到列表的顶部。
因此，上述统计数据可能具有误导性。通常来讲，一部真正的好电影会有大批用户给更高的评分。
'''
crate = movie_data.groupby('title')['rating'].count().sort_values(ascending=False).head()

'''
现在你会看到真正的好电影就排在顶部了。以上列表证实了我们的观点，好电影通常会收到更高的评分。
现在我们知道每部电影的平均评分和评分数量都是重要的属性了。
让我们创建一个新的包含这些属性的 dataframe。
执行如下脚本创建 ratings_mean_count dataframe，首先将每部电影的平均评分添加到这个 dataframe：

'''
ratings_mean_count = pd.DataFrame(movie_data.groupby('title')['rating'].mean())

'''接下来，我们需要把电影的评分数添加到 ratings_mean_count dataframe。执行如下脚本来实现：
'''
ratings_mean_count['rating_counts'] = pd.DataFrame(movie_data.groupby('title')['rating'].count())



sns.set_style('dark')
# %matplotlib inline

plt.figure(figsize=(8,6))
plt.rcParams['patch.force_edgecolor'] = True
ratings_mean_count['rating_counts'].hist(bins=50)

'''从上图中，我们可以看到大部分电影的评分不到 50 条。而且有 100 条以上评分的电影数量非常少'''

'''现在我们绘制平均评分的直方图'''
plt.figure(figsize=(8,6))
plt.rcParams['patch.force_edgecolor'] = True
ratings_mean_count['rating'].hist(bins=50)


'''
您可以看到整数值的 bar 比浮点值更高，因为大多数用户会做出整数评分，即 1、2、3、4 或 5。此外，很明显，数据的正态分布较弱，平均值约为 3.5。数据中有一些异常值。

前面，我们说有更多评分数的电影通常也有高平均评分，因为一部好电影通常都是家喻户晓的，而很多人都会看这样的电影，因此通常会有更高的评分。
我们看看在我们的数据集中的电影是否也是这种情况。我们将平均评分与评分数量进行对比：

'''
plt.figure(figsize=(8,6))
plt.rcParams['patch.force_edgecolor'] = True
sns.jointplot(x='rating', y='rating_counts', data=ratings_mean_count, alpha=0.4)

'''该图表明，相较于低平均分的电影来说，高平均分的电影往往有更多的评分数量。'''


'''
我们在数据的可视化和预处理上花了较多时间。现在是时候找出电影之间的相似之处了。
我们将使用电影评分之间的相关性作为相似性度量。为了发现电影评分之间的相关性，我们需要创建一个矩阵，
其中每列是电影名称，每行包含特定用户为该电影指定的评分。请记住，此矩阵将具有大量空值，因为不是每个用户都会对每部电影进行评分。
创建电影标题和相应的用户评分矩阵，执行如下脚本

'''
user_movie_rating = movie_data.pivot_table(index='userId', columns='title', values='rating')

'''
我们知道每列包含所有用户对某部电影的评分。让我们找到电影 "Forrest Gump (1994)" 的所有用户评分，
然后找出跟它相似的电影。我们选这部电影是因为它评分数最多，我们希望找到具有更高评分数的电影之间的相关性。

'''
forrest_gump_ratings = user_movie_rating['Forrest Gump (1994)']

'''
现在让我们检索所有和 "Forrest Gump (1994)" 类似的电影。我们可以使用如下所示的 corrwith() 函数找到 "Forest Gump (1994)" 和所有其他电影的用户评分之间的相关性
'''
movies_like_forest_gump = user_movie_rating.corrwith(forrest_gump_ratings)

corr_forrest_gump = pd.DataFrame(movies_like_forest_gump, columns=['Correlation'])
corr_forrest_gump.dropna(inplace=True)
corr_forrest_gump.head()



# print(movie_data)

# df = pd.DataFrame({'Animal': ['Falcon', 'Falcon',
#                          'Parrot', 'Parrot'],
#                'Max Speed': [380., 370., 24., 26.]})
# df.groupby("Animal", group_keys=True).apply(lambda x: x) 


