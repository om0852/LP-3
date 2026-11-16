"""
Assignment 1: Predict the price of an Uber ride.
  1. Pre-process the dataset      2. Identify outliers
  3. Check the correlation        4. Linear regression + random forest
  5. Evaluate and compare (R2, RMSE, MAE)

Dataset: uber.csv from https://www.kaggle.com/datasets/yasserh/uber-fares-dataset
Run    : python 1_uber_fare_prediction.py [path/to/uber.csv]
"""
import sys

import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

try:
    import matplotlib.pyplot as plt
except ImportError:          # plots are optional
    plt = None

path = sys.argv[1] if len(sys.argv) > 1 else "uber.csv"


def haversine_km(lat1, lon1, lat2, lon2):
    """Great-circle distance between two points in kilometres."""
    lat1, lon1, lat2, lon2 = map(np.radians, [lat1, lon1, lat2, lon2])
    a = (np.sin((lat2 - lat1) / 2) ** 2
         + np.cos(lat1) * np.cos(lat2) * np.sin((lon2 - lon1) / 2) ** 2)
    return 6371 * 2 * np.arcsin(np.sqrt(a))


# ---------------------------------------------------------------- 1. Pre-process
df = pd.read_csv(path)
print("Shape:", df.shape)
print(df.head())
print("\nMissing values:\n", df.isnull().sum())

df = df.drop(columns=[c for c in ("Unnamed: 0", "key") if c in df.columns])
df = df.dropna()

# Date-time features
df["pickup_datetime"] = pd.to_datetime(df["pickup_datetime"], errors="coerce", utc=True)
df = df.dropna(subset=["pickup_datetime"])
df["hour"] = df["pickup_datetime"].dt.hour
df["day"] = df["pickup_datetime"].dt.day
df["month"] = df["pickup_datetime"].dt.month
df["year"] = df["pickup_datetime"].dt.year
df["weekday"] = df["pickup_datetime"].dt.dayofweek
df = df.drop(columns=["pickup_datetime"])

# Remove impossible values
df = df[df["pickup_latitude"].between(-90, 90) & df["dropoff_latitude"].between(-90, 90)
        & df["pickup_longitude"].between(-180, 180) & df["dropoff_longitude"].between(-180, 180)]
df = df[(df["fare_amount"] > 0) & df["passenger_count"].between(1, 6)]

# Trip distance from the pickup and drop-off points
df["distance_km"] = haversine_km(df["pickup_latitude"], df["pickup_longitude"],
                                 df["dropoff_latitude"], df["dropoff_longitude"])
df = df[df["distance_km"] > 0]
print("\nShape after cleaning:", df.shape)

# ---------------------------------------------------------------- 2. Outliers
print("\nOutliers (IQR method: outside Q1 - 1.5*IQR .. Q3 + 1.5*IQR)")
bounds = {}
for col in ["fare_amount", "distance_km"]:
    q1, q3 = df[col].quantile([0.25, 0.75])
    iqr = q3 - q1
    low, high = q1 - 1.5 * iqr, q3 + 1.5 * iqr
    bounds[col] = (low, high)
    n_out = ((df[col] < low) | (df[col] > high)).sum()
    print(f"  {col:<12} range [{low:.2f}, {high:.2f}]  outliers: {n_out}")

if plt:
    df[["fare_amount", "distance_km"]].plot(kind="box", subplots=True, figsize=(8, 4))
    plt.suptitle("Before removing outliers")
    plt.savefig("uber_boxplot.png")
    plt.close("all")

for col, (low, high) in bounds.items():
    df = df[df[col].between(low, high)]
print("Shape after removing outliers:", df.shape)

# ---------------------------------------------------------------- 3. Correlation
corr = df.corr()
print("\nCorrelation with fare_amount:")
print(corr["fare_amount"].sort_values(ascending=False).round(3))

if plt:
    plt.figure(figsize=(9, 7))
    plt.imshow(corr, cmap="coolwarm", vmin=-1, vmax=1)
    plt.colorbar()
    plt.xticks(range(len(corr)), corr.columns, rotation=90)
    plt.yticks(range(len(corr)), corr.columns)
    plt.title("Correlation matrix")
    plt.tight_layout()
    plt.savefig("uber_correlation.png")
    plt.close("all")

# ---------------------------------------------------------------- 4. Models
X = df.drop(columns=["fare_amount"])
y = df["fare_amount"]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

scaler = StandardScaler()
X_train_s = scaler.fit_transform(X_train)
X_test_s = scaler.transform(X_test)

models = {
    "Linear Regression": LinearRegression(),
    "Random Forest": RandomForestRegressor(n_estimators=100, random_state=42, n_jobs=-1),
}

# ---------------------------------------------------------------- 5. Evaluate
print(f"\n{'Model':<20}{'R2':>8}{'RMSE':>10}{'MAE':>10}")
print("-" * 48)
for name, model in models.items():
    model.fit(X_train_s, y_train)
    pred = model.predict(X_test_s)
    r2 = r2_score(y_test, pred)
    rmse = np.sqrt(mean_squared_error(y_test, pred))
    mae = mean_absolute_error(y_test, pred)
    print(f"{name:<20}{r2:>8.4f}{rmse:>10.4f}{mae:>10.4f}")

print("\nHigher R2 and lower RMSE/MAE mean a better model.")
