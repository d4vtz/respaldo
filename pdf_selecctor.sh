#!/bin/sh

###   Assign wallpapers directory here   ###

pdf_dir=$HOME/Documentos/Libros/

###   Config   ###

rofi_title="Selecciona el pdf"
rofi_options=(
	-width 25 \
	-location 0 \
	-bw 2 \
	-dmenu -i \
	-p "${rofi_title}" "${rofi_colors}" \
	-lines 10
#	-kb-cancel F7 ##assign key value if desired for rofi toggle menu, must be setup in main config file
)

###   Display menu   ###

typeset -A menu
for file in $(find $pdf_dir -type f -regex '.*\pdf\$'); 
do
	file_name=${file##*/}
	menu[${file_name%%.*}]=$file
done

launch_rofi=(rofi "${rofi_options[@]}")
selection="$(printf '%s\n' "${!menu[@]}" | sort | "${launch_rofi[@]}")"

