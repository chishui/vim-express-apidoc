if !has('python')
	finish
endif

python import sys, vim
python if vim.eval('expand("<sfile>:p:h")') not in sys.path: sys.path.append(vim.eval('expand("<sfile>:p:h")'))
python import expressdoc

function! AddExpressDoc()
    python expressdoc.main()
endfunc
 
command! AddDoc call AddExpressDoc()
