import rclpy
from rclpy.node import Node
from rclpy.signals import SignalHandlerOptions
import sys
import os
import time
from ximea import xiapi
import ximea
import spidev
import numpy as np
from PIL import Image
import struct

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
        
        _x.bus = 0
        _x.device = 0
        _x.spi = spidev.SpiDev()
        
        _x.spi.open(_x.bus, _x.device)

        # Set SPI speed and mode
        _x.spi.max_speed_hz = 1000000
        _x.spi.mode = 0
        
        _x.temp_counter = 0
        
        _x.image = Image.open('/home/egsa/sdfdsf.PNG')
        
        _x.image_data = np.array(_x.image)[:,:,0]
        _x.log('warn',f'original: {np.shape(_x.image_data)}')
        _x.flat_image_data = _x.image_data.flatten()
        _x.log('warn',f'flat: {np.shape(_x.flat_image_data)}')
        
        _x.chunk_size = 244
        _x.chunks = [_x.flat_image_data[i:i + _x.chunk_size] for i in range(0, len(_x.flat_image_data), _x.chunk_size)]
        
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
        
    def timer_callback(_cb):
        msg = [_cb.temp_counter]
        _cb.log('warn',f'{msg} {_cb.temp_counter}')
        _cb.spi.writebytes(msg)
        _cb.temp_counter += 1
        if _cb.temp_counter > 255:
            _cb.temp_counter = 0
                
def main(args=None):
    rclpy.init(args=args)

    ximea = Ximea()
    
    ximea.log('warn',f'{len(ximea.chunks)}')
    ximea.log('warn',f'sending')
    c = 1
    for chunk in ximea.chunks:
        c_bytes = struct.pack('>I', c)
        chunk_with_counter = c_bytes + bytes(chunk)
        spi_frame = ximea.packetize(ximea.addrPL, ximea.addrRPI, 0, chunk_with_counter)
        # ximea.log('warn', f'frame count: {c_bytes}')
        ximea.spi.writebytes2(spi_frame)
        c += 1
        time.sleep(0.05)
        print("sending")
    ximea.spi.close()
    ximea.log('warn',f'sent')
    
    # timer = ximea.create_timer(0.5, ximea.timer_callback)
        
    rclpy.spin(ximea)

    rclpy.shutdown()

if __name__ == '__main__':
    main()
