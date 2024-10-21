
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import joblib

class CongestionPredictor:
    def __init__(self):
        self.model = RandomForestClassifier(n_estimators=100, random_state=42)
    
    def load_data(self, path):
        data = pd.read_csv(path)
        X = data[['rtt', 'packet_loss_rate', 'cwnd', 'throughput']]
        y = data['congestion']
        return train_test_split(X, y, test_size=0.2, random_state=42)
    
    def train(self, X_train, y_train):
        self.model.fit(X_train, y_train)
    
    def evaluate(self, X_test, y_test):
        y_pred = self.model.predict(X_test)
        accuracy = accuracy_score(y_test, y_pred)
        print(f"Accuracy: {accuracy * 100:.2f}%")
    
    def save_model(self, path):
        joblib.dump(self.model, path)
    
    def load_model(self, path):
        self.model = joblib.load(path)
    
    def predict(self, input_data):
        return self.model.predict(input_data)

if __name__ == "__main__":
    predictor = CongestionPredictor()
    X_train, X_test, y_train, y_test = predictor.load_data("../dataset/dummy_dataset.csv")
    predictor.train(X_train, y_train)
    predictor.evaluate(X_test, y_test)
    predictor.save_model("../models/congestion_model.pkl")
