#ps -ef | grep lego_clock_world | grep -v grep | awk '{print $2}' | xargs sudo kill
#ps -ef | grep music_ | grep -v grep | awk '{print $2}' | xargs sudo kill
#clock stop
/home/pi/jagyeongnu/c/stop_clock_led.sh

#music stop
/home/pi/jagyeongnu/c/stop_music.sh

#alarm stop
/home/pi/jagyeongnu/py/stop_alarm.sh

#time_change stop
/home/pi/jagyeongnu/c/stop_time_change.sh



