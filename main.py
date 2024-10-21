
import pandas as pd
from models.model import CongestionPredictor

def run_congestion_control():
    # Load pre-trained model
    predictor = CongestionPredictor()
    predictor.load_model("./models/congestion_model.pkl")

    # Load new traffic data (this could be from a real-time source in a real project)
    traffic_data = pd.read_csv("./dataset/generated_traffic.csv")

    X_new = traffic_data[['rtt', 'packet_loss_rate', 'cwnd', 'throughput']]
    predictions = predictor.predict(X_new)

    # Print results
    for i, pred in enumerate(predictions):
        print(f"Sample {i + 1}: Congestion {'detected' if pred == 1 else 'not detected'}")

if __name__ == "__main__":
    run_congestion_control()
