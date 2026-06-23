import pandas as pd

df = pd.read_csv("datasets/labels.csv", header=None)

df.columns = [
    "image_id",
    "vehicle_class",
    "xmin",
    "ymin",
    "xmax",
    "ymax"
]

print("\nTotal Annotations:")
print(len(df))

print("\nUnique Vehicle Classes:")
print(df["vehicle_class"].nunique())

print("\nVehicle Classes:")
print(sorted(df["vehicle_class"].unique()))

print("\nTop 20 Classes:")
print(df["vehicle_class"].value_counts().head(20))