import pandas as pd

df = pd.read_csv("datasets/labels.csv", header=None)

print(df.head(10))
print("\nShape:", df.shape)