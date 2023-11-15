import rclpy
from rclpy.node import Node
from rclpy.signals import SignalHandlerOptions
import serial
from serial import SerialException
import sys
import os
import time
import random
import threading
import RPi.GPIO as GPIO

current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(current_dir)

from ssp import SSP
from log_level import LogLevel

class Emulator(Node,SSP,LogLevel):
    def __init__(_emu,addr):
        super().__init__('emulator')
        SSP.__init__(_emu)
        LogLevel.__init__(_emu)
        
        _emu.addr = addr
    
        _emu.uart_port_0 = '/dev/ttyUSB0'
        _emu.uart_port_1 = '/dev/ttyUSB1'
        _emu.baud_rate = 115200
        _emu.parity =  'N'
        _emu.timeout = None
        
        _emu.syncPIN = 26
        _emu.STATE = False
        
        GPIO.cleanup()
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(_emu.syncPIN, GPIO.OUT)
        
        _emu.rand = [random.randint(0,255) for _ in range(248)]
        
        _emu.log('info',f'subsystem <{hex(_emu.addr)}> up and running')
        
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
            _osp.SER0 = serial.Serial(port=_osp.uart_port_0, baudrate=_osp.baud_rate, parity=_osp.parity, timeout=_osp.timeout)
            _osp.log('status_ok',f'successfully opened comm port {_osp.SER0.name}')
        except SerialException as e:
            _osp.sysERR_CODE = _osp.errPORT0
            _osp.log('status_nok',f"couldn't open comm port {_osp.uart_port_0}")
            _osp.log('err',f'{e}')
        try:
            _osp.SER1 = serial.Serial(port=_osp.uart_port_1, baudrate=_osp.baud_rate, parity=_osp.parity, timeout=_osp.timeout)
            _osp.log('status_ok',f'successfully opened comm port {_osp.SER1.name}')
        except SerialException as e:
            _osp.sysERR_CODE = _osp.errPORT1
            _osp.log('status_nok',f"couldn't open comm port {_osp.uart_port_1}")
            _osp.log('err',f'{e}')
    
    def command_send(_cs,ser,dest,src,cmd,data):
        try:
            frame = _cs.packetize(dest,src,cmd,data)
            
            while ser.out_waiting:
                pass
            
            ser.write(frame)
            
            # data_len = frame[_cs.idxDATA_LEN]
            # sent = {
            #     "flag_s":frame[_cs.idxSTART_FLAG],
            #     "dest":frame[_cs.idxDEST_ADDR],
            #     "src":frame[_cs.idxSRC_ADDR],
            #     "cmd":frame[_cs.idxCMD_ID],
            #     "data_len":frame[_cs.idxDATA_LEN],
            #     "data":bytes(frame[_cs.idxDATA_START:_cs.idxDATA_START + data_len]),
            #     "crc_0":frame[_cs.idxCRC_0],
            #     "crc_1":frame[_cs.idxCRC_1],
            #     "flag_e":frame[_cs.idxEND_FLAG],
            # }
            # detailed_debug = {
            #     key: ' '.join([f'{byte:02X}' for byte in value]) if key == 'data' and isinstance(value, bytes) else
            #     f'{value.hex()}' if isinstance(value, bytes) else
            #     f'{value:02X}' if isinstance(value, int) else
            #     str(value)
            #     for key, value in sent.items()
            # }
            # _cs.log('status_ok',f"cmd -> {detailed_debug} on {ser.name}")
            
            debug = ' '.join(['{:02X}'.format(byte) for byte in frame])
            _cs.log('status_ok',f"cmd -> {debug}")
            
        except Exception as e:
            _cs.log('status_nok',"frame not sent")
            _cs.log('err',f'{e}')
            
    def recieve_frame(_rf,ser):
        frame = b''
        try:            
            while not ser.in_waiting:
                pass
        
            while ser.in_waiting:
                temp = ser.read(5)
                frame += temp
                data_length = temp[-1]
                temp = ser.read(data_length + 3)
                frame += temp
                
            depacketized_frame = _rf.depacketize(frame,'r')
            
            # detailed_debug = {
            #     key: ' '.join([f'{byte:02X}' for byte in value]) if key == 'data' and isinstance(value, bytes) else
            #     f'{value.hex()}' if isinstance(value, bytes) else
            #     f'{value:02X}' if isinstance(value, int) else
            #     str(value)
            #     for key, value in depacketized_frame.items()
            # }
            # _rf.log('status_ok',f'recieved {detailed_debug} from {ser.name}')
            
            debug = ' '.join(['{:02X}'.format(byte) for byte in frame])
            _rf.log('status_ok',f"recieved -> {debug} from {ser.name}")
            
            return depacketized_frame
        
        except Exception as e:
            _rf.log('status_nok',"error recieving frame")
            _rf.log('err',f'{e}')
            
    def command_send_callback(_cb):
        # _cb.command_send(_cb.SER0,_cb.addrRPI,0x50,_cb.cmdWD,_cb.rand)
        _cb.command_send(_cb.SER1,_cb.addrRPI,0x01,_cb.cmdSSC,[0xff]*8)
        _cb.log('',"listening for reply...")
        
    def sync_callback(_cb):
        _cb.STATE = _cb.STATE ^ True
        GPIO.output(_cb.syncPIN,_cb.STATE)
        # _cb.log('warn',f'{_cb.STATE}')
        
    def standby_p0(_cb):
        while True:
            _cb.recieve_frame(_cb.SER0)
            
    def standby_p1(_cb): 
        while True:
            _cb.recieve_frame(_cb.SER1)           
            
def main(args=None):
    rclpy.init(args=args,signal_handler_options=SignalHandlerOptions.NO)

    emulator = Emulator(0x50)
    emulator.open_serial_ports()
    
    command_send_timer = emulator.create_timer(5.0, emulator.command_send_callback)
    sync_timer = emulator.create_timer(0.5, emulator.sync_callback)
          
    sb_0 = threading.Thread(target=emulator.standby_p0)
    sb_1 = threading.Thread(target=emulator.standby_p1)
    
    nodeExecutor_thread = rclpy.executors.MultiThreadedExecutor()
    nodeExecutor_thread.add_node(emulator)
    nodeExecutor_thread = threading.Thread(target=nodeExecutor_thread.spin, daemon=True)
    
    nodeExecutor_thread.start()
    sb_0.start()
    sb_1.start()
    
    nodeExecutor_thread.join()
    sb_0.join()
    sb_1.join()

if __name__ == '__main__':
    main()