"""
Database layer — hybrid backend.

Tries SQL Server first (office / local development).
If unavailable (e.g. deployed on Streamlit Cloud), automatically
falls back to a local SQLite database so the app works anywhere.

Public interface (unchanged — pages need no edits):
    save_prediction(...)        -> True / False
    get_prediction_history()    -> pandas DataFrame
    database_available()        -> True / False
"""

import sqlite3
import pandas as pd

# pyodbc may not be installable everywhere — guard the import
try:
    import pyodbc
    PYODBC_OK = True
except Exception:
    PYODBC_OK = False

SQLITE_FILE = "predictions.db"


# ============================================================
# SQL SERVER CONNECTION (office / local)
# ============================================================

def get_sqlserver_connection():
    """Returns a SQL Server connection, or None if unreachable."""
    if not PYODBC_OK:
        return None
    try:
        conn = pyodbc.connect(
            "DRIVER={ODBC Driver 17 for SQL Server};"
            "SERVER=DESKTOP-JS0I57G\\SQLEXPRESS;"
            "DATABASE=PredictiveMaintenanceDB;"
            "Trusted_Connection=yes;",
            timeout=3,
        )
        return conn
    except Exception as e:
        print(f"SQL Server unavailable, using SQLite fallback: {e}")
        return None


# ============================================================
# SQLITE FALLBACK (cloud / anywhere)
# ============================================================

def get_sqlite_connection():
    """Returns a SQLite connection, creating the table if needed."""
    conn = sqlite3.connect(SQLITE_FILE)
    conn.execute("""
        CREATE TABLE IF NOT EXISTS PredictionHistory (
            Id INTEGER PRIMARY KEY AUTOINCREMENT,
            MachineType TEXT,
            AirTemperature REAL,
            ProcessTemperature REAL,
            RotationalSpeed REAL,
            Torque REAL,
            ToolWear REAL,
            TemperatureDifference REAL,
            Prediction TEXT,
            Confidence REAL,
            PredictionTime TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)
    conn.commit()
    return conn


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
    confidence,
):
    """Save a prediction. Returns True if saved, False otherwise."""

    values = (
        str(machine_type),
        float(air_temp),
        float(process_temp),
        float(rotational_speed),
        float(torque),
        float(tool_wear),
        float(temp_difference),
        str(prediction),
        float(confidence),
    )

    # --- Try SQL Server first ---
    conn = get_sqlserver_connection()
    if conn is not None:
        try:
            cursor = conn.cursor()
            cursor.execute(
                """
                INSERT INTO PredictionHistory
                (MachineType, AirTemperature, ProcessTemperature,
                 RotationalSpeed, Torque, ToolWear,
                 TemperatureDifference, Prediction, Confidence)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
                """,
                values,
            )
            conn.commit()
            cursor.close()
            return True
        except Exception as e:
            print(f"Error saving to SQL Server: {e}")
        finally:
            conn.close()

    # --- Fallback: SQLite ---
    try:
        conn = get_sqlite_connection()
        conn.execute(
            """
            INSERT INTO PredictionHistory
            (MachineType, AirTemperature, ProcessTemperature,
             RotationalSpeed, Torque, ToolWear,
             TemperatureDifference, Prediction, Confidence)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
            """,
            values,
        )
        conn.commit()
        conn.close()
        return True
    except Exception as e:
        print(f"Error saving to SQLite: {e}")
        return False


# ============================================================
# GET PREDICTION HISTORY
# ============================================================

def get_prediction_history():
    """Returns prediction history as a DataFrame (empty if none)."""

    # --- Try SQL Server first ---
    conn = get_sqlserver_connection()
    if conn is not None:
        try:
            df = pd.read_sql(
                "SELECT * FROM PredictionHistory ORDER BY PredictionTime DESC",
                conn,
            )
            return df
        except Exception as e:
            print(f"Error reading SQL Server: {e}")
        finally:
            conn.close()

    # --- Fallback: SQLite ---
    try:
        conn = get_sqlite_connection()
        df = pd.read_sql_query(
            "SELECT * FROM PredictionHistory ORDER BY PredictionTime DESC",
            conn,
        )
        conn.close()
        return df
    except Exception as e:
        print(f"Error reading SQLite: {e}")
        return pd.DataFrame()


# ============================================================
# DATABASE STATUS
# ============================================================

def database_available():
    """True if any database backend is usable (it always is, via SQLite)."""
    conn = get_sqlserver_connection()
    if conn is not None:
        conn.close()
        return True
    try:
        conn = get_sqlite_connection()
        conn.close()
        return True
    except Exception:
        return False
