import streamlit as st
from database import execute_scalar


st.set_page_config(
    page_title="Bone Mobile",
    layout="wide"
)


st.title("Comrade Business One Mobile")


sales = execute_scalar("""
SELECT 
    ISNULL(SUM(
        CASE 
        WHEN tran_type='SINVOICE' 
        THEN d 
        ELSE -d 
        END
    ),0)

FROM asinv

WHERE inv_date = CAST(GETDATE() AS DATE)

""")


col1, col2 = st.columns(2)


with col1:
    st.metric(
        "Today's Sales",
        f"AED {sales:,.2f}"
    )


with col2:
    st.metric(
        "Status",
        "Connected"
    )
