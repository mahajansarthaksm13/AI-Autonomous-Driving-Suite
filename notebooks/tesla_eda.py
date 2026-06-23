# import pandas as pd

# df = pd.read_csv("datasets/Tesla - Deaths.csv")

# print("="*50)
# print("TESLA DATASET")
# print("="*50)

# print("\nShape:")
# print(df.shape)

# print("\nColumns:")
# print(df.columns.tolist())

# print("\nFirst 5 Rows:")
# print(df.head())

# print("\nMissing Values:")
# print(df.isnull().sum())

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("datasets/Tesla - Deaths.csv")

# Clean column names
df.columns = df.columns.str.strip()

# Remove rows with missing year
df = df.dropna(subset=["Year"])

# Convert year to integer
df["Year"] = df["Year"].astype(int)

# Count incidents per year
year_counts = df["Year"].value_counts().sort_index()

print(year_counts)

plt.figure(figsize=(12,6))
year_counts.plot(kind="bar")

plt.title("Tesla Fatal Incidents by Year")
plt.xlabel("Year")
plt.ylabel("Number of Incidents")

plt.tight_layout()
plt.savefig("reports/year_trend.png")
plt.close()

plt.figure(figsize=(12,6))

country_counts = (
    df["Country"]
    .astype(str)
    .str.strip()
    .value_counts()
    .head(10)
)

print("\nTop Countries:")
print(country_counts)

country_counts.plot(kind="bar")

plt.title("Top 10 Countries by Tesla Fatal Incidents")
plt.xlabel("Country")
plt.ylabel("Incidents")

plt.tight_layout()
plt.savefig("reports/country_analysis.png")
plt.close()
plt.figure(figsize=(12,6))

model_counts = (
    df["Model"]
    .astype(str)
    .str.strip()
    .value_counts()
)

print("\nTesla Models:")
print(model_counts)

model_counts.plot(kind="bar")

plt.title("Tesla Fatal Incidents by Model")
plt.xlabel("Tesla Model")
plt.ylabel("Incidents")

plt.tight_layout()

plt.savefig("reports/model_analysis.png")
plt.close()

# --------------------
# Autopilot Analysis
# --------------------

plt.figure(figsize=(10,6))

autopilot_counts = (
    df["Autopilot claimed"]
    .astype(str)
    .str.strip()
    .value_counts()
)

print("\nAutopilot Claims:")
print(autopilot_counts)

autopilot_counts.plot(kind="bar")

plt.title("Autopilot Claimed in Fatal Incidents")
plt.xlabel("Autopilot Claimed")
plt.ylabel("Incidents")

plt.tight_layout()

plt.savefig("reports/autopilot_analysis.png")
plt.close()

print("\n" + "="*50)
print("TESLA SAFETY DASHBOARD KPI")
print("="*50)

total_cases = len(df)

total_deaths = pd.to_numeric(
    df["Deaths"],
    errors="coerce"
).sum()

countries = df["Country"].nunique()

top_country = (
    df["Country"]
    .astype(str)
    .str.strip()
    .value_counts()
    .idxmax()
)

print(f"Total Cases      : {total_cases}")
print(f"Total Deaths     : {int(total_deaths)}")
print(f"Countries        : {countries}")
print(f"Top Country      : {top_country}")