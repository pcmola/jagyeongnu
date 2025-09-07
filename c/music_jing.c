#include <stdio.h>
#include <wiringPi.h>
//#define JING_PIN 11
#define JING_PIN 20

int main(void)
{
   
    if (wiringPiSetupGpio() == -1) {
        return 1;
    }

    pinMode(JING_PIN, OUTPUT);
    digitalWrite(JING_PIN, LOW);
    
    while(1) {
        if (digitalRead (JING_PIN) == HIGH) {
            printf("Jing, strike!!\n");
            system("omxplayer /home/pi/jagyeongnu/c/jing.mp3");
        }
        usleep(1000);
    }
    return 0; 
}


