import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# df = pd.read_json("../pageon.json")
df = pd.read_json("../json/movie.json")
df.dtypes
# df.set_index('', inplace=True)
print(type(df))
print(df.info(verbose=False, memory_usage='deep'))
cols = df.columns
inx = df.index

# df.loc[:, "year"] = df["year"].str.replace("(", "").astype('str')
# df.loc[:, "year"] = df["year"].str.replace(")", "").astype('int32')

# df.loc[lambda df : (df["name"]<=30) & (df["yWendu"]>=15), :]
filterdf = df[df.name.str.contains('霸王')]

data = [[50, True], [40, False], [30, False]]
label_rows = ["Sally", "Mary", "John"]
label_cols = ["age", "qualified"]

dataf = pd.DataFrame(data, label_rows, label_cols)
print('#'*20)
print(dataf.loc["Mary", "age"])

ts = pd.Series(np.random.randn(1000), index=pd.date_range('1/1/2000', periods=1000))
ts = ts.cumsum()
ts.plot()