import shap
import joblib

model = joblib.load("xgboost_predictive_maintenance.pkl")

explainer = shap.TreeExplainer(model)

print("✅ SHAP is working successfully!")
