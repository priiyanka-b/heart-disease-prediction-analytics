import pandas as pd
import numpy as np
import pickle

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score


# -----------------------------
# 1. Load Dataset
# -----------------------------
df = pd.read_csv("dataset/cardio_train.csv", sep=";")

print("First 5 rows:")
print(df.head())


# -----------------------------
# 2. Data Cleaning
# -----------------------------

# Remove impossible blood pressure values
df = df[df["ap_hi"] > df["ap_lo"]]

# Remove extreme blood pressure values
df = df[(df["ap_hi"] > 70) & (df["ap_hi"] < 250)]
df = df[(df["ap_lo"] > 40) & (df["ap_lo"] < 200)]

# Convert age from days to years
df["age"] = (df["age"] / 365).astype(int)


# -----------------------------
# 3. Feature Engineering
# -----------------------------

# Create BMI
df["height_m"] = df["height"] / 100
df["bmi"] = df["weight"] / (df["height_m"] ** 2)


# -----------------------------
# 4. Prepare Features and Target
# -----------------------------

# Drop unnecessary columns
X = df.drop(columns=["cardio", "height_m", "id"])
y = df["cardio"]

print("\nFeatures used for training:")
print(X.columns)


# -----------------------------
# 5. Train-Test Split
# -----------------------------

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

print("\nTraining samples:", len(X_train))
print("Testing samples:", len(X_test))


# -----------------------------
# 6. Train Model
# -----------------------------

model = LogisticRegression(max_iter=1000)

model.fit(X_train, y_train)

print("\nModel training completed.")


# -----------------------------
# 7. Predictions
# -----------------------------

y_pred = model.predict(X_test)


# -----------------------------
# 8. Evaluate Model
# -----------------------------

accuracy = accuracy_score(y_test, y_pred)

print("\nModel Accuracy:", accuracy)


# -----------------------------
# 9. Save Model
# -----------------------------

pickle.dump(model, open("heart_disease_model.pkl", "wb"))

print("\nModel saved as heart_disease_model.pkl")