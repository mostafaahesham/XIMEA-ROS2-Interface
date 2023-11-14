import rclpy
from rclpy.node import Node
import sys
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(current_dir)

from log_level import LogLevel

class SysMonitor(Node,LogLevel):
    def __init__(_mon):
        super().__init__('sys_monitor')
        LogLevel.__init__(_mon)
            
    def log(_log,type,log):
        match type:
            case "err":
                _log.get_logger().info(f'{_log.red}{log}{_log.reset}')
            case 'warn':
                _log.get_logger().info(f'{_log.yellow}{log}{_log.reset}')
            case 'status_nok':
                _log.get_logger().info(f'{_log.pink}{log}{_log.reset}')  
            case 'status_ok':
                _log.get_logger().info(f'{_log.cyan}{log}{_log.reset}')
            case 'info':
                _log.get_logger().info(f'{_log.green}{log}{_log.reset}')
            case _:
                _log.get_logger().info(f'{_log.darkgrey}{log}{_log.reset}')

def main(args=None):
    rclpy.init(args=args)

    sys_monitor = SysMonitor()
    
    rclpy.spin(sys_monitor)

    rclpy.shutdown()

if __name__ == '__main__':
    main()