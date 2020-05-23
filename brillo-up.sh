#! /bin/bash

#Script para subir el brillo de la pantalla

brillo=$(cat /sys/class/backlight/radeon_bl0/brightness)
brillo=$(expr $brillo + 25)
echo $brillo > /sys/class/backlight/radeon_bl0/brightness
