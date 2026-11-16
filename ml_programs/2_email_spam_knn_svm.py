"""
Assignment 2: Email spam detection (binary classification) with
K-Nearest Neighbors and Support Vector Machine, and performance analysis.
    0 = Not Spam (normal state), 1 = Spam (abnormal state)

Dataset: emails.csv from
         https://www.kaggle.com/datasets/balaka18/email-spam-classification-dataset-csv
Run    : python 2_email_spam_knn_svm.py [path/to/emails.csv]
"""
import sys

import pandas as pd
from sklearn.metrics import (accuracy_score, classification_report, confusion_matrix,
                             f1_score, precision_score, recall_score)
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import MinMaxScaler
from sklearn.svm import SVC

path = sys.argv[1] if len(sys.argv) > 1 else "emails.csv"

# ---------------------------------------------------------------- Read
df = pd.read_csv(path)
print("Shape:", df.shape)
print("Missing values:", int(df.isnull().sum().sum()))

df = df.dropna()
X = df.drop(columns=["Email No.", "Prediction"], errors="ignore")   # word counts
y = df["Prediction"]
print("\nClass distribution (0 = Not Spam, 1 = Spam):")
print(y.value_counts())

# ---------------------------------------------------------------- Split + scale
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=42, stratify=y)

scaler = MinMaxScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# ---------------------------------------------------------------- Models
models = {
    "KNN (k=5)": KNeighborsClassifier(n_neighbors=5),
    "SVM (linear)": SVC(kernel="linear", C=1.0),
}

results = {}
for name, model in models.items():
    model.fit(X_train, y_train)
    pred = model.predict(X_test)
    results[name] = (
        accuracy_score(y_test, pred),
        precision_score(y_test, pred),
        recall_score(y_test, pred),
        f1_score(y_test, pred),
    )
    print(f"\n===== {name} =====")
    print("Confusion matrix (rows = actual, columns = predicted):")
    print(confusion_matrix(y_test, pred))
    print(classification_report(y_test, pred, target_names=["Not Spam", "Spam"]))

# ---------------------------------------------------------------- Compare
print(f"{'Model':<16}{'Accuracy':>10}{'Precision':>11}{'Recall':>9}{'F1':>8}")
print("-" * 54)
for name, (acc, prec, rec, f1) in results.items():
    print(f"{name:<16}{acc:>10.4f}{prec:>11.4f}{rec:>9.4f}{f1:>8.4f}")

best = max(results, key=lambda m: results[m][0])
print(f"\nBest accuracy on the test set: {best}")
