import pyodbc
import pandas as pd


def get_connection():
    """
    Create and return a SQL Server connection.
    """
    conn = pyodbc.connect(
        "DRIVER={ODBC Driver 17 for SQL Server};"
        "SERVER=DESKTOP-JS0I57G\\SQLEXPRESS;"
        "DATABASE=PredictiveMaintenanceDB;"
        "Trusted_Connection=yes;"
    )
    return conn


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
    """

    conn = get_connection()
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


def get_prediction_history():
    """
    Read all prediction history from SQL Server.
    """

    conn = get_connection()

    query = """
        SELECT *
        FROM PredictionHistory
        ORDER BY PredictionTime DESC
    """

    df = pd.read_sql(query, conn)

    conn.close()

    return df
