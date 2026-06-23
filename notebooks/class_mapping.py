# notebooks/class_mapping.py

import pandas as pd

df = pd.read_csv("datasets/labels.csv", header=None)

classes = sorted(df[1].unique())

print("Class Mapping:\n")

for idx, cls in enumerate(classes):
    print(f"{idx}: {cls}")