import pyodbc
import pandas as pd


# ============================================================
# SQL SERVER CONNECTION
# ============================================================

def get_connection():
    """
    Creates and returns a SQL Server connection.

    Returns:
        pyodbc.Connection if successful
        None if SQL Server is unavailable
    """

    try:
        conn = pyodbc.connect(
            "DRIVER={ODBC Driver 17 for SQL Server};"
            "SERVER=DESKTOP-JS0I57G\\SQLEXPRESS;"
            "DATABASE=PredictiveMaintenanceDB;"
            "Trusted_Connection=yes;"
        )

        return conn

    except Exception as e:

        print(f"Database Connection Error: {e}")

        return None


# ============================================================
# SAVE PREDICTION
# ============================================================

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
    Save prediction into SQL Server.

    Returns:
        True  -> Saved successfully
        False -> Database unavailable
    """

    conn = get_connection()

    if conn is None:
        return False

    try:

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

        return True

    except Exception as e:

        print(f"Error Saving Prediction: {e}")

        return False

    finally:

        conn.close()


# ============================================================
# GET PREDICTION HISTORY
# ============================================================

def get_prediction_history():
    """
    Returns prediction history.

    If SQL Server is unavailable,
    returns an empty DataFrame.
    """

    conn = get_connection()

    if conn is None:
        return pd.DataFrame()

    try:

        query = """
        SELECT *
        FROM PredictionHistory
        ORDER BY PredictionTime DESC
        """

        df = pd.read_sql(query, conn)

        return df

    except Exception as e:

        print(f"Error Reading Database: {e}")

        return pd.DataFrame()

    finally:

        conn.close()


# ============================================================
# DATABASE STATUS
# ============================================================

def database_available():
    """
    Checks whether SQL Server is available.

    Returns:
        True or False
    """

    conn = get_connection()

    if conn is None:
        return False

    conn.close()

    return True
