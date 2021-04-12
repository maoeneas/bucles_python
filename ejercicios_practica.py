#!/usr/bin/env python
'''
Bucles [Python]
Ejercicios de práctica
---------------------------
Autor: Inove Coding School
Version: 1.2

Descripcion:
Programa creado para poner a prueba los conocimientos
adquiridos durante la clase
'''

__author__ = "Inove Coding School"
__email__ = "alumnos@inove.com.ar"
__version__ = "1.2"


def ej1():
    # Ejercicios con bucles "while"


    # Dado el siguiente "while", complete la condicion
    # para que el "while" itere siempre que <x sea menor a 6>
    # Además, complete la línea de código necesaria para que
    # el valor de "x" incremente "1" en cada iteración

    mio= False
    x = 0
    while mio:    # reemplace "condicion" por lo que crea necesario
        print("Valor de x =", x)
        # Coloque la línea de código para que "X" incremente "1"
    while x < 6:
        print("Valor de x =", x)   
        x +=1

    x = 5
    # Dado el siguiente "while", complete la condicion
    # para que el "while" itere siempre que <x sea mayor o igual a 0>
    # Además, complete la línea de código necesaria para que
    # el valor de "x" decremente "1" en cada iteración

    while x >= 0:   # reemplace "condicion" por lo que crea necesario
        print("Valor de x =", x)
        #     # Coloque la línea de código para que "X" decremente "1"
        x -=1    

def ej2():
    # Ejemplos con bucles "for"

    # Dado la siguiente lista de colores, utilizar "for"
    # para imprimir en pantalla todos los colores
    colores = ['rojo', 'naranja', 'verde', 'azul']
    print("comienza ejercicio 2")
    for color in colores:
        print("para color:",color)

    # Itere el "for" utilizando la lista como parámero
    # y utilizar como elemento del "for" cada color
    # for color ...
    # Itere el "for" utilizando el tamaño de la lista
    # como parámetro y utilizar el índice para acceder a
    # los elementos de la lista
    # for i ...
    for l in colores:
        print("tamaño de la ista es:", len(colores))
        break   
    
    for i in colores:
        print("recorrer indice de la lista:", (len(i)))
        # no tengo idea porque me tira 4,7,4,5 y no 0,1,2,3
        
        # Aca vi como lo resolvio un compañero, le pide a: i que obtenga la cantidad de indices y que liste los colores  
        # for i in range(len(colores)):
        #     print("indice=",i,"color=",colores[i])
        # print("\n")
        
        # NOTA: claro, recorda que para acceder a cada elemento de la lista utilizas los corchetes, al igual que haciamos para 
        # los strings, entonces, cuando haces lista[0] elegis el primer elemento de la lista.
        # en un for, lo que tenes que hacer es:
        # for indice in range(len(colores)):
        # print(colores[indice])
        # entonces, el range toma como argumento dentro de sus parentesis el largo (len) de la lista "colores"
        # de manera que el len(colores) te devuelve el número de elementos dentro de la lista!
        
def ej3():
    # Ejemplos con bucles "for"

    # Dado la siguiente lista de números, utilizar "for"
    # para recorrer toda la lista y realizar la sumatoria de todos los números
    # La sumatoria se deberá ir guardando en la variable "suma"
    numeros = [1, 5, -1, 6, 10, 2, -5]
    suma = 0   # Variable ya inicializada, la suma arranca en cero
    for sumita in numeros:
        suma += sumita 
        print("número = ", sumita, "sumatoria =", suma)

def ej4():
    # Ejercicios con bucles "while"

    x = 0
    print ("ejercicio 4 comenzado")
    # Realizar un bucle "while" cuya condición de continuidad
    # sea que <x sea menor a 10> y que <x sea distinto de 6>
    # Colocar ambas condiciones como condicion del "while" realizando
    while x<10: # --> acá tiene que ser while (x < 10) and (x != 6): y luego el incrementador x += 2
        if x== 6:
            x= x+1    
        print("el valor de x es:", x)
        x= x+1    
    

    # una condición compuesta (utilice el operador "and" o "or" según corresponda)
    # En cada iteracion del bucle debe incrementar el valor de "x" en "2"
    # e imprimir en pantalla el resultado de X (antes de incrementar) con print
    
    # Realice el mismo bucle "while" pero en vez de estar formado por una condición
    # compuesta, que el "while" siga iterando mientras <x sea menos a 10>, y dentro del
    # "while" consultar si <x es igual a 6>, y en ese caso realizar una interrupción del bucle
    # En cada iteracion del bucle debe incrementar el valor de "x" en "2"
    # e imprimir en pantalla el resultado de X (antes de incrementar) con print
    
    # Acá sí tenes que hacer el if x == 6: -->break!
    


def ej5():
    # Ejercicio de secuencias numéricas
    # Pedir por consola dos números que representen el principio y fin de una
    # secuencia numérica.
    # Realizar un bucle "for" que recorra esa secuencia armada con "range"
    # y calcule a sumatoria total de todos los números dentro de esa secuencia
    # Tener en cuenta que "range" no incluye el número de "fin" en su secuencia,
    # sino que va hasta el anterior
    # Imprimir el valor de la sumatoria
    print ("comienza Ejercicio 5")
    inicio = int(input('Ingrese el primero número de la secuencia\n'))
    final = int(input('Ingrese el ultimo número de la secuencia\n'))
    for i in [inicio]:
        print(inicio)

    for d in [final]:
        print(i + d)    
        
    # Aquí el for tendría que usar el range(inicio,fin+1) de la siguiente forma
    # sumatoria = 0
    # for numero in range(inicio,fin+1):
    #     sumatorio += numero
    # print("La sumatoria de los numero ingresados es:", sumatoria)


def ej6():
    # Ejercicio de secuencias numéricas
    # Pedir por consola dos números que representen el principio y fin de una
    # secuencia numérica.
    # Realizar un bucle "for" que recorra esa secuencia armada con "range"
    # y cuante cuantes números son negativos y cuantos números son mayor o igual a cero
    # Tener en cuenta que "range" no incluye el número de "fin" en su secuencia,
    # sino que va hasta el anterior
    print ("comienza Ejercicio 6")
    inicio = int(input('Ingrese el primero número de la secuencia\n'))
    final = int(input('Ingrese el ultimo número de la secuencia\n'))

    for i in range(inicio): # Acá lo arrancaste bien, pero tenes que usar range(inicio,fin+1)
        if (i % 2) == 0: # El condicional tiene que encuestar if (i < 0): --> para los negativos
            print("cant positivos:", i)
        elif (i % 2) == 1: # Este tiene que encuestar if (i >= 0): --> para los numeros mayores o iguales a cero
            print("cant negativos:", i)

if __name__ == '__main__':
    print("Bienvenidos a otra clase de Inove con Python")
    #ej1()
    #ej2()
    #ej3()
    #ej4()
    #ej5()
    ej6()
