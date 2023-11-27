import rclpy
from rclpy.node import Node
from rclpy.signals import SignalHandlerOptions
import sys
import os
import RPi.GPIO as GPIO
import threading

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
        
        _cmd.syncPIN = 17
        _cmd.STATE = GPIO.LOW
        GPIO.setmode(GPIO.BCM)           
        GPIO.setup(_cmd.syncPIN, GPIO.IN)
        
        _cmd.cmd_handler_service = _cmd.create_service(BusReply, 'cmd_srv', _cmd.service_handler)
        _cmd.publisher = _cmd.create_publisher(PldCmd,'/payloads',10)
        
        _cmd.payloadCMD = PldCmd()
        
        _cmd.callbacks = {
            str(_cmd.cmdPING):_cmd.ping_callback,
            str(_cmd.cmdWD):_cmd.wd_callback,
            str(_cmd.cmdSM):_cmd.sm_callback,
            str(_cmd.cmdGM):_cmd.gm_callback,
            str(_cmd.cmdGSC):_cmd.gsc_callback,
            str(_cmd.cmdSSC):_cmd.ssc_callback,
            str(_cmd.cmdRCS):_cmd.rcs_callback,
            str(_cmd.cmdGIMG):_cmd.gimg_callback,
            str(_cmd.cmdTIMG):_cmd.timg_callback,
            str(_cmd.cmdDIMG):_cmd.dimg_callback,
            str(_cmd.cmdCXT):_cmd.cxt_callback,
        }       

    def service_handler(_sh, req, res):
        
        # _sh.log('info',f'{req}')  
                                        
        if req.err:
            res.cmd = _sh.rplyNACK
            res.data = [req.cmd,req.err]
            res.data_len = len(res.data)
            res.err = req.err
            # _sh.log('warn',f'err_status -> {_sh.errors[str(req.err)]} <{hex(req.err)}>')
            
            return res
        
        else:
            cmd_callback = _sh.callbacks.get(str(req.cmd),_sh.default_callback)
            return cmd_callback(req, res)
            
    def ping_callback(_cb,req,res):
        res.cmd = _cb.rplyACK
        res.data_len = 1
        res.data = [req.cmd]
        
        return res
    
    def wd_callback(_cb,req,res):
        res.cmd = _cb.rplyACK
        res.data_len = 1
        res.data = [req.cmd]
        
        return res
    
    def sm_callback(_cb,req,res):
        if req.data[0] not in _cb.satMODEs:
            
            res.cmd = _cb.rplyNACK
            res.data = [req.cmd,_cb.errPARAMS]
            res.data_len = len(res.data)
            res.err = _cb.errPARAMS
            
            return res
        else:
            _cb.satMODE = req.data[0]
            
            res.cmd = _cb.rplyACK
            res.data_len = 1
            res.data = [req.cmd]
            
            return res
    
    def gm_callback(_cb,req,res):
        res.cmd = req.cmd | 1 << 6
        res.data_len = 1
        res.data = [_cb.satMODE]
        
        return res
    
    def gsc_callback(_cb,req,res):  
        res.cmd = req.cmd | 1 << 6
        res.data = _cb.syncCOUNTER.to_bytes(8,'big')
        res.data_len = len(res.data)
        
        return res
    
    def ssc_callback(_cb,req,res):  
        _cb.syncCOUNTER = int.from_bytes(bytearray(req.data), byteorder="big")
        
        res.cmd = _cb.rplyACK
        res.data_len = 1
        res.data = [req.cmd]
        
        return res
    
    def rcs_callback(_cb,req,res):
        _cb.payloadCMD.cmd = req.cmd
        _cb.payloadCMD.cam_id = req.data[_cb.idxCAM_ID]
        _cb.payloadCMD.config = req.data[_cb.idxCAM_ID + 1:]
        
        _cb.publisher.publish(_cb.payloadCMD)
        
        res.cmd = _cb.rplyACK
        res.data_len = 1
        res.data = [req.cmd]
            
        return res
    
    def gimg_callback(_cb,req,res):        
        pass
    
    def timg_callback(_cb,req,res):
        pass
    
    def dimg_callback(_cb,req,res):
        pass
    
    def cxt_callback(_cb,req,res):
        pass
    
    def sync_increment(_cb):
        current_state = GPIO.LOW
        while True:
            new_state = GPIO.input(_cb.syncPIN)
            if current_state == GPIO.LOW and new_state == GPIO.HIGH:
                current_state = new_state
                _cb.syncCOUNTER += 1
                _cb.log('',f'{_cb.bold}sync counter -> {_cb.syncCOUNTER}s')

            elif current_state == GPIO.HIGH and new_state == GPIO.LOW:
                current_state = new_state
    
    def default_callback(_cb, req, res):
        _cb.log('error', f'Unknown command: {req.cmd}')
    
        return res

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

def main(args=None):
    rclpy.init(args=args)

    cmd_handler = CmdHandler()
    sync_thread = threading.Thread(target=cmd_handler.sync_increment)
    sync_thread.start()

    rclpy.spin(cmd_handler)
    sync_thread.join()

    rclpy.shutdown()

if __name__ == '__main__':
    main()