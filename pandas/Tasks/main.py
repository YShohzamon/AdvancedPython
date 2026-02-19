
import pandas as pd
import numpy as np
print(f"Pandas version: {pd.__version__}\nNumPy version: {np.__version__}")

df = pd.read_csv(r"Info\diabetes.csv")

print(df.to_string())

# Bazi ustunlardagi keraksiz 0 qiymatli qatorlar tozalandi.

cols = ["Glucose", "BloodPressure", "SkinThickness", "Insulin", "BMI"]
removed_df = df[(df[cols] == 0).any(axis=1)]
clean_df = df[(df[cols] != 0).all(axis=1)]

print(df.info())
print("---------------------")
print(removed_df.info())
print("---------------------")
print(clean_df.info())

print("Total rows:", 376 + 392)

print(clean_df.to_string())

print(removed_df.to_string())

interval_age1 = df[(df["Age"] > 25) & (df["Age"] < 35)]
interval_age2 = df[df["Age"].between(30, 55)]

print(interval_age1.to_string())
print("----------------------------------------------------------")
print(interval_age2.to_string())

removed_df.to_csv(r"Info\zero_rows.csv", index=False)
clean_df.to_csv(r"Info\clean_data.csv", index=False)