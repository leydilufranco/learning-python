# Strings 

my_string = "Mi String"
my_other_string = 'Mi otro String'

print (len(my_string))
print (len(my_other_string))

print (my_string + " " + my_other_string)

#Traer todos los datos de forma simple 
name, surname, age = "leydi", "Franco", 35 

print ("Mi nombre es {} {} y mi edad es {}".format (name, surname, age) ) #Forma 1 con {}
print ("Mi nombre es %s %s y mi edad es %d" % (name, surname, age) ) # Forma 2 con % seguido del tipo de dato q se declaro en la variable 
print ("Mi nombre es" +name + " " + surname + "   y mi edad es " +str (age)) # Es posible pero muy largo y no es buena practica 
print (f"Mi nombre es {name} {surname} y mi edad es {age}")

#Desempaquetado de caracteres

language = "Python"
a, b, c, d, e, f = language # Se sacan las variables de acuerdo a la cantidad de letras q tiene la variable Python 
print (a) #Imprime la letra P
print(b) # Imprimpe la letra y

language_slice = language [0:3] ## Muestra las letras que quieras llamar en este caso traeria Pyt
print (language_slice)


language_slice = language [1:3]
print (language_slice)
language_slice = language [1:]
print (language_slice)
language_slice = language [-2]
print (language_slice)


#Funciones 

print( language.capitalize ())
print( language.upper ())
print( language.count ("t"))
print( language.isnumeric ())
print( language.lower ())
print( language.lower ().isupper())
print( language.startswith ("ph"))



