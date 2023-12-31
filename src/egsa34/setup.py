from setuptools import find_packages, setup
from glob import glob
import os

package_name = 'egsa34'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share/', package_name, 'launch'), glob('launch/*.launch.py')),
        (os.path.join('share/', package_name, 'config'), glob('config/*.yaml'))
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='egsa',
    maintainer_email='egsa@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'bus_interface = egsa34.bus_interface:main',
            'cmd_handler = egsa34.cmd_handler:main',
            'ximea = egsa34.ximea:main',
            'sync_emulator = egsa34.sync_emulator:main'
        ],
    },
)
