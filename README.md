# 🤖 AI Predictive Maintenance Platform

> **Predict. Explain. Prevent.**

An end-to-end **AI-powered Predictive Maintenance Platform** developed using **Python, XGBoost, Streamlit, SHAP Explainable AI, and Microsoft SQL Server**. The application predicts industrial machine failures, provides explainable AI insights, stores prediction history in a database, and generates downloadable PDF reports.

---

# 📌 Overview

The AI Predictive Maintenance Platform helps maintenance engineers predict potential machine failures before they occur.

The application combines:

- Machine Learning
- Explainable AI
- Database Management
- Interactive Dashboards
- Automated Reporting

into a single industrial web application.

---

# 🚀 Key Features

## 🤖 Machine Failure Prediction

Predict machine health using an XGBoost Machine Learning model.

Input Parameters:

- Machine Type
- Air Temperature
- Process Temperature
- Rotational Speed
- Torque
- Tool Wear

Output:

- Healthy / Failure
- Prediction Confidence
- Engineering Interpretation

---

## 🧠 Explainable AI (SHAP)

Every prediction includes AI explainability using SHAP.

The system explains which operating parameters influenced the prediction.

Examples:

- Tool Wear
- Torque
- Temperature Difference
- Rotational Speed

---

## 📊 Interactive Dashboard

Visualize prediction history using SQL Server data.

Dashboard includes:

- Total Predictions
- Healthy Machines
- Failure Predictions
- Machine Type Distribution
- Prediction History

---

## 📈 Analytics

Interactive analytics page with:

- Failure Distribution
- Machine Type Analysis
- Confidence Analysis
- Historical Prediction Trends

---

## 💾 SQL Server Integration

Predictions are automatically stored inside Microsoft SQL Server.

Database Features:

- Prediction History
- Database Monitor
- Export Records
- Real-time Retrieval

---

## 📄 Automated PDF Report

Generate professional prediction reports containing:

- Machine Information
- Prediction Result
- Confidence Score
- Engineering Recommendation
- Explainable AI Summary

---

## 🎨 Professional User Interface

Modern multi-page Streamlit application including:

- Home
- Prediction
- Dashboard
- Database Monitor
- Analytics
- About

---

# 🏗 Project Architecture

```
                 User

                  │

                  ▼

        Streamlit Web Application

                  │

        ┌─────────┴─────────┐

        ▼                   ▼

 Machine Learning       SQL Server

   XGBoost Model      PredictionHistory

        │                   │

        └─────────┬─────────┘

                  ▼

          Dashboard & Analytics

                  │

                  ▼

            PDF Report Generator
```

---

# 🧠 Machine Learning Model

Algorithm:

**XGBoost Classifier**

Feature Engineering:

- Temperature Difference
- One-Hot Encoding
- Data Standardization

Prediction Output:

- Healthy
- Failure

---

# 🛠 Technology Stack

| Category | Technology |
|-----------|------------|
| Programming | Python |
| Web Framework | Streamlit |
| Machine Learning | XGBoost |
| Explainable AI | SHAP |
| Database | Microsoft SQL Server |
| Data Analysis | Pandas |
| Visualization | Plotly |
| Reporting | ReportLab |
| Version Control | Git & GitHub |

---

# 📂 Project Structure

```
AI-Predictive-Maintenance-System

│

├── app.py

├── database.py

├── pdf_report.py

├── styles.py

├── requirements.txt

├── README.md

│

├── model

│   └── xgboost_predictive_maintenance.pkl

│

├── pages

│   ├── 1_Home.py

│   ├── 2_Prediction.py

│   ├── 3_Dashboard.py

│   ├── 4_Database.py

│   ├── 5_Analytics.py

│   └── 6_About.py

│

├── assets

│

└── screenshots
```

---

# ⚙ Installation

Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/AI-Predictive-Maintenance-System.git
```

Move into the project

```bash
cd AI-Predictive-Maintenance-System
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the application

```bash
streamlit run app.py
```

---

# 🗄 SQL Server Setup

Create a SQL Server database named:

```
PredictiveMaintenanceDB
```

Create the table:

```
PredictionHistory
```

Update your SQL Server connection inside

```
database.py
```

---

# 📊 Application Workflow

```
User Input

↓

Feature Engineering

↓

XGBoost Prediction

↓

Prediction Confidence

↓

SHAP Explainability

↓

Engineering Recommendation

↓

Store in SQL Server

↓

Dashboard Update

↓

Generate PDF Report
```

---

# 📸 Screenshots

## Home

(Add Screenshot)

---

## Prediction

(Add Screenshot)

---

## Dashboard

(Add Screenshot)

---

## Database Monitor

(Add Screenshot)

---

## Analytics

(Add Screenshot)

---

## About

(Add Screenshot)

---

# 🔮 Future Improvements

- Batch Prediction using CSV
- Remaining Useful Life (RUL) Estimation
- Cloud Database Integration
- Azure Deployment
- Docker Support
- User Authentication
- Maintenance Scheduling
- Email Notifications
- REST API Integration

---

# 👨‍💻 Developer

**Raj Patil**

Petrochemical Engineer

Machine Learning Enthusiast

Python Developer

---

# 📜 License

This project is licensed under the MIT License.

---

# ⭐ Acknowledgements

This project was developed as a portfolio project demonstrating:

- Machine Learning
- Explainable AI
- Predictive Maintenance
- SQL Server Integration
- Industrial Analytics
- Streamlit Web Application Development

---

## 🚀 Version

**AI Predictive Maintenance Platform**

**Version 1.0**

**Predict. Explain. Prevent.**
