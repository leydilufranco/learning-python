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
print (is_anagram("Amor", "Roma"))