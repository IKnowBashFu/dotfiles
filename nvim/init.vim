if &compatible
  set nocompatible
endif

set runtimepath+=~/.config/nvim

call plug#begin(expand('~/.config/nvim/plugged'))

Plug 'SirVer/ultisnips'
Plug 'scrooloose/nerdtree'
Plug 'ervandew/supertab'

" Auto-complete shit
Plug 'Shougo/deoplete.nvim', {'do': ':UpdateRemotePlugins'}
Plug 'zchee/deoplete-go', {'do': 'make'}
Plug 'zchee/deoplete-clang'
Plug 'othree/jspc.vim'
Plug 'zchee/deoplete-jedi'

" NodeJS Autocomplete
Plug 'ternjs/tern_for_vim', {'for': ['javascript', 'javascript.jsx']}
Plug 'carlitux/deoplete-ternjs', {'for': ['javascript', 'javascript.jsx']}
Plug 'othree/jspc.vim', {'for': ['javascript', 'javascript.jsx']}

call plug#end()

filetype plugin indent on
syntax enable

set t_Co=256
set tabstop=4
set softtabstop=4
set shiftwidth=4
set noexpandtab
colorscheme hydrangea

" No shitty undo
nnoremap U :echo " < < ===== C H E C K C A P S L O C K ===== > > "<CR>


" autocmd vimenter * NERDTree
map <C-n> :NERDTreeToggle<CR>
autocmd bufenter * if (winnr("$") == 1 && exists("b:NERDTree") && b:NERDTree.isTabTree()) | q | endif

set backspace=2
" set mouse=


" Set Up UltiSnips
let g:UltiSnipsJumpForwardTrigger="<c-b>"
let g:UltiSnipsJumpBackwardTrigger="<c-z>"
let g:UltiSnipsEditSplit="vertical"
let g:UltiSnipsSnippetDirectories=["UltiSnips"]

" Enable Deoplete
let g:deoplete#enable_at_startup = 1

" Tern Config
let g:deoplete#omni#functions = {}
let g:deoplete#omni#functions.javascript = ['tern#Complete', 'jspc#omni']
let g:deoplete#sources#ternjs#case_insensitive = 1
set completeopt=longest,menuone
let g:deoplete#sources = {}
let g:deoplete#sources['javascript.jsx'] = ['file', 'ultisnips', 'ternjs']
let g:tern#command = ['tern']
let g:tern#arguments = ['--persistent']


let g:deoplete#sources#go#gocode_binary = '/home/bashfu/Code/go/bin/gocode'
let g:deoplete#sources#clang#libclang_path = '/usr/lib/llvm-4.0/lib/libclang.so'
let g:deoplete#sources#clang#clang_header = '/usr/lib/llvm-4.0/lib/clang'

" SuperTab
autocmd FileType javascript let g:SuperTabDefaultCompletionType = "<c-x><c-o>"
let g:UltiSnipsExpandTrigger="<C-j>"
inoremap <expr><TAB>  pumvisible() ? "\<C-n>" : "\<TAB>"
