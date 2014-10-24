" initialise all plugins managed by pathogen
execute pathogen#infect()

" enable syntax highlighting
syntax on
filetype plugin indent on

set number
set autochdir
let NERDTreeChDirMode=2
nnoremap <leader>n :NERDTree .<CR>

" set theme
set background=light
colorscheme mustang

autocmd vimenter * if !argc() | NERDTree | endif
map <C-n> :NERDTreeToggle<CR>

" Status Line {  
        set laststatus=2                             " always show statusbar  
        set statusline=  
        set statusline+=%-10.3n\                     " buffer number  
        set statusline+=%f\                          " filename   
        set statusline+=%h%m%r%w                     " status flags  
        set statusline+=\[%{strlen(&ft)?&ft:'none'}] " file type  
        set statusline+=%=                           " right align remainder  
        set statusline+=0x%-8B                       " character value  
        set statusline+=%-14(%l,%c%V%)               " line, character  
        set statusline+=%<%P                         " file position  
"}

" Rainbow Parenthesis {
       au VimEnter * RainbowParenthesesToggle
       au Syntax * RainbowParenthesesLoadRound
       au Syntax * RainbowParenthesesLoadSquare
       au Syntax * RainbowParenthesesLoadBraces
"}
