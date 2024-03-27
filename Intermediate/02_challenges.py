"""
Escribe un programa que muestre por consola con un print los 
numeros del 1 a 100 (ambos incluidos y con un salto de linea entre cada impresion), 
sustituyendo los siguietnes:
- Multiplos de 3 por la palabra "fizz"
- Multiplo de 5 por la palabra "buzz"
- Multiple de 3 y de 5 a la vez por la palabra "fizzbuzz"
"""

def fizbuzz (): 
    for index in range (1, 101):
        if index % 3 == 0 and index % 5 == 0:
            print ("fizzbuz")
        elif index % 3 == 0:
            print ("fizz")
        elif index % 5 ==0:
            print ("buzz")
        else:
            print(index)


fizbuzz()


"""
Escribe una funcion que reciba (String) y retorne verdadero o falso (bool)
segun sea o no anagramas. 
- Un anagrama consiste en formar una palabra reordenando TODAS las letras de otra 
palabra inicial.
- No hace falta comprobar que ambas plabras existan 
- Dos palabras exactamente iguales no son anagrama

"""

def is_anagram (word_one, word_two):
    if word_one.lower() == word_two.lower():
        return False
    return sorted (word_one.lower()) == sorted(word_two.lower())
print (is_anagram("Omare", "Roma"))

"""
Escribe un programa que imprima los 50 primeros numeros de la sucesion de Fibonacci empezando en 0 
- La serie Fibonacci se compone por una sucesion de numeros en la que el siguiente siempre es la suma de los anteriores
"""

def fibonacci ():
    prev=0 
    next = 1
    
    for index in range (0, 50):
        print (prev)
        fib = prev + next 
        prev = next 
        next = fib

fibonacci()

"""
Es un numero primo?
Escribe un programa que se encargue de comprobar si un numero es primo o no
hecho esto imprime los numeros primos entre 1 y 100
"""

def primos ():

    for number in range (1, 101):

        if number >= 2:
            is_divisible = False 
    
            for index in range (2, number):
                if number % index == 0: 
                    is_divisible = True
                    break
            if not is_divisible: 
                print(number)

primos()

"""
Crea un programa que invierta el orden de una cadena de texto sin usar 
funciones propias del lenguaje que lo haga de forma automatica 
- si le pasamos "hola mundo" nos retorna "odnum aloh"
"""


def reverse (text): 
    text_len = len(text)
    reversed_text = ""

    for index in range (0, len(text)):
        reversed_text += text[text_len -index -1]
    return reversed_text

print (reverse("Hola Mundo"))