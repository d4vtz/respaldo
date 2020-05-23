#! /bin/bash

agenda=$(echo -e "Modificar algo a la agenda\nBorrar algo de la agenda\n Cerrar " | rofi -dmenu -i -p "Que desea agregar a la agenda?" -location 0 -xoffset -14 -yoffset -52 -width 30 -hide-scrollbar -line-padding 4 -padding 20 -lines 5)

case $agenda in
	'Modificar algo a la agenda' )

            dia=$(rofi -dmenu -i -p "Que dia?" -location 0 -xoffset -30 -yoffset -52 -width 30 -hide-scrollbar -line-padding 4 -padding 20 -lines 5)

            touch ~/Plantillas/notas/$dia.txt
            echo "$dia" > ~/Plantillas/notas/$dia.txt
            gedit ~/Plantillas/notas/$dia.txt ;;

    'Borrar algo de la agenda' )
            var=cat $HOME/Plantillas/notas/.txt
            borrar=$(echo -e "$var" | rofi -dmenu -i -p "Que desea agregar a la agenda?" -location 0 -xoffset -14 -yoffset -52 -width 30 -hide-scrollbar -line-padding 4 -padding 20 -lines 5)
            tilix & ;;


	' Cerrar')
        	exit 0;;

esac