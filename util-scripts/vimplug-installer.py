#!/usr/bin/env python3

import argparse
import os

parser = argparse.ArgumentParser(description='Install dotfiles')
parser.add_argument('-e', '--editor', choices=['vim', 'nvim'], dest='editor', default=False)
args = parser.parse_args()

if (args.editor == 'vim'):
    os.system('curl -fLo ~/.vim/autoload/plug.vim --create-dirs https://raw.githubusercontent.com/junegunn/vim-plug/master/plug.vim')

if (args.editor == 'nvim'):
    os.system('curl -fLo ~/.locals/share/nvim/site/autoload/plug.vim --create-dirs https://raw.githubusercontent.com/junegunn/vim-plug/master/plug.vim')
