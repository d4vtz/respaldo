#! /bin/bash

#Script para bajar el brillo de la pantalla

brillo=$(cat /sys/class/backlight/radeon_bl0/brightness)
brillo=$(expr $brillo - 25)
echo $brillo > /sys/class/backlight/radeon_bl0/brightness
