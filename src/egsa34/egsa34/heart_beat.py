import rclpy
from rclpy.node import Node
from rclpy.time import Time
import RPi.GPIO as GPIO
import time
from rclpy.signals import SignalHandlerOptions

class HeartBeat(Node):
    def __init__(_hb):
        super().__init__('heart_beat')
        
        _hb.PIN = 18
        _hb.STATE = False
        GPIO.cleanup()
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(_hb.PIN, GPIO.OUT)
            
    def timer_callback(_cb):
        _cb.STATE = _cb.STATE ^ True
        GPIO.output(_cb.PIN,_cb.STATE)

def main(args=None):
    rclpy.init(args=args)

    heart_beat = HeartBeat()
    
    timer = heart_beat.create_timer(1.0, heart_beat.timer_callback)
    
    rclpy.spin(heart_beat)

    rclpy.shutdown()

if __name__ == '__main__':
    main()