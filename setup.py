#!/usr/bin/env python3

import argparse
import os

parser = argparse.ArgumentParser(description='Install dotfiles')
parser.add_argument('-e', '--editor', choices=['vim', 'nvim', 'both'], dest='editor', default=False)
parser.add_argument('--powerline', '-p', nargs='?', const=True, default=False)
parser.add_argument('--bashrc', '-b', nargs='?', const=True, default=False)
parser.add_argument('--uninstall', nargs='?', const=True, default=False)
args = parser.parse_args()

if (args.uninstall == True):
    os.system('unlink ~/.vim && unlink ~/.config/nvim && unlink ~/powerline-shell && unlink ~/.powerlinerc && unlink ~/.my-bashrc')

if (args.editor == 'vim'):
    os.system('ln -s ~/dotfiles/vim ~/.vim')
    os.system('~/dotfiles/util-scripts/vimplug-installer.py -e vim')

if (args.editor == 'nvim'):
    os.system('ln -s ~/dotfiles/nvim ~/.config/nvim')
    os.system('~/dotfiles/util-scripts/vimplug-installer.py -e nvim')

if (args.editor == 'both'):
    os.system('ln -s ~/dotfiles/vim ~/.vim')
    os.system('~/dotfiles/util-scripts/vimplug-installer.py -e vim')
    os.system('ln -s ~/dotfiles/nvim ~/.config/nvim')
    os.system('~/dotfiles/util-scripts/vimplug-installer.sh -e nvim')

if (args.powerline == True):
    os.system('ln -s ~/dotfiles/powerline-shell ~/powerline-shell')
    os.system('~/powerline-shell/setup.py install')
    os.system('ln -s ~/dotfiles/.powerlinerc ~/.powerlinerc')
    os.system('echo "source ~/.powerlinerc" >> ~/.bashrc')

if (args.bashrc == True):
    os.system('ln -s ~/dotfiles/.my-bashrc ~/.my-bashrc')
    os.system('echo "source ~/.my-bashrc" >> ~/.bashrc')
