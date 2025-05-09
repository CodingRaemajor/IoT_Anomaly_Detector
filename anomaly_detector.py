import json
import time
import os

# Tracking repeated motion 
motion_counts = {}
file_path = "iot_stream.jsonl"
last_size = 0

def is_anomaly(data):
    device = data["device_id"]
    temp = data["temperature"]
    humidity = data["humidity"]
    motion = data["motion"]

    # Motion anomaly detection
    if device not in motion_counts:
        motion_counts[device] = 0
    
    if motion:
        motion_counts[device] += 1
    else:
        motion_counts[device] = 0
    
    return (
        temp < 15 or temp > 35 or
        humidity < 20 or humidity > 70 or
        motion_counts[device] >= 3
    )

print("Watching for anomalies in 'iot_stream.jsonl'...\n")
while True:
    try:
        with open(file_path, "r") as f:
            f.seek(last_size)
            for line in f:
                data = json.loads(line.strip())
                if is_anomaly(data):
                    print(f"[Alert ANOMALY] {json.dumps(data)}")
                else:
                    print(f"[Normal] {data['device_id']} at {data['timestamp']}")
            last_size = f.tell()
    except Exception as e:
        print(f"Error processing line: {e}")
    
    time.sleep(1)    
    