import pandas as pd
import mysql.connector

# -----------------------------------
# 1. Load CSV
# -----------------------------------

df = pd.read_csv("cardio_predictions.csv")

print("Dataset loaded:", len(df))


# -----------------------------------
# 2. Connect to MySQL
# -----------------------------------

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="ADMIn@2312..",
    database="heart_disease_analytics"
)

cursor = conn.cursor()

print("Connected to MySQL")


# -----------------------------------
# 3. Insert Patients
# -----------------------------------

for _, row in df.iterrows():
    
    patient_query = """
    INSERT INTO patients (patient_id, age, gender, height, weight)
    VALUES (%s, %s, %s, %s, %s)
    """
    
    cursor.execute(patient_query, (
        int(row["id"]),
        int(row["age"]),
        int(row["gender"]),
        int(row["height"]),
        float(row["weight"])
    ))

conn.commit()

print("Patients inserted.")


# -----------------------------------
# 4. Insert Health Metrics
# -----------------------------------

for _, row in df.iterrows():

    metrics_query = """
    INSERT INTO health_metrics
    (patient_id, systolic_bp, diastolic_bp, cholesterol, glucose, smoke, alcohol, active, bmi)
    VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)
    """

    cursor.execute(metrics_query, (
        int(row["id"]),
        int(row["ap_hi"]),
        int(row["ap_lo"]),
        int(row["cholesterol"]),
        int(row["gluc"]),
        int(row["smoke"]),
        int(row["alco"]),
        int(row["active"]),
        float(row["bmi"])
    ))

conn.commit()

print("Health metrics inserted.")


# -----------------------------------
# 5. Insert Predictions
# -----------------------------------

for _, row in df.iterrows():

    pred_query = """
    INSERT INTO predictions (patient_id, predicted_risk)
    VALUES (%s, %s)
    """

    cursor.execute(pred_query, (
        int(row["id"]),
        int(row["predicted_risk"])
    ))

conn.commit()

print("Predictions inserted.")


# -----------------------------------
# 6. Close connection
# -----------------------------------

cursor.close()
conn.close()

print("Data successfully loaded into MySQL!")