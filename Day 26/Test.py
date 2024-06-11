import pandas as pd
data = {"student": ["Angela", "James", "Lilly"], "score": [56, 76, 98]}
df = pd.DataFrame(data)
print(df, "\n")
for index, row in df.iterrows():
    print(row)