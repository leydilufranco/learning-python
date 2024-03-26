my_dict = {}
my_other_dict = {}

print (type(my_dict))
print (type(my_other_dict))

my_other_dict = {"Nombre": "leydi ", "Apellido":"Franco", "Edad": 33, 1:"Python"}

my_dict = {
    "Nombre": "Leydi", 
    "Apellido": "Franco", 
    "Edad": 33, 
    "Lenguages": {"Python", "Selenium"}, 
    1:1.49 
}

print (my_other_dict)
print (my_dict)

print (my_dict["Nombre"])

print (my_dict.items())
print(my_dict.keys())
