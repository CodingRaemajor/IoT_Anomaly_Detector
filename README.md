📡 Real-Time IoT Anomaly Detection Dashboard
Live App: iotanomalydetector.streamlit.app

This project simulates live IoT sensor data, applies real-time machine learning-based anomaly detection, and visualizes everything using a clean Streamlit dashboard.

🚀 Features
Simulates multiple IoT devices (e.g., temperature, humidity, motion)
Injects occasional random anomalies
Detects outliers using Isolation Forest
Live visualization of:
     Sensor data table
     Temperature & humidity trends
     Detected anomalies
Deployable via Streamlit Cloud

🧠 Tech Stack
Python
Streamlit
Scikit-learn (Isolation Forest)
Pandas
JSONL for real-time logging

📂 Folder Structure
bash
Copy code
iot-anomaly-detector/
├── dashboard.py             # Main Streamlit app
├── iot_simulator.py         # Sensor data generator
├── ml_anomaly_detector.py   # CLI-based anomaly checker (optional)
├── anomaly_detector.py      # Rule-based detector (optional)
├── iot_stream.jsonl         # Real-time sensor data (generated live)
├── requirements.txt         # Dependencies
└── README.md                # You're here!

📦 Setup Instructions
1. Clone this repo
bash
Copy code
git clone https://github.com/CodingRaemajor/IoT_Anomaly_Detector.git
cd IoT_Anomaly_Detector
2. Install requirements
bash
Copy code
pip install -r requirements.txt
3. Run the simulator
bash
Copy code
python iot_simulator.py
4. Launch the dashboard
bash
Copy code
streamlit run dashboard.py

📊 Screenshots
DashBoard View
![Screenshot 2025-05-09 164933](https://github.com/user-attachments/assets/ed05575d-9143-4c92-911c-a34b7bd8ede2)

Anomaly Detection in Action
![Screenshot 2025-05-09 164945](https://github.com/user-attachments/assets/abe4786b-52d1-467f-acc6-9267bd76bf80)

✨ Future Enhancements
Sensor dropdown filtering
Auto-refresh every X seconds
Anomaly logging to CSV
LSTM autoencoder anomaly detection

👨‍💻 Author
Parth Patel
Computer Science Student @ University of Regina
📫 iparth2166@gmail.com


---
### 📄 License

This project is licensed under the [MIT License](LICENSE).
