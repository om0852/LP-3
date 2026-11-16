"""
Assignment 6: K-Means clustering on sales_data_sample.csv.
The number of clusters is determined with the elbow method.

Dataset: sales_data_sample.csv from
         https://www.kaggle.com/datasets/kyanyoga/sample-sales-data
Run    : python 6_kmeans_sales.py [path/to/sales_data_sample.csv]
"""
import sys

import numpy as np
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

try:
    import matplotlib.pyplot as plt
except ImportError:          # the plot is optional
    plt = None

path = sys.argv[1] if len(sys.argv) > 1 else "sales_data_sample.csv"

# ---------------------------------------------------------------- Read
df = pd.read_csv(path, encoding="latin1")      # the file is not UTF-8
print("Shape:", df.shape)

features = ["QUANTITYORDERED", "PRICEEACH", "SALES", "MSRP"]
data = df[features].dropna()
print(data.describe().round(2))

X = StandardScaler().fit_transform(data)

# ---------------------------------------------------------------- Elbow method
# WCSS = within-cluster sum of squares (KMeans.inertia_)
ks = list(range(1, 11))
wcss = []
for k in ks:
    km = KMeans(n_clusters=k, n_init=10, random_state=42).fit(X)
    wcss.append(km.inertia_)

print("\nElbow method")
print(f"{'k':<4}{'WCSS':>12}")
for k, w in zip(ks, wcss):
    print(f"{k:<4}{w:>12.2f}")

# The elbow is the point farthest from the straight line joining the
# first and last points of the WCSS curve.
p1 = np.array([ks[0], wcss[0]])
p2 = np.array([ks[-1], wcss[-1]])
line = p2 - p1
distances = [abs(line[0] * (p1[1] - w) - (p1[0] - k) * line[1]) / np.hypot(*line)
             for k, w in zip(ks, wcss)]
best_k = ks[int(np.argmax(distances))]
print(f"\nElbow found at k = {best_k}")

if plt:
    plt.plot(ks, wcss, "bo-")
    plt.axvline(best_k, color="red", linestyle="--", label=f"elbow (k = {best_k})")
    plt.xlabel("Number of clusters (k)")
    plt.ylabel("WCSS")
    plt.title("Elbow method")
    plt.legend()
    plt.savefig("elbow_plot.png")
    plt.close("all")

# ---------------------------------------------------------------- Final clustering
kmeans = KMeans(n_clusters=best_k, n_init=10, random_state=42)
data = data.assign(Cluster=kmeans.fit_predict(X))

print("\nCluster sizes:")
print(data["Cluster"].value_counts().sort_index())
print("\nCluster averages:")
print(data.groupby("Cluster")[features].mean().round(2))

if plt:
    plt.scatter(data["QUANTITYORDERED"], data["SALES"], c=data["Cluster"], cmap="viridis", s=10)
    plt.xlabel("QUANTITYORDERED")
    plt.ylabel("SALES")
    plt.title(f"K-Means clusters (k = {best_k})")
    plt.savefig("sales_clusters.png")
