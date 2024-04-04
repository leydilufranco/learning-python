## phthon package

##https://pypi.org

import numpy
import requests ## se debe instalar con pip install numpy

numpy_array = numpy.array ([33, 21, 62, 52, 23, 23, 12])
print (numpy_array * 2)

response = requests.get ("https://pokeapi.co/api/v2/pokemon?limit=151")
print (response)
print (response.status_code)
print (response.json)