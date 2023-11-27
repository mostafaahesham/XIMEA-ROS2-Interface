import rclpy
from rclpy.node import Node
from rclpy.signals import SignalHandlerOptions
import sys
import os
import time
from ximea import xiapi
import ximea

from pl_interface.msg import PldCmd

current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(current_dir)

from ssp import SSP
from log_level import LogLevel

class Ximea(Node,SSP,LogLevel):
    def __init__(_x):
        super().__init__('ximea')
        SSP.__init__(_x)
        LogLevel.__init__(_x)  
        
        _x.subscriber = _x.create_subscription(PldCmd,'/payloads',_x.payload_callback,10)
        
        _x.cam = xiapi.Camera()
        _x.cam.set_debug_level("XI_DL_WARNING")
        # _x.cam.open_device()
        
    def log(_log,type,log):
        match type:
            case "err":
                _log.get_logger().info(f'{_log.red}{log}{_log.reset}')
            case 'warn':
                _log.get_logger().info(f'{_log.yellow}{log}{_log.reset}')
            case 'nok':
                _log.get_logger().info(f'{_log.pink}{log}{_log.reset}')  
            case 'ok':
                _log.get_logger().info(f'{_log.cyan}{log}{_log.reset}')
            case 'info':
                _log.get_logger().info(f'{_log.green}{log}{_log.reset}')
            case _:
                _log.get_logger().info(f'{_log.darkgrey}{log}{_log.reset}')
                
    def payload_callback(_cb,data):
        _cb.log('warn',f'{data}')
                
def main(args=None):
    rclpy.init(args=args)

    ximea = Ximea()
        
    rclpy.spin(ximea)

    rclpy.shutdown()

if __name__ == '__main__':
    main()