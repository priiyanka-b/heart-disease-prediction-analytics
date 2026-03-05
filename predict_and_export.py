import pandas as pd
import pickle

# -----------------------------------
# 1. Load dataset
# -----------------------------------

df = pd.read_csv("dataset/cardio_train.csv", sep=";")

print("Dataset loaded.")
print("Total records:", len(df))


# -----------------------------------
# 2. Load trained model
# -----------------------------------

model = pickle.load(open("heart_disease_model.pkl", "rb"))

print("Model loaded successfully.")


# -----------------------------------
# 3. Feature engineering (same as training)
# -----------------------------------

# convert age from days to years
df["age"] = (df["age"] / 365).astype(int)

# create BMI
df["height_m"] = df["height"] / 100
df["bmi"] = df["weight"] / (df["height_m"] ** 2)


# -----------------------------------
# 4. Prepare features for prediction
# -----------------------------------

X = df.drop(columns=["cardio", "height_m", "id"])


# -----------------------------------
# 5. Generate predictions
# -----------------------------------

df["predicted_risk"] = model.predict(X)

print("\nPrediction sample:")
print(df[["age","ap_hi","ap_lo","cholesterol","predicted_risk"]].head())


# -----------------------------------
# 6. Save dataset with predictions
# -----------------------------------

df.to_csv("cardio_predictions.csv", index=False)

print("\nPredictions exported successfully!")
print("File created: cardio_predictions.csv")