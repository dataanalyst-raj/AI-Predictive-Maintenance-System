# 🤖 AI Predictive Maintenance Platform

> **Predict. Explain. Prevent.**

### 🔗 [**Live Demo — Try the App**](https://ai-predictive-maintenance-system-yhykkkw5bemvhxqwttfzyj.streamlit.app/)

An end-to-end **AI-powered Predictive Maintenance Platform** built with **Python, XGBoost, Streamlit, SHAP Explainable AI, and SQL**. The application predicts industrial machine failures, explains every prediction with SHAP, stores prediction history in a database, and generates downloadable PDF reports.

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

The system explains which operating parameters influenced the prediction — for example Tool Wear, Torque, Temperature Difference, and Rotational Speed — so an engineer can see *why* a machine was flagged, not just that it was.

---

## 📊 Interactive Dashboard

Visualize prediction history directly from the database:

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

## 💾 Hybrid Database Layer (SQL Server → SQLite Failover)

Predictions are stored automatically using a **multi-backend database layer with automatic failover** — a real production pattern:

- **Local / office deployment:** connects to **Microsoft SQL Server** (`PredictiveMaintenanceDB`)
- **Cloud deployment (Streamlit Cloud):** automatically falls back to **SQLite** — no configuration needed
- Identical interface for both backends: the application code never changes

Database features:

- Prediction History
- Database Monitor
- Export Records
- Real-time Retrieval

> Note: on the free Streamlit Cloud demo, SQLite storage is temporary and resets when the app restarts.

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

Modern multi-page Streamlit application with a shared, centralized CSS design system:

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
 Machine Learning     Database Layer
   XGBoost Model     SQL Server ──► SQLite
        │             (auto-failover)
        └─────────┬─────────┘
                  ▼
          Dashboard & Analytics
                  │
                  ▼
            PDF Report Generator
```

---

# 🧠 Machine Learning Model

Algorithm: **XGBoost Classifier**

Trained on the **AI4I 2020 Predictive Maintenance Dataset** (10,000 sensor readings, 3.39% failure rate — a realistic imbalanced-class industrial problem).

Feature Engineering:

- Temperature Difference (heat-dissipation physics)
- One-Hot Encoding of machine quality type
- Data Standardization

Prediction Output:

- Healthy / Failure with confidence score
- SHAP feature contributions per prediction

---

# 🛠 Technology Stack

| Category | Technology |
|-----------|------------|
| Programming | Python |
| Web Framework | Streamlit |
| Machine Learning | XGBoost |
| Explainable AI | SHAP |
| Database | Microsoft SQL Server + SQLite (failover) |
| Data Analysis | Pandas |
| Visualization | Plotly |
| Reporting | ReportLab |
| Version Control | Git & GitHub |

---

# 📂 Project Structure

```
ai-predictive-maintenance-system
│
├── app.py
├── database.py
├── pdf_report.py
├── requirements.txt
├── README.md
├── xgboost_predictive_maintenance.pkl
│
└── pages
    ├── 1_Home.py
    ├── 2_Prediction.py
    ├── 3_Dashboard.py
    ├── 4_Database.py
    ├── 5_Analytics.py
    └── 6_About.py
```

---

# ⚙ Installation

Clone the repository

```bash
git clone https://github.com/dataanalyst-raj/ai-predictive-maintenance-system.git
```

Move into the project

```bash
cd ai-predictive-maintenance-system
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the application

```bash
streamlit run app.py
```

The app runs immediately using SQLite — no database setup required.

---

# 🗄 Optional: SQL Server Setup

To use Microsoft SQL Server instead of SQLite:

1. Create a database named `PredictiveMaintenanceDB`
2. Create the `PredictionHistory` table
3. Update the connection string inside `database.py`

If SQL Server is unreachable, the application automatically falls back to SQLite.

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
Store in Database (SQL Server / SQLite)
   ↓
Dashboard Update
   ↓
Generate PDF Report
```

---

# 📸 Screenshots

## Prediction

(Add Screenshot)

## Dashboard

(Add Screenshot)

## Analytics

(Add Screenshot)

---

# 🔮 Future Improvements

- Batch Prediction using CSV
- Remaining Useful Life (RUL) Estimation
- Cloud Database Integration (Supabase / Neon Postgres)
- Docker Support
- User Authentication
- Maintenance Scheduling
- Email Notifications
- REST API Integration

---

# 👨‍💻 Developer

**Raj Patil**

Process Development Engineer · Machine Learning Enthusiast · Python Developer

---

# 📜 License

This project is licensed under the MIT License.

---

# ⭐ Acknowledgements

This project was developed as a portfolio project demonstrating:

- Machine Learning
- Explainable AI
- Predictive Maintenance
- SQL Database Integration with Failover
- Industrial Analytics
- Streamlit Web Application Development

---

## 🚀 Version

**AI Predictive Maintenance Platform**

**Version 1.1**

**Predict. Explain. Prevent.**
