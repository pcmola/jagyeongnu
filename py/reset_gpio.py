import RPi.GPIO as GPIO



# BCM 번호 사용

GPIO.setmode(GPIO.BCM)



# 사용할 수 있는 GPIO 목록

pins = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 

        12, 13, 14, 15, 16, 17, 18, 19, 

        20, 21, 22, 23, 24, 25, 26, 27]



for pin in pins:

    GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_OFF)



print("모든 GPIO 핀 초기화 완료")



GPIO.cleanup()  # 추가적으로 라이브러리 자원 해제


