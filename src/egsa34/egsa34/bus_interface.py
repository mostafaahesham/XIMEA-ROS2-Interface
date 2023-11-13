import rclpy
from rclpy.node import Node
import serial
from serial import SerialException
import sys
import os
import time
import threading
from rclpy.logging import LoggingSeverity

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
        if _sr.sspERR_CODE:            
            _sr.req.cmd = cmd
            _sr.req.err = _sr.sspERR_CODE
            
        if _sr.sysERR_CODE:
            _sr.req.cmd = cmd
            _sr.req.err = _sr.errOTHER
            
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
        except SerialException as e:
            _osp.sysERR_CODE = _osp.errPORT0
            _osp.log('status_nok',f"couldn't open comm port {_osp.portUART0}")
            _osp.log('err',f'{e}')
        try:
            _osp.SER1 = serial.Serial(port=_osp.portUART1, baudrate=_osp.baudRATE, parity=_osp.PARITY, timeout=_osp.TIMEOUT)
            _osp.log('status_ok',f'successfully opened comm port {_osp.SER1.name}')
        except SerialException as e:
            _osp.sysERR_CODE = _osp.errPORT1
            _osp.log('status_nok',f"couldn't open comm port {_osp.portUART1}")
            _osp.log('err',f'{e}')
            
    def transmit_frame(_tf,frame):
        try:
            while _tf.serMAIN.out_waiting:
                pass
            
            _tf.serMAIN.write(bytearray(frame))
            
            # data_len = frame[_tf.idxDATA_LEN]
            # sent = {
            #     "flag_s":frame[_tf.idxSTART_FLAG],
            #     "dest":frame[_tf.idxDEST_ADDR],
            #     "src":frame[_tf.idxSRC_ADDR],
            #     "cmd":frame[_tf.idxCMD_ID],
            #     "data_len":frame[_tf.idxDATA_LEN],
            #     "data":bytes(frame[_tf.idxDATA_START:_tf.idxDATA_START + data_len]),
            #     "crc_0":frame[_tf.idxCRC_0],
            #     "crc_1":frame[_tf.idxCRC_1],
            #     "flag_e":frame[_tf.idxEND_FLAG],
            # }
            # detailed_debug = {
            #     key: ' '.join([f'{byte:02X}' for byte in value]) if key == 'data' and isinstance(value, bytes) else
            #     f'{value.hex()}' if isinstance(value, bytes) else
            #     f'{value:02X}' if isinstance(value, int) else
            #     str(value)
            #     for key, value in sent.items()
            # }
            # _tf.log('status_ok',f"reply -> {detailed_debug} on {_tf.serMAIN.name}")
            
            debug = ' '.join(['{:02X}'.format(byte) for byte in frame])
            _tf.log('status_ok',f"reply -> {debug}")
            
        except SerialException as e:
            _tf.log('status_nok',"error transmitting frame")
            _tf.log('err',f'{e}')
            
            _tf.sysERR_CODE = _tf.errTX
    
    def recieve_frame(_rf):
        frame = b''
        try:
            while not (_rf.SER0.in_waiting or _rf.SER1.in_waiting):
                pass
            
            if _rf.SER0.in_waiting:
                _rf.serMAIN = _rf.SER0
                
            if _rf.SER1.in_waiting:
                _rf.serMAIN = _rf.SER1
        
            while _rf.serMAIN.in_waiting:
                temp = _rf.serMAIN.read(5)
                
                assert temp[_rf.idxSTART_FLAG] == _rf.FLAG, _rf.errFRAME
                assert temp[_rf.idxDEST_ADDR] == _rf.addr, _rf.errDEST
                assert temp[_rf.idxCMD_ID] in _rf.allowed_CMDS, _rf.errCMD
                
                
                data_length = temp[-1]
                frame += temp
                temp = _rf.serMAIN.read(data_length + 3)
                frame += temp
                
                _rf.sspERR_CODE = 0
                _rf.sysERR_CODE = 0
            
            depacketized_frame = _rf.depacketize(frame)
            
            # detailed_debug = {
            #     key: ' '.join([f'{byte:02X}' for byte in value]) if key == 'data' and isinstance(value, bytes) else
            #     f'{value.hex()}' if isinstance(value, bytes) else
            #     f'{value:02X}' if isinstance(value, int) else
            #     str(value)
            #     for key, value in depacketized_frame.items()
            # }
            # _rf.log('status_ok',f'recieved {detailed_debug} from {_rf.serMAIN.name}')
            
            debug = ' '.join(['{:02X}'.format(byte) for byte in frame])
            _rf.log('status_ok',f"recieved -> {debug}")
            
            _rf.log('warn',f'SSP err_status -> {_rf.ssp_errors[str(_rf.sspERR_CODE)]} <{hex(_rf.sspERR_CODE)}>')
            _rf.log('warn',f'SYS err_status -> {_rf.sys_errors[str(_rf.sysERR_CODE)]} <{hex(_rf.sysERR_CODE)}>')
            
            return True , depacketized_frame
        
        except AssertionError as e:
            _rf.log('status_nok',"ssp frame error")
            _rf.log('err',f'{e}')
            
            _rf.sspERR_CODE = e.args[0]
            
            return False, {}
                
        except SerialException as e:
            _rf.log('status_nok',"error recieving frame")
            _rf.log('err',f'{e}')
            
            _rf.sysERR_CODE = _rf.errRX
            
            return False, {}
            
    def standby(_sb):
        
        _sb.log('',"listening for commands...")
        reception_status, cmd_frame = _sb.recieve_frame()
        if _sb.sspERR_CODE == _sb.errDEST or _sb.sspERR_CODE == _sb.errFRAME or reception_status == False:
            pass
        else:
            _sb.send_request(cmd_frame["cmd"],cmd_frame["data"])
            while not _sb.future.done():
                pass
            try:
                response = _sb.future.result()
                rply_frame = _sb.packetize(cmd_frame["src"],cmd_frame["dest"],response.cmd,response.data)
                _sb.transmit_frame(rply_frame)
                _sb.log('info',f'{response}')
            except Exception as e:
                _sb.log('status_nok',f'service call <{_sb.cli.srv_name}> failed')
                _sb.log('err',f'{e}')
            else:
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
        bus_interface.standby()
        
    nodeExecutor_thread.join()

if __name__ == '__main__':
    main()