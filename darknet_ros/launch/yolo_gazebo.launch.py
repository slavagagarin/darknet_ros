from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_ros.actions import Node

def generate_launch_description():
    darknet_ros_share_dir = get_package_share_directory('darknet_ros')
    network_param_file = darknet_ros_share_dir + '/config/yolov7-tiny.yaml'

    darknet_ros_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([darknet_ros_share_dir + '/launch/darknet_ros.launch.py']),
        launch_arguments={'network_param_file': network_param_file}.items()
    )

    gazebo_simulation = Node(
        package="your_gazebo_package", # replace with your actual package name
        executable="your_gazebo_executable", # replace with your actual executable name
        name="gazebo", # replace with your actual node name, if needed
        parameters=[
            {'your_parameter': "your_value"},
        ])

    return LaunchDescription([
        darknet_ros_launch,
        gazebo_simulation,
    ])
 
