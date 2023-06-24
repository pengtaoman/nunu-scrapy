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