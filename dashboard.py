import streamlit as st
import pandas as pd
import json
from sklearn.ensemble import IsolationForest


DATA_FILE = "iot_stream.jsonl"
MODEL_WINDOW = 10

st.set_page_config(page_title="IoT Anomaly Detector", layout="wide")
st.title("Real-Time IoT Sensor Anomaly Dashboard")

def load_data():
    try:
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            lines = f.readlines()
            if len(lines) < MODEL_WINDOW:
                return pd.DataFrame()
            recent_lines = lines[-MODEL_WINDOW:]
            data = [json.loads(line.strip()) for line in recent_lines]
            return pd.DataFrame(data)
    except Exception as e:
        st.error(f"Error reading file: {e}")
        return pd.DataFrame()
    
def detect_anomalies(df):
    features = df[["temperature", "humidity"]]
    model = IsolationForest(n_estimators=100, contamination=0.2, random_state=42)
    model.fit(features)
    df["anomaly_score"] = model.decision_function(features)
    df["is_anomaly"] = df["anomaly_score"] < 0.0
    return df

df = load_data()
st.text(f"Rows loaded: {len(df)}") # Debug Line

if not df.empty:
    df = detect_anomalies(df)

    st.subheader("Sensor Readings")
    st.dataframe(df[["device_id", "timestamp", "temperature", "humidity", "motion_detected", "is_anomaly"]].tail(10), use_container_width=True)

    st.subheader("temperature and Humidity Trends")
    st.line_chart(df[["temperature", "humidity"]])
    
    st.subheader("Anomaly Detections")
    st.dataframe(df[df["is_anomaly"] == True][["device_id", "timestamp", "temperature", "humidity"]], use_container_width=True)
else:
    st.warning("Waiting for data....")