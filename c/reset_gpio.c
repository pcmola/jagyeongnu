#include <wiringPi.h>
#include <stdio.h>


int main(void) {
    if (wiringPiSetupGpio() == -1) { // BCM GPIO 번호 사용
        printf("wiringPi 초기화 실패\n");
        return 1;
    }


    // GPIO 2 ~ 27 까지 순환 (라즈베리파이 40핀 헤더의 주요 GPIO)
    for (int pin = 2; pin <= 27; pin++) {
        pinMode(pin, INPUT);           // 입력 모드로 전환
        pullUpDnControl(pin, PUD_OFF); // 풀업/풀다운 해제
    }

    printf("모든 GPIO 핀 초기화 완료\n");
    return 0;
}
