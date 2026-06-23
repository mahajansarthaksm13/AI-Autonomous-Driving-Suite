import pandas as pd

df = pd.read_csv("datasets/labels.csv", header=None)

print("Unique Image IDs:")
print(df[0].nunique())

print("\nMin Image ID:")
print(df[0].min())

print("\nMax Image ID:")
print(df[0].max())

print("\nSample IDs:")
print(df[0].head(20).tolist())