
import random
import csv

def generate_dummy_traffic_data(num_samples=1000, file_path="../dataset/generated_traffic.csv"):
    with open(file_path, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['rtt', 'packet_loss_rate', 'cwnd', 'throughput', 'congestion'])
        
        for _ in range(num_samples):
            rtt = random.randint(50, 300)  # RTT in ms
            packet_loss_rate = round(random.uniform(0.0, 0.15), 3)  # Loss rate between 0 and 15%
            cwnd = random.randint(2000, 10000)  # Congestion window size
            throughput = random.randint(5000, 15000)  # Throughput in bits/sec
            congestion = 1 if packet_loss_rate > 0.05 or rtt > 180 else 0  # Arbitrary congestion condition
            writer.writerow([rtt, packet_loss_rate, cwnd, throughput, congestion])

if __name__ == "__main__":
    generate_dummy_traffic_data()
