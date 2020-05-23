#                                                                            
#        	       Mi configurción de zsh                  
#                          By:CallmeDav 



#		Aplicar esquema de colores de pywal
#################################################################
export TERM=xterm-256color
(/usr/bin/cat /home/medicendav/.cache/wal/sequences &)
source /home/medicendav/.cache/wal/colors-tty.sh

export PATH="${PATH}:${HOME}/.local/bin/"




#	Configurando mi prompt en  ~/.p10k.zsh.
#################################################################

source /home/medicendav/.config/powerlevel10k/powerlevel10k.zsh-theme
[[ ! -f /home/medicendav/.p10k.zsh ]] || source /home/medicendav/.p10k.zsh

if [[ -r "${XDG_CACHE_HOME:-$HOME/.cache}/p10k-instant-prompt-${(%):-%n}.zsh" ]]; then
  source "${XDG_CACHE_HOME:-$HOME/.cache}/p10k-instant-prompt-${(%):-%n}.zsh"
fi





#################################################################
#
#	     Mis funciones
#	     By:CallmeDav

#"""""""""""""""""""""""""""""""""""""""""""""""""
#    -- Crear una carpeta y entrar a ella --
#"""""""""""""""""""""""""""""""""""""""""""""""""

mkcd(){
	mkdir $1
	cd $1
}

#""""""""""""""""""""""""""""""""""""""""""""""""
#  -- Entra a una carpeta y lista su contenido--
#""""""""""""""""""""""""""""""""""""""""""""""""

cl(){
	cd $1
	ls
}

#""""""""""""""""""""""""""""""""""""""""""""""""
#  -- Entra a una carpeta y lista su contenido --
#""""""""""""""""""""""""""""""""""""""""""""""""

script(){
	touch $1.sh && sudo chmod +x $1.sh
	echo '#! /bin/bash' > $1.sh 
    vim $1.sh
}


#""""""""""""""""""""""""""""""""""""""""""""""""
#  --   Remover archivo tm de autoinicio       --
#""""""""""""""""""""""""""""""""""""""""""""""""


rm-tmp() {
        rm $HOME/.config/bspwm/tmp
}
       

#""""""""""""""""""""""""""""""""""""""""""""""""
#  --            Repositorio git               --
#""""""""""""""""""""""""""""""""""""""""""""""""

repo(){
        cd ~/Documentos/.dotfiles
        git add .
        git status
        git commit -m "$*"
        git push -u origin master
}


dotfiles(){
    cd ~/Documentos
    stow --adopt -v .dotfiles
}


virtual(){
	cd Documentos/AprendiendoPython && source venv/bin/activate
}




#       Generando mi historial de comandos
#################################################################

SAVEHIST=1000
HISTFILE=/home/medicendav/.zsh_history






#################################################################
#							
#			  Mis alias			
#			By: CallmeDav


#"""""""""""""""""""""""""""""""""""""""""""""""""""""""""
#            --  lsd Esteroides para mi ls  --
#"""""""""""""""""""""""""""""""""""""""""""""""""""""""""
alias ll='lsd -lha --group-dirs=first'
alias ls='lsd --group-dirs=first'
alias cat='bat --paging=never'


#"""""""""""""""""""""""""""""""""""""""""""""""""""""""""
#		       --  tmux  --
#"""""""""""""""""""""""""""""""""""""""""""""""""""""""""
alias attach='tmux attach'
alias temux='tmux new -s'


#"""""""""""""""""""""""""""""""""""""""""""""""""""""""""
#		     --  Sistema  --
#"""""""""""""""""""""""""""""""""""""""""""""""""""""""""
alias bye='pkill -KILL -u medicendav'
alias rmc='rm -r'
alias cpr='cp-r'
alias class='xprop WM_CLASS'
alias brillo='./.config/scripts/brillo.sh'
alias wpa='sudo wpa_supplicant -B -i wlp2s0 -c /etc/wpa_supplicant/wpa_supplicant-wlp2s0.conf'


alias tard='tar -cvf'
alias untard='tar -xvf'

alias targz='tar -czvf'
alias untargz='tar -xzvf'

alias dotfiles='cd ~/Documentos/.dotfiles'
alias py='python'
alias latex='latexmk -pdf -pvc'
alias nm-editor='sudo nm-connection-editor'
alias virtualpy='source venv/bin/activate'

#"""""""""""""""""""""""""""""""""""""""""""""""""""""""""
#		      --  pacman  --
#"""""""""""""""""""""""""""""""""""""""""""""""""""""""""
alias installer='sudo xbps-install -S'
alias update='sudo xbps-install -Su'
alias find-pack='sudo xbps-query -Rs'
alias remove='sudo xbps-remove -R'





#################################################################
#							
#			  Mis plugins			
#			By: CallmeDav

source /usr/share/zsh/plugins/zsh-autosuggestions/zsh-autosuggestions.zsh
source /usr/share/zsh/plugins/zsh-syntax-highlighting/zsh-syntax-highlighting.zsh

