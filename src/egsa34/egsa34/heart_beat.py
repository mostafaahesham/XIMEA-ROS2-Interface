import rclpy
from rclpy.node import Node
import RPi.GPIO as GPIO
import time
from rclpy.signals import SignalHandlerOptions

class HeartBeat(Node):
    def __init__(_hb):
        super().__init__('heart_beat')
        
        GPIO.cleanup()
        
        _hb.pin = 17
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(_hb.pin, GPIO.OUT)
            
    def blink(_blnk):
        while True:
            GPIO.output(_blnk.pin, GPIO.HIGH)
            time.sleep(0.2)
            GPIO.output(_blnk.pin, GPIO.LOW)
            time.sleep(1)

def main(args=None):
    rclpy.init(args=args,signal_handler_options=SignalHandlerOptions.NO)

    heart_beat = HeartBeat()
    
    heart_beat.blink()
    
    rclpy.spin(heart_beat)

    rclpy.shutdown()

if __name__ == '__main__':
    main()