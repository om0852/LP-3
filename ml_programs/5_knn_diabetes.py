"""
Assignment 5: K-Nearest Neighbors on diabetes.csv.
Computes confusion matrix, accuracy, error rate, precision and recall.

Dataset: diabetes.csv from https://www.kaggle.com/datasets/abdallamahgoub/diabetes
Run    : python 5_knn_diabetes.py [path/to/diabetes.csv]
"""
import sys

import numpy as np
import pandas as pd
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler

path = sys.argv[1] if len(sys.argv) > 1 else "diabetes.csv"

# ---------------------------------------------------------------- Read
df = pd.read_csv(path)
print("Shape:", df.shape)
print(df.head())

# A zero in these columns is not medically possible - it means "missing".
# Replace such zeros with the column median.
for col in ["Glucose", "BloodPressure", "SkinThickness", "Insulin", "BMI"]:
    if col in df.columns:
        df[col] = df[col].replace(0, np.nan)
        df[col] = df[col].fillna(df[col].median())

X = df.drop(columns=["Outcome"])
y = df["Outcome"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y)

# KNN is distance based, so features must be on the same scale.
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# ---------------------------------------------------------------- Choose k
print("\nAccuracy for different k:")
best_k, best_acc = 1, 0.0
for k in range(1, 22, 2):
    acc = KNeighborsClassifier(n_neighbors=k).fit(X_train, y_train).score(X_test, y_test)
    print(f"  k = {k:<3} accuracy = {acc:.4f}")
    if acc > best_acc:
        best_k, best_acc = k, acc

# ---------------------------------------------------------------- Final model
knn = KNeighborsClassifier(n_neighbors=best_k)
knn.fit(X_train, y_train)
pred = knn.predict(X_test)

cm = confusion_matrix(y_test, pred)
tn, fp, fn, tp = cm.ravel()

accuracy = (tp + tn) / (tp + tn + fp + fn)
error_rate = 1 - accuracy
precision = tp / (tp + fp) if (tp + fp) else 0.0
recall = tp / (tp + fn) if (tp + fn) else 0.0

print(f"\nKNN with k = {best_k}")
print("Confusion matrix (rows = actual, columns = predicted):")
print(cm)
print(f"TN = {tn}, FP = {fp}, FN = {fn}, TP = {tp}")
print(f"\nAccuracy   = {accuracy:.4f}")
print(f"Error rate = {error_rate:.4f}")
print(f"Precision  = {precision:.4f}")
print(f"Recall     = {recall:.4f}")
