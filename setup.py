#!/usr/bin/env python3

import argparse
import os

parser = argparse.ArgumentParser(description='Install dotfiles')
parser.add_argument('-e', '--editor', choices=['vim', 'nvim', 'both'], dest='editor', default=False)
parser.add_argument('--powerline', '-p', nargs='?', const=True, default=False)
parser.add_argument('--bashrc', '-b', nargs='?', const=True, default=False)
args = parser.parse_args()

if (args.editor == 'vim'):
    os.system('ln -s ~/dotfiles/vim ~/.vim')
    os.system('VIM=vim ~/dotfiles/util-scripts/vimplug-installer.sh')

if (args.editor == 'nvim'):
    os.system('ln -s ~/dotfiles/nvim ~/.config/nvim')
    os.system('VIM=nvim ~/dotfiles/util-scripts/vimplug-installer.sh')

if (args.editor == 'both'):
    os.system('ln -s ~/dotfiles/vim ~/.vim')
    os.system('VIM=vim ~/dotfiles/util-scripts/vimplug-installer.sh')
    os.system('ln -s ~/dotfiles/nvim ~/.config/nvim')
    os.system('VIM=nvim ~/dotfiles/util-scripts/vimplug-installer.sh')

if (args.powerline == True):
    os.system('ln -s ~/dotfiles/powerline-shell ~/powerline-shell')
    os.system('~/powerline-shell/setup.py install')
    os.system('ln -s ~/dotfiles/.powerlinerc ~/.powerlinerc')
    os.system('echo "source ~/.powerlinerc" >> ~/.bashrc')

if (args.bashrc == True):
    os.system('ln -s ~/dotfiles/.my-bashrc ~/.my-bashrc')
    os.system('echo "source ~/.my-bashrc" >> ~/.bashrc')
