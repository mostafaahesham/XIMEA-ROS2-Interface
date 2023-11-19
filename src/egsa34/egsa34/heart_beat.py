import rclpy
from rclpy.node import Node
from rclpy.time import Time
import RPi.GPIO as GPIO
import time
from rclpy.signals import SignalHandlerOptions

class HeartBeat(Node):
    def __init__(_hb):
        super().__init__('heart_beat')
        
        _hb.ledPIN = 18
        _hb.syncPIN = 26
        _hb.STATE = False
        
        GPIO.cleanup()
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(_hb.syncPIN, GPIO.OUT)
        GPIO.setup(_hb.ledPIN, GPIO.OUT)
            
    def timer_callback(_cb):
        _cb.STATE = _cb.STATE ^ True
        GPIO.output(_cb.ledPIN,_cb.STATE)
        GPIO.output(_cb.syncPIN,_cb.STATE)

def main(args=None):
    rclpy.init(args=args)

    heart_beat = HeartBeat()
    
    timer = heart_beat.create_timer(0.5, heart_beat.timer_callback)
    
    rclpy.spin(heart_beat)

    rclpy.shutdown()

if __name__ == '__main__':
    main()