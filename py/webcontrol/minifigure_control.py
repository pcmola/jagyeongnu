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
    GPIO.output(jong_dir_pin, GPIO.LOW)
    GPIO.pulseRatio(jong_pwm_pin, 0.01); #delay
    webiopi.sleep(0.60)
    GPIO.pulseRatio(jong_pwm_pin, 0.17);
    webiopi.sleep(0.155)

    GPIO.pulseRatio(jong_pwm_pin, 0); #stop   
    webiopi.sleep(0.8)
    
    GPIO.output(jong_dir_pin, GPIO.HIGH)
    GPIO.pulseRatio(jong_pwm_pin, 0.17);    
    webiopi.sleep(0.15)
    
    GPIO.pulseRatio(jong_pwm_pin, 0);

    
@webiopi.macro 
def book_strike():
    webiopi.debug("Book Strike!!!")
    GPIO.output(book_dir_pin, GPIO.LOW)
    GPIO.pulseRatio(book_pwm_pin, 0.01); #delay
    webiopi.sleep(0.60)
    GPIO.pulseRatio(book_pwm_pin, 0.18);
    webiopi.sleep(0.165)
    
    GPIO.pulseRatio(book_pwm_pin, 0); #stop
    webiopi.sleep(0.8)
    
    GPIO.output(book_dir_pin, GPIO.HIGH)
    GPIO.pulseRatio(book_pwm_pin, 0.18);    
    webiopi.sleep(0.16)
    
    GPIO.pulseRatio(book_pwm_pin, 0);
    
    
            
@webiopi.macro
def jing_strike():
    webiopi.debug("Jing Strike!!!")
    GPIO.output(jing_dir_pin, GPIO.LOW)
    GPIO.pulseRatio(jing_pwm_pin, 0.01); #delay
    webiopi.sleep(0.60)
    GPIO.pulseRatio(jing_pwm_pin, 0.17);
    webiopi.sleep(0.155)
    
    GPIO.pulseRatio(jing_pwm_pin, 0); #stop
    webiopi.sleep(0.8)
    
    GPIO.output(jing_dir_pin, GPIO.HIGH)
    GPIO.pulseRatio(jing_pwm_pin, 0.17);    
    webiopi.sleep(0.15)
    
    GPIO.pulseRatio(jing_pwm_pin, 0);
      
    
