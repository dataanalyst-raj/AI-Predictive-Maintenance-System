import shap
import joblib
import pandas as pd

# Load model
model = joblib.load("xgboost_predictive_maintenance.pkl")

explainer = shap.TreeExplainer(model)

sample = pd.DataFrame([[
    300,
    310,
    1500,
    40,
    10,
    10,
    1,
    0
]], columns=[
    "Air_temperature_K",
    "Process_temperature_K",
    "Rotational_speed_rpm",
    "Torque_Nm",
    "Tool_wear_min",
    "Temperature_Difference",
    "Type_L",
    "Type_M"
])

shap_values = explainer.shap_values(sample)

importance = pd.DataFrame({
    "Feature": sample.columns,
    "SHAP Value": shap_values[0]
})

importance["Absolute"] = importance["SHAP Value"].abs()

importance = importance.sort_values("Absolute", ascending=False)

print(importance)
