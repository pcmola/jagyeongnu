/* fixed_pattern_test.c

 * 74HC/HCT595 LED 고정 패턴 점등 테스트

 * - 각 자리(시간1, 분10, 분1)를 5초씩 켠 뒤 다음 자리로 이동

 * - 스캔/시간 계산 없음: 하드웨어/전원 문제만 드러남

 */



#include <stdio.h>

#include <wiringPi.h>

#include <wiringShift.h>

#include <unistd.h>



#define DS    0   // wiringPi pin (BCM 17)

#define SHCP  1   // wiringPi pin (BCM 18)

#define STCP  2   // wiringPi pin (BCM 27)



#define GREEN_VCC 8   // wiringPi pin (BCM 2)

#define COLON_VCC 11  // wiringPi pin (BCM 7)



// 공통선 (자리 선택) 예시 — 실제 common[] 정의와 동일

unsigned char common[5] = {

    0b01111111, // 시간 10의 자리 (사용안함)

    0b10111111, // 시간 1의 자리

    0b11011111, // 분 10의 자리

    0b11101111, // 분 1의 자리

    0b11110111  // 콜론 (사용안함)

};



// 숫자 '8' 패턴 (모든 세그먼트 점등)

unsigned char digit1_8 = 0b11111111;  // 앞쪽 바이트

unsigned char digit2_8 = 0b11111000;  // 뒤쪽 바이트



void Latch(void) {

    digitalWrite(STCP, HIGH);

    digitalWrite(STCP, LOW);

}



void output_fixed(unsigned char com) {

    // '8' 고정 표시

    shiftOut(DS, SHCP, LSBFIRST, digit2_8);

    shiftOut(DS, SHCP, LSBFIRST, digit1_8);

    shiftOut(DS, SHCP, LSBFIRST, com);

    Latch();

}



int main(void) {

    wiringPiSetup();



    pinMode(DS, OUTPUT);

    pinMode(SHCP, OUTPUT);

    pinMode(STCP, OUTPUT);



    pinMode(GREEN_VCC, OUTPUT);

    pinMode(COLON_VCC, OUTPUT);

    digitalWrite(GREEN_VCC, LOW);

    digitalWrite(COLON_VCC, LOW);



    printf("=== 고정 패턴 LED 테스트 시작 ===\n");



    while (1) {

        printf("자리1(시간 1의 자리) ON\n");

        output_fixed(common[1]);

        sleep(5);



        printf("자리2(분 10의 자리) ON\n");

        output_fixed(common[2]);

        sleep(5);



        printf("자리3(분 1의 자리) ON\n");

        output_fixed(common[3]);

        sleep(5);

    }

    return 0;

}



