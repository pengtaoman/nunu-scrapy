import pandas as pd

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