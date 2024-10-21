
# TCP Congestion Control using Machine Learning

## Project Structure
```
tcp-congestion-ml/
│
├── dataset/
│   └── dummy_dataset.csv  # Dummy dataset with network traffic metrics
├── models/
│   ├── model.py           # ML model for congestion control
│   ├── rl_agent.py        # Reinforcement learning agent for congestion control (optional)
├── simulation/
│   ├── network_simulation.py  # Network simulation code using Mininet or ns-3
│   └── traffic_generator.py   # Script to generate traffic and collect network stats
├── utils/
│   ├── data_loader.py         # Load and preprocess the data
│   └── helpers.py             # Helper functions (e.g., feature engineering)
├── main.py                 # Main file to run the ML model for congestion control
└── README.md               # Instructions on how to run the project
```

## How to Run

### 1. Install Dependencies
Make sure you have the required Python packages installed. You can install them via pip:
```
pip install -r requirements.txt
```

### 2. Run the Traffic Generator
Generate dummy traffic data:
```
python simulation/traffic_generator.py
```

### 3. Train the ML Model
Train the congestion prediction model using the dummy dataset:
```
python models/model.py
```

### 4. Run the Congestion Control System
Use the trained model to predict congestion in the generated traffic:
```
python main.py
```

### 5. (Optional) Reinforcement Learning Agent
To train and run a reinforcement learning agent:
```
python models/rl_agent.py
```

## Notes:
- This is a simplified codebase to demonstrate ML applied to TCP congestion control. In a real-world project, you would need to integrate this with real-time traffic from a network simulator like ns-3 or Mininet.
