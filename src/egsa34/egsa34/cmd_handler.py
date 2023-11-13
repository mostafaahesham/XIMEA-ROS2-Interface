import rclpy
from rclpy.node import Node
import sys
import os

from pl_interface.srv import BusReply
from pl_interface.msg import PldCmd

current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(current_dir)

from ssp import SSP
from log_level import LogLevel

class CmdHandler(Node,SSP,LogLevel):

    def __init__(_cmd):
        super().__init__('cmd_handler')
        SSP.__init__(_cmd)
        LogLevel.__init__(_cmd)
        
        _cmd.cmd_handler_service = _cmd.create_service(BusReply, 'bus_reply', _cmd.service_handler)
        _cmd.publisher = _cmd.create_publisher(PldCmd,'/payloads',10)
        
        _cmd.cmd = PldCmd()
        
        _cmd.callbacks = {
            str(_cmd.cmdPING):_cmd.ping_callback,
            str(_cmd.cmdRCS):_cmd.rcs_callback,
            str(_cmd.cmdGIMG):_cmd.gimg_callback,
            str(_cmd.cmdTIMG):_cmd.timg_callback,
            str(_cmd.cmdDIMG):_cmd.dimg_callback,
            str(_cmd.cmdCXT):_cmd.cxt_callback,
        }       

    def service_handler(_sh, req, res):
        
        _sh.log('info',f'{req}')  
                                             
        if req.err:
            res.cmd = _sh.rplyNACK
            res.data = [req.cmd,req.err]
            res.data_len = len(res.data)
            res.err = req.err
            
            return res
        
        else:
            cmd_callback = _sh.callbacks.get(str(req.cmd),_sh.default_callback)
            return cmd_callback(req, res)
            
    def ping_callback(_cb,req,res):
        res.cmd = _cb.rplyACK
        res.data_len = 1
        res.data = [req.cmd]
        
        return res
    
    def rcs_callback(_cb,req,res):
        pass
    
    def gimg_callback(_cb,req,res):
        
        _cb.cmd.cmd = req.cmd
        _cb.cmd.addr = req.data[0]
        
        _cb.publisher.publish(_cb.cmd)
        
        res.cmd = _cb.rplyACK
        res.data_len = 1
        res.data = [req.cmd]
        
        return res
    
    def timg_callback(_cb,req,res):
        pass
    
    def dimg_callback(_cb,req,res):
        pass
    
    def cxt_callback(_cb,req,res):
        pass
    
    def default_callback(_cb, req, res):
        _cb.log('error', f'Unknown command: {req.cmd}')
    
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