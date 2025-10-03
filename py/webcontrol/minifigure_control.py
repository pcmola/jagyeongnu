#minifigure_control.py
import webiopi

#import sys
#sys.path.append('/home/pi/jagyeongnu/py/python-omxplayer-wrapper-develop')
#sys.path.append('/usr/local/lib/python2.7/dist-packages/decorator-4.0.10-py2.7.egg')
#from omxplayer import OMXPlayer

webiopi.setDebug()

GPIO = webiopi.GPIO

jong_pwm_pin = 19
jong_dir_pin = 13
book_pwm_pin = 16
book_dir_pin = 12
jing_pwm_pin = 20
jing_dir_pin =  3

def setup():
    webiopi.debug("Script with macros - Setup")
    GPIO.setFunction(jong_pwm_pin, GPIO.PWM)
    GPIO.setFunction(jong_dir_pin, GPIO.OUT)
    GPIO.pulseRatio(jong_pwm_pin, 0);
    GPIO.output(jong_dir_pin, GPIO.LOW)    

    GPIO.setFunction(book_pwm_pin, GPIO.PWM)
    GPIO.setFunction(book_dir_pin, GPIO.OUT)
    GPIO.pulseRatio(book_pwm_pin, 0);
    GPIO.output(book_dir_pin, GPIO.LOW)
        
    GPIO.setFunction(jing_pwm_pin, GPIO.PWM)
    GPIO.setFunction(jing_dir_pin, GPIO.OUT)
    GPIO.pulseRatio(jing_pwm_pin, 0)
    GPIO.output(jing_dir_pin, GPIO.LOW)
    
def loop():
    webiopi.sleep(1)

def destroy():
    webiopi.debug("Script with macros - Destroy")
    GPIO.pulseRatio(jong_pwm_pin, 0);
    GPIO.output(jong_dir_pin, GPIO.LOW)    
    
    GPIO.pulseRatio(book_pwm_pin, 0);
    GPIO.output(book_dir_pin, GPIO.LOW) 
    
    GPIO.pulseRatio(jing_pwm_pin, 0)
    GPIO.output(jing_dir_pin, GPIO.LOW)


@webiopi.macro
def jong_strike():
    webiopi.debug("Jong Strike!!!")

    # Forward
    GPIO.output(jong_dir_pin, GPIO.LOW)
    GPIO.pulseRatio(jong_pwm_pin, 0.001)  # kick
    webiopi.sleep(0.55)
    GPIO.pulseRatio(jong_pwm_pin, 0.20)  # mid
    webiopi.sleep(0.10)
    GPIO.pulseRatio(jong_pwm_pin, 0.10)  # run
    webiopi.sleep(0.12)
    GPIO.pulseRatio(jong_pwm_pin, 0.00)  # stop   
    webiopi.sleep(0.8)
    
    # Reverse
    GPIO.output(jong_dir_pin, GPIO.HIGH)
    GPIO.pulseRatio(jong_pwm_pin, 0.01)  # kick 
    webiopi.sleep(0.01)
    GPIO.pulseRatio(jong_pwm_pin, 0.20)  # mid  
    webiopi.sleep(0.10)
    GPIO.pulseRatio(jong_pwm_pin, 0.10)  # run  
    webiopi.sleep(0.10)    
    GPIO.pulseRatio(jong_pwm_pin, 0.00)  # final stop
    webiopi.sleep(0.5)

    
@webiopi.macro
def book_strike():
    webiopi.debug("Book Strike!!!")
    
    # Forward
    GPIO.output(book_dir_pin, GPIO.LOW)
    GPIO.pulseRatio(book_pwm_pin, 0.001)   # kick
    webiopi.sleep(0.55)
    GPIO.pulseRatio(book_pwm_pin, 0.20)   # mid
    webiopi.sleep(0.13)
    GPIO.pulseRatio(book_pwm_pin, 0.10)   # run
    webiopi.sleep(0.12)
    GPIO.pulseRatio(book_pwm_pin, 0.00)   # stop
    webiopi.sleep(0.8)

    # Reverse
    GPIO.output(book_dir_pin, GPIO.HIGH)
    GPIO.pulseRatio(book_pwm_pin, 0.01)   # kick
    webiopi.sleep(0.01)
    GPIO.pulseRatio(book_pwm_pin, 0.20)   # mid
    webiopi.sleep(0.10)
    GPIO.pulseRatio(book_pwm_pin, 0.10)   # run
    webiopi.sleep(0.12)
    GPIO.pulseRatio(book_pwm_pin, 0.00)   # final stop
    webiopi.sleep(0.5)

    
            
@webiopi.macro
def jing_strike():
    webiopi.debug("Jing Strike!!!")

    # Forward
    GPIO.output(jing_dir_pin, GPIO.LOW)
    GPIO.pulseRatio(jing_pwm_pin, 0.001)  # kick
    webiopi.sleep(0.55)
    GPIO.pulseRatio(jing_pwm_pin, 0.20)  # mid 
    webiopi.sleep(0.11)
    GPIO.pulseRatio(jing_pwm_pin, 0.10)  # run 
    webiopi.sleep(0.12)
    GPIO.pulseRatio(jing_pwm_pin, 0.00)  # stop
    webiopi.sleep(0.8)
    
    # Reverse
    GPIO.output(jing_dir_pin, GPIO.HIGH)
    GPIO.pulseRatio(jing_pwm_pin, 0.01)  # kick   
    webiopi.sleep(0.01)    
    GPIO.pulseRatio(jing_pwm_pin, 0.25)  # mid   
    webiopi.sleep(0.11)    
    GPIO.pulseRatio(jing_pwm_pin, 0.10)  # stop   
    webiopi.sleep(0.12)    
    GPIO.pulseRatio(jing_pwm_pin, 0.00)  # final stop
      
    
