my_set = set()
my_other_set = {} #inicialmente es un diccieonario

print (type (my_set))
print (type (my_other_set)) #se llama el tipo de dato, como esta es un diccionario 

my_other_set = {"leydi", "Franco ", 33}
print (type (my_other_set)) # Ya se incluyeron los datos en el set con corchetes ahora si es un set

print(len(my_other_set)) # Imprime la cantidad de datos q tiene el set

my_other_set.add("Felipe")

print (my_other_set) #Imprimep todo, pero un set no es una estructura ordenada

my_other_set.add("Felipe") # un set no admite repetidos
print (my_other_set)

my_other_set.add("felipe") # un set no admite repetidos, en este caso lo admite por la minuscula f
print (my_other_set)

my_set = ("Andres", "Cubillos", 32 )
print (my_set)





