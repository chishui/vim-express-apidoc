==========================
vim-express-apidoc
==========================
vim-express-apidoc is a vim plugin which helps to generate a [apidoc](http://apidocjs.com/) format  
API annotaion if your REST API stack is node+express+apidoc.  
# Requirements
- Python 2.7  

# Installation
```
$ git clone https://github.com/chishui/vim-express-apidoc.git
$ cp vim-express-apidoc/* ~/.vim/plugin
```
# Usage
In vim, put cursor in REST API definition line like:
```
router.get('/users/1', function(req, res, next)) {
```
Type in command ``AddDoc`` or map ``F1`` to this command as you like
```
nmap<F1> :AddDoc<CR>
```
# Comment
This project is used for my convenience, so it's not flexible and only Javascript usage.
