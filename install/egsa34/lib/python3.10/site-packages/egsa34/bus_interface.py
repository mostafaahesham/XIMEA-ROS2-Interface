import rclpy
from rclpy.node import Node
import serial
import sys
import os
import time
import threading
from rclpy.logging import LoggingSeverity
from pl_interface.msg import BusCmd, BusReply
from pl_interface.srv import BusReply

current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(current_dir)

from ssp import SSP
from log_level import LogLevel

class BusInterface(Node,SSP,LogLevel):
    def __init__(_bus,addr):
        super().__init__('bus_interface')
        SSP.__init__(_bus)
        LogLevel.__init__(_bus)
        _bus.declare_parameters(
            namespace='',
            parameters=[
                ('uart_config.ports.port0', ""),
                ('uart_config.ports.port1', ""),
                ('uart_config.baud_rate', 0),
                ('uart_config.parity', ""),
                ('uart_config.timeout', 0.0),
            ])
        _bus.portUART0 = _bus.get_parameter("uart_config.ports.port0").value
        _bus.portUART1 = _bus.get_parameter("uart_config.ports.port1").value
        _bus.baudRATE = _bus.get_parameter("uart_config.baud_rate").value
        _bus.PARITY = _bus.get_parameter("uart_config.parity").value 
        _bus.TIMEOUT = _bus.get_parameter("uart_config.timeout").value
        
        _bus.SER0 = None
        _bus.SER1 = None
        _bus.serMAIN = None
        
        _bus.addr = addr
        
        _bus.log('info',f'subsystem <{hex(_bus.addr)}> up and running')
        
        _bus.bus_client = _bus.create_client(BusReply, 'bus_reply')       
        while not _bus.bus_client.wait_for_service(timeout_sec=1.0):
            _bus.log('',f'waiting for <{_bus.bus_client.srv_name}> service')
        _bus.log('status_ok',f'service <{_bus.bus_client.srv_name}> ready')
        _bus.req = BusReply.Request()
        
    def send_request(_sr,cmd,data):
        if _sr.errCODE:            
            _sr.req.cmd = cmd
            _sr.req.err = _sr.errCODE
            
        else:
            _sr.req.cmd = cmd
            _sr.req.data_len = len(data)
            _sr.req.data = data
                            
        _sr.future = _sr.bus_client.call_async(_sr.req)
            
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
        
    def open_serial_ports(_osp):
        try:
            _osp.SER0 = serial.Serial(port=_osp.portUART0, baudrate=_osp.baudRATE, parity=_osp.PARITY, timeout=_osp.TIMEOUT)
            _osp.log('status_ok',f'successfully opened comm port {_osp.SER0.name}')
        except Exception as e:
            _osp.log('status_nok',f"couldn't open comm port {_osp.portUART0}")
            _osp.log('err',f'{e}')
        try:
            _osp.SER1 = serial.Serial(port=_osp.portUART1, baudrate=_osp.baudRATE, parity=_osp.PARITY, timeout=_osp.TIMEOUT)
            _osp.log('status_ok',f'successfully opened comm port {_osp.SER1.name}')
        except Exception as e:
            _osp.log('status_nok',f"couldn't open comm port {_osp.portUART1}")
            _osp.log('err',f'{e}')
            
    def transmit_frame(_tf,frame):
        try:
            while _tf.serMAIN.out_waiting:
                pass
            
            _tf.serMAIN.write(bytearray(frame))
            data_len = frame[_tf.idxDATA_LEN]
            sent = {
                # "flag_s":frame[_tf.idxSTART_FLAG],
                "dest":frame[_tf.idxDEST_ADDR],
                "src":frame[_tf.idxSRC_ADDR],
                "cmd":frame[_tf.idxCMD_ID],
                "data_len":frame[_tf.idxDATA_LEN],
                "data":frame[_tf.idxDATA_START:_tf.idxDATA_START + data_len],
                # "crc_0":frame[_tf.idxCRC_0],
                # "crc_1":frame[_tf.idxCRC_1],
                # "flag_e":frame[_tf.idxEND_FLAG],
            }
            _tf.log('status_ok',f"reply -> {sent} on {_tf.serMAIN.name}")
        except Exception as e:
            _tf.log('status_nok',"frame not sent")
            _tf.log('err',f'{e}')
    
    def recieve_frame(_rf):
        frame = b''
        try:
            _rf.log('',"waiting for commands...")
            while not (_rf.SER0.in_waiting or _rf.SER1.in_waiting):
                pass
            
            if _rf.SER0.in_waiting:
                _rf.serMAIN = _rf.SER0
                
            if _rf.SER1.in_waiting:
                _rf.serMAIN = _rf.SER1
        
            while _rf.serMAIN.in_waiting:
                temp = _rf.serMAIN.read(5)
                frame += temp
                data_length = temp[-1]
                temp = _rf.serMAIN.read(data_length + 3)
                frame += temp
            
            depacketized_frame = _rf.depacketize(frame)
            
            _rf.log('status_ok',f'recieved {depacketized_frame} from {_rf.serMAIN.name}')
            _rf.log('warn',f'{_rf.errors[str(_rf.errCODE)]} <{hex(_rf.errCODE)}>')
            
            return depacketized_frame
                
        except Exception as e:
            _rf.log('status_nok',"error recieving frame")
            _rf.log('err',f'{e}')
        
    def reply_callback(_rcb,data):
        pass

def main(args=None):
    rclpy.init(args=args)

    bus_interface = BusInterface(0x26)
    
    nodeExecutor_thread = rclpy.executors.MultiThreadedExecutor()
    nodeExecutor_thread.add_node(bus_interface)
    nodeExecutor_thread = threading.Thread(target=nodeExecutor_thread.spin, daemon=True)
    nodeExecutor_thread.start()
    
    bus_interface.open_serial_ports()
    
    while True:
        cmd_frame = bus_interface.recieve_frame()
        if bus_interface.errCODE == bus_interface.errCMD or bus_interface.errCODE == bus_interface.errDEST:
            pass
        else:
            bus_interface.send_request(cmd_frame["cmd"],cmd_frame["data"])
            while not bus_interface.future.done():
                pass
            try:
                response = bus_interface.future.result()
                rply_frame = bus_interface.packetize(cmd_frame["src"],cmd_frame["dest"],response.cmd,response.data)
                bus_interface.log('info',f'{response}')
                bus_interface.transmit_frame(rply_frame)
            except Exception as e:
                bus_interface.log('status_nok',f'service call <{bus_interface.cli.srv_name}> failed')
                bus_interface.log('err',f'{e}')
            else:
                pass
        
    nodeExecutor_thread.join()

if __name__ == '__main__':
    main()