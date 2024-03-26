#Clases 

class MyEmptyPerson:
    pass

print (MyEmptyPerson)
print (MyEmptyPerson())

class Person:
    def __init__(self, name, surname, edad): #Para parametrizar los datos, self es obligatorio
        self.name = name
        self.surname = surname
        self.edad = edad

my_person = Person ("Leydi", "Franco", 33) # con esto nombro una variable para asignarle datos al parametro de la clase q inicie, y luego lo imprimo
print(f"{my_person.name} {my_person.surname} {my_person.edad}")
