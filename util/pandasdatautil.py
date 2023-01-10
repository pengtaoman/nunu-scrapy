import pandas as pd

df = pd.read_json("../pageon.json")
# data = pd.read_json("../json/movie.json")
df.dtypes
df.set_index('', inplace=True)
print(type(df))
print(df.info(verbose=False, memory_usage='deep'))
print(df.columns)
