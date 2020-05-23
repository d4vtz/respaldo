#! /bin/bash

if [ "/bin/cat /sys/class/power_supply/BAT0/capacity" == 15 ]; then
notify-send 'Bateria baja'
fi
