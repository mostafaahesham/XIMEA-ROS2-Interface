import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    ld = LaunchDescription()

    config = os.path.join(
        get_package_share_directory('egsa34'),
        'config',
        'config.yaml'
        )
        
    bus_interface_0=Node(
        namespace='p0',
        package = 'egsa34',
        name = 'bus_interface',
        executable = 'bus_interface',
        remappings=[
        ('/p0/cmd_srv', '/cmd_srv'),
        ],
        parameters = [config]
    )
    
    bus_interface_1=Node(
        namespace='p1',
        package = 'egsa34',
        name = 'bus_interface',
        executable = 'bus_interface',
        remappings=[
        ('/p1/cmd_srv', '/cmd_srv'),
        ],
        parameters = [config]
    )
    
    cmd_handler=Node(
        package = 'egsa34',
        name = 'cmd_handler',
        executable = 'cmd_handler',
        parameters = [config]
    )
    
    ximea = Node(
        package = 'egsa34',
        name = 'ximea',
        executable = 'ximea',
    )

    ld.add_action(bus_interface_0)
    ld.add_action(bus_interface_1)
    ld.add_action(cmd_handler)
    ld.add_action(ximea)
    
    return ld