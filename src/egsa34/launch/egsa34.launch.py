import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    ld = LaunchDescription()

    bus_interface_config = os.path.join(
        get_package_share_directory('egsa34'),
        'config',
        'bus_interface_config.yaml'
        )
        
    bus_interface=Node(
        package = 'egsa34',
        name = 'bus_interface',
        executable = 'bus_interface',
        parameters = [bus_interface_config]
    )
    
    cmd_handler=Node(
        package = 'egsa34',
        name = 'cmd_handler',
        executable = 'cmd_handler',
    )
    
    ximea = Node(
        package = 'egsa34',
        name = 'ximea',
        executable = 'ximea',
    )

    ld.add_action(bus_interface)
    ld.add_action(cmd_handler)
    ld.add_action(ximea)
    
    return ld