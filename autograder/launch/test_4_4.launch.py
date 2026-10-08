from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from ament_index_python.packages import get_package_share_directory
import os

def generate_launch_description():
    ekf_file = os.path.join(
        get_package_share_directory('stinger_bringup'),
        'config',
        'ekf.yaml'
    )

    localization_launch = os.path.join(
        get_package_share_directory('stinger_bringup'),
        'launch',
        'localization.launch.py'
    )

    return LaunchDescription([
        Node(
            package='autograder',
            executable='test_topic_4_4',
            name='ekf_filter_node',
            output='screen',
            parameters=[ekf_file]
        ),
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource(localization_launch),
            # This configuration/remapping check runs without Gazebo or /clock.
            launch_arguments={
                'use_sim_time': 'false',
                'publish_robot_description': 'false',
            }.items()
        ),
    ])
