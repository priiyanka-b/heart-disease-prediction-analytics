# 🫀 Heart Disease Prediction & Analytics

An end-to-end data project combining machine learning prediction with SQL-based analytics and a live deployed web app. Predicts the likelihood of heart disease from clinical features, stores results in MySQL, and surfaces insights through a web interface.



---

## 🔍 Problem Statement

Heart disease is the leading cause of death globally. Early risk detection using patient data can significantly improve outcomes. This project builds a classification model on clinical indicators and wraps it in a full analytics pipeline — from raw data to deployed predictions stored in a database.

---

## 🗂 Project Structure

```
heart-disease-prediction-analytics/
├── dataset/                    # Raw heart disease dataset
├── eda/                        # Exploratory data analysis
├── app.py                      # Flask web application
├── predict_and_export.py       # Batch prediction script, exports to CSV
├── load_to_mysql.py            # Loads prediction results into MySQL
├── cardio_predictions.csv      # Exported prediction results
├── static/                     # CSS and static assets
├── templates/                  # HTML templates
├── .gitignore
└── README.md
```

---

## ⚙️ How It Works

1. **EDA** — Explored clinical features (age, cholesterol, blood pressure, etc.) to understand distributions and correlations
2. **Model Training** — Classification model trained on heart disease dataset
3. **Batch Prediction** — `predict_and_export.py` runs predictions and exports results to CSV
4. **MySQL Integration** — `load_to_mysql.py` loads prediction results into a relational database for analytics queries
5. **Web App** — Flask app deployed on Vercel serves live predictions from user inputs

---

## 🛠 Tech Stack

- **Python** — pandas, scikit-learn, Flask
- **Database** — MySQL
- **Frontend** — HTML/CSS (Flask templates)
- **Deployment** — Vercel

---

## 🚀 Run Locally

```bash
# Install dependencies
pip install -r requirements.txt

# Run batch predictions
python predict_and_export.py

# Load predictions to MySQL (update DB credentials in script)
python load_to_mysql.py

# Start the web app
python app.py
```

Then open `http://localhost:5000` in your browser.

---

## 📊 What Makes This Different

Most ML projects stop at the notebook. This one goes further:
- Predictions are **exported to CSV** for reporting
- Results are **loaded into MySQL** for structured querying
- A **live web app** lets users get predictions in real time
- Deployed publicly on **Vercel**

---

## 📌 Key Learnings

- Bridging ML output with a database pipeline (not just a notebook)
- Importance of separating prediction logic from the web app layer
- Deploying a Flask ML app to a production environment

---

## 🔗 Connect

**LinkedIn:** [Priyanka Bharwani](https://www.linkedin.com/in/priyanka-bharwani-4988322b9)
