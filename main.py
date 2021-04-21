import pandas as pd

df = pd.read_json("tweets_json_bbb21.txt")
id = df['id'].unique()
print(df.shape)
print(len(id))