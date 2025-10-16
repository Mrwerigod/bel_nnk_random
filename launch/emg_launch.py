from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='my_robot_package',
            executable='emg_publisher',
            name='emg_publisher'
        ),
        Node(
            package='my_robot_package',
            executable='emg_subscriber',
            name='emg_subscriber'
        )
    ])
