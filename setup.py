from setuptools import setup
import os
from glob import glob

package_name = 'my_robot_package'

setup(
    name=package_name,
    version='0.1.0',
    packages=[package_name],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='ajr',
    maintainer_email='ajr@FURBIFY-QJR1QN8',
    description='EMG signal simulation in ROS 2 (Python)',
    license='Apache-2.0',
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name, 'launch'), glob('launch/*.py')),
    ],
    entry_points={
        'console_scripts': [
            'emg_publisher = my_robot_package.emg_publisher:main',
            'emg_subscriber = my_robot_package.emg_subscriber:main',
        ],
    },
)
