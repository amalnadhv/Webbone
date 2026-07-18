import pyodbc
import pandas as pd
import streamlit as st


def get_connection():

    try:
        conn = pyodbc.connect(
            "DRIVER={ODBC Driver 17 for SQL Server};"
            "SERVER=sreeji, 1475;"
            "DATABASE=WAQTH;"
            "UID=sa;"
            "PWD=QDCqdc123;"
            "TrustServerCertificate=no;"
        )

        return conn

    except Exception as e:
        st.error(f"Database Connection Failed: {e}")
        return None


def execute_query(query):

    conn = get_connection()

    if conn is None:
        return None

    try:
        df = pd.read_sql(query, conn)
        conn.close()
        return df

    except Exception as e:
        st.error(f"Query Error: {e}")
        return None


def execute_scalar(query):

    conn = get_connection()

    if conn is None:
        return 0

    try:
        cursor = conn.cursor()
        cursor.execute(query)

        result = cursor.fetchone()

        conn.close()

        if result:
            return result[0]

        return 0

    except Exception as e:
        st.error(f"Query Error: {e}")
        return 0
