/* time_change.c */
#include <stdio.h>
#include <stdlib.h>
#include <wiringPi.h>
#include <time.h>

#define BUTTON_HOUR    7 // BCM GPIO 4
#define BUTTON_MINUTE 22 // BCM GPIO 6
unsigned char strFormat[3];

int main(void)
{
    time_t timer;
    wiringPiSetup();
    pinMode(BUTTON_HOUR,   INPUT);
    pinMode(BUTTON_MINUTE, INPUT);

    while(1) {
        
        //+1시간
        if(digitalRead(BUTTON_HOUR) == 1) {
            system("sudo date -s \"1 hours\"");
            delay(100);
        }

        if(digitalRead(BUTTON_MINUTE) == 1) {
            time(&timer);
            strftime(strFormat, 3, "%M", localtime(&timer));
    
            //현재시간이 59분이면 -59분
            if(strFormat[0] == '5' && strFormat[1] == '9') {
                system("sudo date -s \"-59 minutes\"");
            }
            //그 외에는 +1분
            else {
                system("sudo date -s \"1 minutes\"");
            }
            delay(100);
        }
        delay(100);
    }
}
