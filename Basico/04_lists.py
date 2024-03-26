# lists #

my_list = list ()
my_other_list = []

print (len(my_list))

my_list = [33, 33, 14, 10, 14, 38, 43]

print (my_list) # Imprime la lista 
print (len(my_list)) # Imprime la cantidad de datos de la lista osea 7

my_other_list = [33, 1.45, "Leydi", "Franco"]

print (type (my_list))
print (type (my_other_list))

print (type (my_other_list [-1])) # trae el ultimo valor de la lista osea Franco
print (my_list.count("franco")) # el count cuenta la cantidad de veces q tiene el apellido franco en la lista, trae 0 por q franco esta con minuscula 
print (my_list.count (14)) # Cuenta las veces q tiene 14 mi lista en este caso 2       

age, height, name, surname = my_other_list
print (name) # Imprime el nombre de los datos asignados en my list por la posicion del name 

print(my_list + my_other_list) # Imprime las 2 listas 
print(my_list + my_list) # Imprime las 2 listas 

my_other_list.append ("Gonzalez") # Anade otro dato a la lista iniciar y lo envia al final de la lista 
print (my_other_list)

my_other_list.insert (1, "Azul") # Inserta el dato en la posicion q se le ponga es decir la 1
print (my_other_list)

my_other_list.remove ("Gonzalez") #Elimina el dato q se le pase a eliminar, pero solo elimina uno
print (my_other_list)

my_list.remove (14) #Esta funcion solo elimina un dato de la lista, por ejemplo hay dos veces 14, elimina solo uno 
print (my_list)


my_new_list = my_list.copy()

my_list.clear #Limpia todo lo q traiga la lista, es decir la deja vacia []
print (my_list)# Evidencia q la trae vacia
print (my_new_list) #Copia de nuevo toda la lista de my list

my_new_list.reverse () # pone todos los datos de atras para adelante
print(my_new_list) 