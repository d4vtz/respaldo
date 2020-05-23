#! /bin/bash

var=$(echo -e "              Bloquear\n            Cerrar Sesión\n             Reiniciar\n              Apagar\n             Cancelar" | rofi -dmenu -i -p "	    Desea salir?" -location 0 -xoffset -14 -yoffset -52 -width 30 -hide-scrollbar -line-padding 4 -padding 20 -lines 5)

case $var in
	' Apagar')
	rm /tmp/bspwm_temporal
	systemctl poweroff ;;

	' Reiniciar')
	systemctl reboot ;;

	' Cerrar Sesión')
	pkill -KILL -u medicendav;;

	' Bloquear')
	i3lock-fancy;;


	' Cancelar')
	exit 0;;

esac
