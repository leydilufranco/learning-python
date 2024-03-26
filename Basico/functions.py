
##Funciones 

def my_function ():
    print("Imprime mi primer funcion")

my_function()

def my_function2 (firstdata, seconddata):
    print(firstdata + seconddata)
    
my_function2 (7,8)

def my_function3 (firstdata, seconddata):
    print(firstdata * seconddata)
    
my_function3 ("Leydi",8)
my_function3 (1,7)
my_function2 (8,5)

def cadena (id, nombre, precio = 200):
    print(f"{id} {nombre} {precio}")

cadena ('01', "pera", 300)

def varios_datos (*text): #CUando se coloca el * y la palabra text en la funcion, traera todos los datos q quieras llamar en la funcion
    print (text)

varios_datos ("leydi", "pera", 200)

def varios_datos1 (*texts):
    print (type(texts))
    for text in texts: 
        print(text.upper())

varios_datos1 ("hola", "leydi")