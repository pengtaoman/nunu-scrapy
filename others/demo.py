# -*- coding: utf-8 -*-

import pandas as pd

# 创建示例 DataFrame
data = {'Name': ['Alice', 'Bob', 'Charlie', 'David'],
        'Fruits': [['apple', 'banana'], ['orange', 'grape'], ['pear', 'kiwi'], ['melon', 'banana']]}
df = pd.DataFrame(data)

# 判断 Fruits 列是否包含特定字符串
search_string = 'banana'
df['Contains_String'] = df['Fruits'].apply(lambda x: search_string in x)
df = df[df['Contains_String'] == True]
print(df)



#实现推荐功能
#根据用户输入的电影分类、国家、评分、导演、主演等信息，使用构建好的推荐算法进行推荐，输出推荐结果。

#下面是一个基于内容的推荐算法的Python代码示例：

#python
#Copy code
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# 读取电影数据
movies_df = pd.read_csv('movies.csv')

# 处理电影数据
movies_df = movies_df.drop_duplicates()
movies_df = movies_df.dropna()
movies_df['genres'] = movies_df['genres'].apply(lambda x: ' '.join(x.split('|')))
movies_df['directors'] = movies_df['directors'].apply(lambda x: ' '.join(x.split('|')))
movies_df['actors'] = movies_df['actors'].apply(lambda x: ' '.join(x.split('|')))

# 编码电影数据
tfidf = TfidfVectorizer(stop_words='english')
movies_df['genres_vector'] = list(tfidf.fit_transform(movies_df['genres']).toarray())
movies_df['directors_vector'] = list(tfidf.fit_transform(movies_df['directors']).toarray())
movies_df['actors_vector'] = list(tfidf.fit_transform(movies_df['actors']).toarray())

# 定义推荐函数
def get_recommendations(genres, country, rating, directors, actors):
    # 过滤电影数据
    filtered_movies = movies_df[(movies_df['genres'].str.contains(genres)) &
                                (movies_df['country'] == country) &
                                (movies_df['rating'] >= rating) &
                                (movies_df['directors'].str.contains(directors)) &
                                (movies_df['actors'].str.contains(actors))]
    # 计算电影相似度
    genres_similarity = cosine_similarity(list(filtered_movies['genres_vector']))
    directors_similarity = cosine_similarity(list(filtered_movies['directors_vector']))
    actors_similarity = cosine_similarity(list(filtered_movies['actors_vector']))
    similarity_matrix = genres_similarity + directors_similarity + actors_similarity
    # 获取电影推荐结果
    indices = pd.Series(filtered_movies.index)
    recommended_movies = []
    for i in range(len(indices)):
        similar_movies = list