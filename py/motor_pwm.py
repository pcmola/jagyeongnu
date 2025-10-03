import RPi.GPIO as GPIO

import time

 

pwm_pin    = 13

goback_pin = 19

 

GPIO.setmode(GPIO.BCM)

GPIO.setup(pwm_pin,    GPIO.OUT)

GPIO.setup(goback_pin, GPIO.OUT)

 

pwm_motor = GPIO.PWM(pwm_pin, 500)

pwm_motor.start(0)

 

try:

    while True:

       GPIO.output(goback_pin, False)

       pwm_motor.ChangeDutyCycle(0)  #stop

       time.sleep(1) 

       pwm_motor.ChangeDutyCycle(80) #go

       time.sleep(0.11) 

       

       GPIO.output(goback_pin, True)

       pwm_motor.ChangeDutyCycle(0)  #stop

       time.sleep(1) #go

       pwm_motor.ChangeDutyCycle(80) #go

       time.sleep(0.11) #stop

finally:

    print("Cleaning up")

    GPIO.cleanup()

