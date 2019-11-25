# validating_postal_code

## some testing results
(py37) charm@charm-Aspire-S7-191:~/Documents/validatingpostcode$ python without_if.py 
3456789
False
(py37) charm@charm-Aspire-S7-191:~/Documents/validatingpostcode$ 123455
123455: command not found
(py37) charm@charm-Aspire-S7-191:~/Documents/validatingpostcode$ python without_if.py 
123456
True
(py37) charm@charm-Aspire-S7-191:~/Documents/validatingpostcode$ python without_if.py 
131245
True
(py37) charm@charm-Aspire-S7-191:~/Documents/validatingpostcode$ python without_if.py 
121343
False
(py37) charm@charm-Aspire-S7-191:~/Documents/validatingpostcode$ python without_if.py 
121314
False
(py37) charm@charm-Aspire-S7-191:~/Documents/validatingpostcode$ python without_if.py 
00022
False
(py37) charm@charm-Aspire-S7-191:~/Documents/validatingpostcode$ python without_if.py 
110000
False
(py37) charm@charm-Aspire-S7-191:~/Documents/validatingpostcode$ python without_if.py 
552523
False
(py37) charm@charm-Aspire-S7-191:~/Documents/validatingpostcode$ python without_if.py 
123
False
(py37) charm@charm-Aspire-S7-191:~/Documents/validatingpostcode$ python without_if.py 
3f3456
False
(py37) charm@charm-Aspire-S7-191:~/Documents/validatingpostcode$ python without_if.py 
asdfgh
False

