
import streamlit as st
import mysql.connector
import pandas as pd

# Database connection
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="31012001",
    database="flight_analytics"
)

query = "SELECT * FROM flights"
df = pd.read_sql(query, conn)

st.title("Flight Analytics Dashboard")

st.metric("Total Flights ", len(df))

st.subheader("Flights Data")
st.dataframe(df)

airport = st.selectbox(
    "Select Origin Airport",
    df["origin_iata"].unique()
)

fitered_df = df[df["origin_iata"] ==
airport]

st.subheader("Fitered Flights")
st.dataframe(fitered_df)
