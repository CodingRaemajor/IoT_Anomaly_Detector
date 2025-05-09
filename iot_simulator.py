import json
import random
import time
from datetime import datetime

# Define multiple devices IDs

DEVICE_IDS = [f"sensor_{i:02}" for i in range(1,6)]

def generate_sensor_data(device_id):
    # Slightly unique normal ramges per device
    base_temp = 20 + int(device_id[-2:]) * 0.5
    base_humidity = 40 + int(device_id[-2:]) * 1.5

    tempreture = round(random.normalvariate(base_temp, 1.2), 2)
    humidity = round(random.normalvariate(base_humidity, 3), 2)
    motion = random.choices([True, False], weights=[0.1,0.9])[0]

    #Inject anomalies randomly
    if random.random() < 0.5:
        tempreture = round(random.uniform(40, 60), 2)
    if random.random() < 0.3:
        humidity = round(random.uniform(0, 10), 2)
    if random.random() < 0.01:
        motion = True

    return {
        "device_id": device_id,
        "timestamp": datetime.now().isoformat(),
        "temperature": tempreture,
        "humidity": humidity,
        "motion_detected": motion
    }

if __name__ == "__main__":
    print("Starting IoT Simulator...\n")
    while True:
        for device_id in DEVICE_IDS:
            data = generate_sensor_data(device_id)
            with open("iot_stream.jsonl", "a") as f:
                f.write(json.dumps(data) + "\n")
        time.sleep(1) # 1-second interval between data batches