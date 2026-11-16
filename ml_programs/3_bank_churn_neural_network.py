"""
Assignment 3: Neural-network classifier that predicts whether a bank
customer will leave (Exited = 1) or stay (Exited = 0).
  1. Read the dataset
  2. Separate features/target, split into train and test sets
  3. Normalize the train and test data
  4. Build the model, identify points of improvement and implement them
  5. Print the accuracy score and confusion matrix

Dataset: Churn_Modelling.csv from
         https://www.kaggle.com/barelydedicated/bank-customer-churn-modeling
Run    : python 3_bank_churn_neural_network.py [path/to/Churn_Modelling.csv]

Uses scikit-learn's MLPClassifier (a feed-forward neural network), so no
TensorFlow installation is needed.
"""
import sys

import pandas as pd
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier
from sklearn.preprocessing import StandardScaler

path = sys.argv[1] if len(sys.argv) > 1 else "Churn_Modelling.csv"

# ---------------------------------------------------------------- 1. Read
df = pd.read_csv(path)
print("Shape:", df.shape)
print(df.head())

# ---------------------------------------------------------------- 2. Features / target
# RowNumber, CustomerId and Surname identify the customer but do not
# influence churn, so they are dropped.
X = df.drop(columns=["RowNumber", "CustomerId", "Surname", "Exited"], errors="ignore")
y = df["Exited"]
X = pd.get_dummies(X, columns=["Geography", "Gender"], drop_first=True)
print("\nFeatures:", list(X.columns))
print("Target distribution:\n", y.value_counts())

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y)

# ---------------------------------------------------------------- 3. Normalize
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)     # fit only on training data
X_test = scaler.transform(X_test)


def evaluate(name, model):
    pred = model.predict(X_test)
    acc = accuracy_score(y_test, pred)
    print(f"\n===== {name} =====")
    print(f"Accuracy score: {acc:.4f}")
    print("Confusion matrix (rows = actual, columns = predicted):")
    print(confusion_matrix(y_test, pred))
    print(classification_report(y_test, pred, target_names=["Stayed", "Left"]))
    return acc


# ---------------------------------------------------------------- 4. Build the model
# Baseline: one small hidden layer.
baseline = MLPClassifier(hidden_layer_sizes=(6,), activation="relu", solver="adam",
                         max_iter=200, random_state=42)
baseline.fit(X_train, y_train)
acc_base = evaluate("Baseline network: 1 hidden layer (6 neurons)", baseline)

# Points of improvement:
#   - more capacity: two larger hidden layers (32, 16)
#   - L2 regularization (alpha) to reduce over-fitting
#   - early stopping on a validation split, with more iterations allowed
#   - smaller mini-batches for more frequent weight updates
improved = MLPClassifier(hidden_layer_sizes=(32, 16), activation="relu", solver="adam",
                         alpha=0.001, batch_size=32, learning_rate_init=0.001,
                         max_iter=500, early_stopping=True, validation_fraction=0.1,
                         n_iter_no_change=15, random_state=42)
improved.fit(X_train, y_train)
acc_imp = evaluate("Improved network: 2 hidden layers (32, 16) + early stopping", improved)

# ---------------------------------------------------------------- 5. Summary
print(f"Baseline accuracy : {acc_base:.4f}")
print(f"Improved accuracy : {acc_imp:.4f}")
