import rclpy
from rclpy.node import Node
import sys
import os

from pl_interface.srv import BusReply

current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(current_dir)

from ssp import SSP
from log_level import LogLevel

class CmdHandler(Node,SSP,LogLevel):

    def __init__(_cmd):
        super().__init__('cmd_handler')
        SSP.__init__(_cmd)
        LogLevel.__init__(_cmd)
        _cmd.cmd_handler = _cmd.create_service(BusReply, 'bus_reply', _cmd.reply_callback)
        
        _cmd.callbacks = {
            str(_cmd.cmdPING):_cmd.ping_callback
        }       

    def reply_callback(_cb, req, res):
        
        _cb.log('info',f'{req}')  
                                             
        if req.err:
            res.cmd = _cb.rplyNACK
            res.data = [req.cmd,req.err]
            res.data_len = len(res.data)
            res.err = req.err
            
            return res
        
        else:
            cmd_callback = _cb.callbacks.get(str(req.cmd),_cb.default_callback)
            return cmd_callback(req, res)
            
    def ping_callback(_cb,req,res):
        res.cmd = _cb.rplyACK
        res.data_len = 1
        res.data = [req.cmd]
        
        return res
    
    def default_callback(_cb, req, res):
        _cb.log('info', f'Unknown command: {req.cmd}')
    
        return res

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

    cmd_handler = CmdHandler()

    rclpy.spin(cmd_handler)

    rclpy.shutdown()

if __name__ == '__main__':
    main()