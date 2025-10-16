import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32

class EMGSubscriber(Node):
    def __init__(self):
        super().__init__('emg_subscriber')
        self.subscription = self.create_subscription(
            Float32,
            'emg_signal',
            self.callback,
            10
        )
        self.values = []

    def callback(self, msg):
        self.values.append(msg.data)
        avg = sum(self.values) / len(self.values)
        self.get_logger().info(f'Received: {msg.data:.2f} µV | Average: {avg:.2f} µV')

def main(args=None):
    rclpy.init(args=args)
    node = EMGSubscriber()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
