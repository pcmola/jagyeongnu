#alarm_hour.py
import RPi.GPIO as GPIO
import time
import os


jong_pwm_pin = 19
jong_dir_pin = 13
book_pwm_pin = 16
book_dir_pin = 12   
jing_pwm_pin = 20
jing_dir_pin =  3


GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(jong_pwm_pin, GPIO.OUT)
GPIO.setup(jong_dir_pin, GPIO.OUT)
GPIO.setup(book_pwm_pin, GPIO.OUT)
GPIO.setup(book_dir_pin, GPIO.OUT)
GPIO.setup(jing_pwm_pin, GPIO.OUT)
GPIO.setup(jing_dir_pin, GPIO.OUT)

jong_pwm_motor = GPIO.PWM(jong_pwm_pin, 500)
jong_pwm_motor.start(0)
book_pwm_motor = GPIO.PWM(book_pwm_pin, 500)
book_pwm_motor.start(0)
jing_pwm_motor = GPIO.PWM(jing_pwm_pin, 500)
jing_pwm_motor.start(0)

def jong_strike():

    GPIO.output(jong_dir_pin, False)
    jong_pwm_motor.ChangeDutyCycle(10) #go(delay)
    time.sleep(0.7) 
    jong_pwm_motor.ChangeDutyCycle(34) #go
    time.sleep(0.13) 
    jong_pwm_motor.ChangeDutyCycle(0)  #stop
    time.sleep(1) 

    GPIO.output(jong_dir_pin, True)
    jong_pwm_motor.ChangeDutyCycle(34) #go(delay)
    time.sleep(0.12) 

    jong_pwm_motor.ChangeDutyCycle(0)  #stop
    time.sleep(1) 
        

def book_strike():

    GPIO.output(book_dir_pin, False)
    book_pwm_motor.ChangeDutyCycle(10) #go(delay)
    time.sleep(0.7) 
    book_pwm_motor.ChangeDutyCycle(34) #go
    time.sleep(0.13) 
    book_pwm_motor.ChangeDutyCycle(0)  #stop
    time.sleep(1) 

    GPIO.output(book_dir_pin, True)
    book_pwm_motor.ChangeDutyCycle(34) #go
    time.sleep(0.12) 

    book_pwm_motor.ChangeDutyCycle(0)  #stop
    time.sleep(1) 
    
    
def jing_strike():

    GPIO.output(jing_dir_pin, False)
    jing_pwm_motor.ChangeDutyCycle(10) #go(delay)
    time.sleep(0.7) 
    jing_pwm_motor.ChangeDutyCycle(34) #go
    time.sleep(0.13) 
    jing_pwm_motor.ChangeDutyCycle(0)  #stop
    time.sleep(1) 

    GPIO.output(jing_dir_pin, True)
    jing_pwm_motor.ChangeDutyCycle(34) #go
    time.sleep(0.12) 

    jing_pwm_motor.ChangeDutyCycle(0)  #stop
    GPIO.output(jong_dir_pin, False)
    time.sleep(1)  



fmt = "%H:%M:%S"
t = time.localtime()
current_time = time.strftime(fmt, t)
hour = int(current_time[0:2])

while True:
    t = time.localtime()
    current_time = time.strftime(fmt, t)
    #if(current_time[0:2] >= "09" and current_time[0:2] <= "22" and (current_time[3:5] == "00" or current_time[3:5] == "30") and current_time[6:8] <= "50"): 
    #if(current_time[0:2] >= "09" and current_time[0:2] <= "18" and (current_time[3:5] == "00" or current_time[3:5] == "30") and current_time[6:8] <= "50"): 
    #if current_time[6:8] <= "50" :
    if(current_time[0:2] >= "09" and current_time[0:2] <= "22" and 
    (current_time[3:5] == "00" or current_time[3:5] == "10" or current_time[3:5] == "20" or current_time[3:5] == "30" or current_time[3:5] == "40" or current_time[3:5] == "50") and 
    current_time[6:8] <= "55"):
        if(current_time[6:8] == "00") :
            os.system("sudo /home/pi/jagyeongnu/hub-ctrl -h 0 -P 2 -p 0")
            time.sleep(1)
            os.system("sudo /home/pi/jagyeongnu/hub-ctrl -h 0 -P 2 -p 1")
        print "Strike!"
    	jong_strike()
    	book_strike()
    	jing_strike()
    time.sleep(1)
    print ("{}".format(current_time))

    
