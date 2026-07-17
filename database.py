import pyodbc
import pandas as pd


# ----------------------------------------------------
# Database Connection
# ----------------------------------------------------

def get_connection():
    """
    Create and return a SQL Server connection.
    Returns None if SQL Server is unavailable.
    """

    try:
        conn = pyodbc.connect(
            "DRIVER={ODBC Driver 17 for SQL Server};"
            "SERVER=DESKTOP-JS0I57G\\SQLEXPRESS;"
            "DATABASE=PredictiveMaintenanceDB;"
            "Trusted_Connection=yes;"
        )

        return conn

    except Exception:
        return None


# ----------------------------------------------------
# Save Prediction
# ----------------------------------------------------

def save_prediction(
    machine_type,
    air_temp,
    process_temp,
    rotational_speed,
    torque,
    tool_wear,
    temp_difference,
    prediction,
    confidence
):
    """
    Save prediction results into SQL Server.
    Returns True if saved successfully.
    Returns False if SQL Server is unavailable.
    """

    conn = get_connection()

    if conn is None:
        return False

    cursor = conn.cursor()

    query = """
        INSERT INTO PredictionHistory
        (
            MachineType,
            AirTemperature,
            ProcessTemperature,
            RotationalSpeed,
            Torque,
            ToolWear,
            TemperatureDifference,
            Prediction,
            Confidence
        )
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
    """

    values = (
        str(machine_type),
        float(air_temp),
        float(process_temp),
        float(rotational_speed),
        float(torque),
        float(tool_wear),
        float(temp_difference),
        str(prediction),
        float(confidence)
    )

    cursor.execute(query, values)

    conn.commit()

    cursor.close()
    conn.close()

    return True


# ----------------------------------------------------
# Get Prediction History
# ----------------------------------------------------

def get_prediction_history():
    """
    Read all prediction history from SQL Server.
    Returns an empty DataFrame if SQL Server is unavailable.
    """

    conn = get_connection()

    if conn is None:
        return pd.DataFrame()

    query = """
        SELECT *
        FROM PredictionHistory
        ORDER BY PredictionTime DESC
    """

    df = pd.read_sql(query, conn)

    conn.close()

    return df
