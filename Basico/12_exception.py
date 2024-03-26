#Exception handling 

numberOne = 5
numberTwo = 2

numberTwo = 2

try:
    print (numberOne+numberTwo)
    print ("No se ha producido error")
except:
    print ("se ha producido un error ")
else: # Se ejecuta si no se porduce una excepcion, tambien se una finally q siempre se ejecutara si se coloca
    print ("la ejecucion continua correctamente ")