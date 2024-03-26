# Loops ### un bucle sirve para pasar por diferentes codigos varias veces 

my_condition = 0 

while my_condition < 10:
    print (my_condition)
    my_condition += 2

print ("La ejecucion continua ")

while my_condition < 20:
    my_condition +=2
    if my_condition == 15:
            print("Mi condicion es 15")
            break
    print(my_condition)

print ("Mi condicion es menor que 20")

# For 

my_list = [35, 24, 62, 52, 30, 30, 17]

for element in my_list:
     print(element)

my_tuple = (33, 1.49, "Leydi", "Franco", "Red")

for element in my_tuple:
     print(element)

my_set = {"Brais", "Moure", 35}

for element in my_set:
     print(element)

my_dict = {"Nombre":"Leydi", "Apellido":"Franco", "Edad":33, 1:"Blue"}

for element in my_dict:
     print(element)
     if element == "Edad":
          break
