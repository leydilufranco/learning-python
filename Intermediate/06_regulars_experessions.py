## Expresiones regulares

import re
my_string = "Esta no es mi leccion"

search = re.search("leccion", my_string, re.I)
print (search)
start, end = search.span ()
print(my_string[start:end])