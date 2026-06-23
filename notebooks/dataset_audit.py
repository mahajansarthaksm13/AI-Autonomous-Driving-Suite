import pandas as pd

print("=" * 50)
print("LABELS DATASET")
print("=" * 50)

labels = pd.read_csv("datasets/labels.csv")

print("\nShape:")
print(labels.shape)

print("\nColumns:")
print(labels.columns.tolist())

print("\nFirst 5 rows:")
print(labels.head())

print("\nMissing Values:")
print(labels.isnull().sum())

print("\n\n")

print("=" * 50)
print("TESLA DATASET")
print("=" * 50)

tesla = pd.read_csv("datasets/Tesla - Deaths.csv")

print("\nShape:")
print(tesla.shape)

print("\nColumns:")
print(tesla.columns.tolist())

print("\nFirst 5 rows:")
print(tesla.head())

print("\nMissing Values:")
print(tesla.isnull().sum())