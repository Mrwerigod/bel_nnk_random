import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32
import math
import random

class EMGPublisher(Node):
    def __init__(self):
        super().__init__('emg_publisher')
        self.publisher_ = self.create_publisher(Float32, 'emg_signal', 10)
        self.timer = self.create_timer(0.05, self.publish_emg)  # 20 Hz
        self.time = 0.0

    def publish_emg(self):
        base_signal = 50 * math.sin(2 * math.pi * 1 * self.time)  # 1 Hz szinusz
        noise = random.uniform(-5, 5)
        emg_value = base_signal + noise
        msg = Float32()
        msg.data = emg_value
        self.publisher_.publish(msg)
        self.get_logger().info(f'Publishing EMG: {emg_value:.2f} µV')
        self.time += 0.05

def main(args=None):
    rclpy.init(args=args)
    node = EMGPublisher()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
