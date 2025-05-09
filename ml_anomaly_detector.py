import json
import time
import pandas as pd
from sklearn.ensemble import IsolationForest


DATA_FILE = "iot_stream.jsonl"
MODEL_WINDOW = 10 # use last N records for training
ANOMALY_THRESOLD = -0.2 # IsolationForest decision function thresold


def load_recent_data(file_path, window=MODEL_WINDOW):
    try:
        with open(file_path, "r") as f:
            lines = f.readlines()[-window:]
            records = [json.loads(line) for line in lines]
        
        df = pd.DataFrame(records)
        return df[["device_id", "timestamp", "temperature", "humidity"]]
    except Exception as e:
        print(f"Error Loading Data:" , e)
        return pd.DataFrame()
    
def detect_anomalies(df):
    model = IsolationForest(n_estimators=100, contamination=0.05, random_state=42)


    # Feature matrix (excluding timestamp and device ID)
    features = df[["temperature", "humidity"]]
    model.fit(features)

    # Predict anomalies
    scores = model.decision_function(features)
    df["anomaly_score"] = scores
    df["is_anomaly"] = scores < ANOMALY_THRESOLD

    return df[df["is_anomaly"] == True]

if __name__ == "__main__":
    print("Starting ML anomaly detector...\n")

    while True:
        data = load_recent_data(DATA_FILE)

        if not data.empty and len(data) >= MODEL_WINDOW:
            anomalies = detect_anomalies(data)
            if not anomalies.empty:
                print("Detected anomalies:\n", anomalies[["device_id", "timestamp", "temperature", "humidity"]])
            else:
                print("No anomalies detected in the recent batch")
        else:
            print("Wating for enough data...")
        
        time.sleep(5)