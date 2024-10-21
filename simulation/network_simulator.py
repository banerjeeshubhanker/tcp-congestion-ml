
import gym
from gym import spaces
import numpy as np

class NetworkCongestionEnv(gym.Env):
    """Custom Environment that simulates a network for TCP congestion control."""
    
    def __init__(self):
        super(NetworkCongestionEnv, self).__init__()
        
        # Define action and observation space
        # Actions represent changes in the congestion window (CWND)
        self.action_space = spaces.Discrete(3)  # 0: Decrease CWND, 1: Keep CWND, 2: Increase CWND
        
        # Observations include RTT, packet_loss_rate, CWND, throughput
        self.observation_space = spaces.Box(low=np.array([50, 0.0, 1000, 0]), 
                                            high=np.array([500, 1.0, 10000, 20000]),
                                            dtype=np.float32)
        
        # Initial state
        self.state = [100, 0.01, 5000, 10000]  # Initial RTT, packet loss rate, CWND, throughput
        
        # Parameters for the network (simulated)
        self.bandwidth = 10000  # Max throughput (bits/sec)
        self.base_rtt = 100  # Base RTT in milliseconds
    
    def step(self, action):
        rtt, packet_loss_rate, cwnd, throughput = self.state
        
        # Modify CWND based on the action
        if action == 0:  # Decrease CWND
            cwnd = max(1000, cwnd - 500)
        elif action == 2:  # Increase CWND
            cwnd = min(10000, cwnd + 500)
        
        # Simulate packet loss based on network congestion (simplified model)
        if cwnd > self.bandwidth:
            packet_loss_rate = min(1.0, packet_loss_rate + 0.05)  # High packet loss
        else:
            packet_loss_rate = max(0.0, packet_loss_rate - 0.01)  # Lower packet loss
        
        # Simulate RTT based on congestion
        if packet_loss_rate > 0.05:
            rtt = min(500, rtt + 20)  # High RTT due to congestion
        else:
            rtt = max(self.base_rtt, rtt - 10)  # Lower RTT
        
        # Update throughput based on CWND and packet loss
        throughput = cwnd * (1 - packet_loss_rate)
        
        # Update state
        self.state = [rtt, packet_loss_rate, cwnd, throughput]
        
        # Define a reward: Higher throughput, lower RTT and packet loss is better
        reward = throughput - (rtt * packet_loss_rate * 100)
        
        # Done flag (you can define a specific condition to end the episode)
        done = False
        
        return np.array(self.state, dtype=np.float32), reward, done, {}
    
    def reset(self):
        """Reset the environment to an initial state."""
        self.state = [100, 0.01, 5000, 10000]  # Initial state: RTT, packet loss rate, CWND, throughput
        return np.array(self.state, dtype=np.float32)
    
    def render(self, mode='human'):
        """Render the environment (optional)."""
        rtt, packet_loss_rate, cwnd, throughput = self.state
        print(f"RTT: {rtt} ms, Packet Loss Rate: {packet_loss_rate}, CWND: {cwnd}, Throughput: {throughput} bps")

# Register the environment (optional, if you want to add to Gym registry)
from gym.envs.registration import register
register(id='NetworkCongestion-v0', entry_point='__main__:NetworkCongestionEnv', max_episode_steps=200)
