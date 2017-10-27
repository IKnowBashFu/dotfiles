#!/bin/sh
if [ -n "$VIM" ]
then
	if [ "$VIM" == "vim" ]
	then
		curl -fLo ~/.vim/autoload/plug.vim --create-dirs \
			https://raw.githubusercontent.com/junegunn/vim-plug/master/plug.vim
		exit
	elif [ "$VIM" == "nvim" ]
	then
		curl -fLo ~/.local/share/nvim/site/autoload/plug.vim --create-dirs \
			https://raw.githubusercontent.com/junegunn/vim-plug/master/plug.vim
	else
		echo -e "VIM must be set to either vim or nvim\n"
	fi
else
	echo -e "VIM must be set to either vim or nvim\n"
fi
