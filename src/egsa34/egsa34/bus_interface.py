import rclpy
from rclpy.node import Node
from rclpy.signals import SignalHandlerOptions

import serial
from serial import SerialException
import sys
import os
import time
import threading

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
        
        _bus._allow_undeclared_parameters = True
        
        _bus.namespace = _bus.get_namespace()
        _bus.ns = _bus.namespace[1:]
        
        _bus.declare_parameters(
            namespace=_bus.namespace,
            parameters=[
                (f'uart_config.ports.{_bus.ns}', ""),
                ('uart_config.baud_rate', 0),
                ('uart_config.parity', ""),
                ('uart_config.timeout', 0.0),
                ('services.cmd_srv',"")
            ])
        _bus.portUART = _bus.get_parameter(f'{_bus.namespace}.uart_config.ports.{_bus.ns}').value
        _bus.baudRATE = _bus.get_parameter(f'{_bus.namespace}.uart_config.baud_rate').value
        _bus.PARITY = _bus.get_parameter(f'{_bus.namespace}.uart_config.parity').value 
        _bus.TIMEOUT = _bus.get_parameter(f'{_bus.namespace}.uart_config.timeout').value
        
        _bus.cmd_service_name = _bus.get_parameter(f'{_bus.namespace}.services.cmd_srv').value
        
        _bus.addr = addr
        _bus.SER = None
        
        _bus.log('info',f'subsystem <{hex(_bus.addr)}> up and running')
        
        _bus.log('warn',f'{_bus.portUART}')
        
        
        _bus.bus_client = _bus.create_client(BusReply, _bus.cmd_service_name)       
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
        
    def open_serial_port(_osp):
        try:
            _osp.SER = serial.Serial(port=_osp.portUART, baudrate=_osp.baudRATE, parity=_osp.PARITY, timeout=_osp.TIMEOUT)
            _osp.log('status_ok',f'successfully opened comm port {_osp.SER.name}')
        except SerialException as e:
            
            _osp.sysERR_CODE = list(_osp.sys_errors.keys())[list(_osp.sys_errors.values()).index(f'SYS_PORT{_osp.ns[-1]}_ERR')]

            _osp.log('status_nok',f"couldn't open comm port {_osp.portUART}")
            _osp.log('err',f'{e}')
            
            _osp.log('warn',f'SSP err_status -> {_osp.ssp_errors[str(_osp.sspERR_CODE)]} <{hex(_osp.sspERR_CODE)}>')
            _osp.log('warn',f'SYS err_status -> {_osp.sys_errors[str(_osp.sysERR_CODE)]} <{hex(_osp.sysERR_CODE)}>')
            
    def transmit_frame(_tf,frame):
        try:
            while _tf.SER.out_waiting:
                pass
            
            _tf.SER.write(bytearray(frame))
            
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
            # _tf.log('status_ok',f"reply -> {detailed_debug} on {_tf.SER.name}")
            
            # debug = ' '.join(['{:02X}'.format(byte) for byte in frame])
            # _tf.log('status_ok',f"reply -> {debug}")
            
        except SerialException as e:
            _tf.log('status_nok',"error transmitting frame")
            _tf.log('err',f'{e}')
            
            _tf.sysERR_CODE = _tf.errTX
            
            _tf.log('warn',f'SSP err_status -> {_tf.ssp_errors[str(_tf.sspERR_CODE)]} <{hex(_tf.sspERR_CODE)}>')
            _tf.log('warn',f'SYS err_status -> {_tf.sys_errors[str(_tf.sysERR_CODE)]} <{hex(_tf.sysERR_CODE)}>')
    
    def recieve_frame(_rf):
        frame = b''
        try:
            while not _rf.SER.in_waiting:
                pass
        
            while _rf.SER.in_waiting:
                temp = _rf.SER.read(5)
                
                assert temp[_rf.idxSTART_FLAG] == _rf.FLAG, _rf.errFRAME
                assert temp[_rf.idxDEST_ADDR] == _rf.addr, _rf.errDEST
                assert temp[_rf.idxCMD_ID] in _rf.allowed_CMDS, _rf.errCMD
                
                
                data_length = temp[-1]
                frame += temp
                temp = _rf.SER.read(data_length + 3)
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
            # _rf.log('status_ok',f'recieved {detailed_debug} from {_rf.SER.name}')
            
            # debug = ' '.join(['{:02X}'.format(byte) for byte in frame])
            # _rf.log('status_ok',f"recieved -> {debug}")
            
            return True , depacketized_frame
        
        except AssertionError as e:
            _rf.log('status_nok',"ssp frame error")
            _rf.log('err',f'{e}')
            
            _rf.sspERR_CODE = e.args[0]
            
            _rf.log('warn',f'SSP err_status -> {_rf.ssp_errors[str(_rf.sspERR_CODE)]} <{hex(_rf.sspERR_CODE)}>')
            _rf.log('warn',f'SYS err_status -> {_rf.sys_errors[str(_rf.sysERR_CODE)]} <{hex(_rf.sysERR_CODE)}>')
            
            return False, {}
                
        except SerialException as e:
            _rf.log('status_nok',"error recieving frame")
            _rf.log('err',f'{e}')
            
            _rf.sysERR_CODE = _rf.errRX
            
            _rf.log('warn',f'SSP err_status -> {_rf.ssp_errors[str(_rf.sspERR_CODE)]} <{hex(_rf.sspERR_CODE)}>')
            _rf.log('warn',f'SYS err_status -> {_rf.sys_errors[str(_rf.sysERR_CODE)]} <{hex(_rf.sysERR_CODE)}>')
            
            return False, {}
            
    def standby(_sb):
        while True:
            # _sb.log('',"listening for commands...")
            reception_status, cmd_frame = _sb.recieve_frame()
            if _sb.sspERR_CODE == _sb.errDEST or _sb.sspERR_CODE == _sb.errFRAME or reception_status == False:
                pass
            else:
                try:
                    _sb.send_request(cmd_frame["cmd"],cmd_frame["data"])
                    while not _sb.future.done():
                        pass
                    try:
                        response = _sb.future.result()
                        rply_frame = _sb.packetize(cmd_frame["src"],cmd_frame["dest"],response.cmd,response.data)
                        _sb.transmit_frame(rply_frame)
                        # _sb.log('info',f'{response}')
                    except Exception as e:
                        _sb.log('status_nok',f'service request <{_sb.bus_client.srv_name}> failed')
                        _sb.log('err',f'{e}')
                    else:
                        pass
                except Exception as e:
                    _sb.log('status_nok',f'service response <{_sb.bus_client.srv_name}> failed')
                    _sb.log('err',f'{e}')
                    
                    _sb.log('warn',f'SSP err_status -> {_sb.ssp_errors[str(_sb.sspERR_CODE)]} <{hex(_sb.sspERR_CODE)}>')
                    _sb.log('warn',f'SYS err_status -> {_sb.sys_errors[str(_sb.sysERR_CODE)]} <{hex(_sb.sysERR_CODE)}>')
        

def main(args=None):
    rclpy.init(args=args,signal_handler_options=SignalHandlerOptions.NO)

    bus_interface = BusInterface(0x26)
    
    nodeExecutor_thread = rclpy.executors.MultiThreadedExecutor()
    nodeExecutor_thread.add_node(bus_interface)
    nodeExecutor_thread = threading.Thread(target=nodeExecutor_thread.spin, daemon=True)
    nodeExecutor_thread.start()
    
    bus_interface.open_serial_port()
    bus_interface.standby()
        
    nodeExecutor_thread.join()

if __name__ == '__main__':
    main()