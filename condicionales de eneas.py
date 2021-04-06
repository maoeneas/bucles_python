#!/usr/bin/env python
'''
Condicionales [Python]
Ejercicios de profundización
---------------------------
Autor: Inove Coding School
Version: 1.3
Descripcion:
Programa creado para que practiquen los conocimietos adquiridos durante la semana
'''

__author__ = "Inove Coding School"
__email__ = "alumnos@inove.com.ar"
__version__ = "1.3"


def ej1():
    print('Ejercicios de práctica con números')

    '''
    Realice un programa que solicite por consola 2 números
    Calcule la diferencia entre ellos e informe por pantalla
    si el resultado es positivo, negativo o cero.
    '''
    print("ingrese el primer numero")
    primer = int(input())
    print("ingrese el segundo numero")
    segundo = int(input())
    resultado= primer-segundo
    if resultado >0:
        print("Es positivo el numero: ",resultado)
    elif resultado<0:
        print("Es negativo el numero: ",resultado)
    else:
        print("el numero que ingresaste es 0")



def ej2():
    print('Ejercicios de práctica con números')

    '''
    Realice un programa que solicite el ingreso de tres números
    enteros, y luego en cada caso informe si el número es par
    o impar.
    Para cada caso imprimir el resultado en pantalla.
    '''
    print("inserte el numero 1 ")
    primer= int(input())
    print("inserte el numero 2 ")
    segundo= int(input())
    print("inserte el numero 3 ")
    tercer= int(input())


    if (primer % 2) == 0:
        print("el primer numero es par")
    else:
        print("el primer numero es IMPAR")
    if (segundo % 2) == 0:    
        print("el segundo numero es par")
    else:     
        print("el segundo numero es impar")
    if (tercer % 2) == 0:    
        print("el tercer numero es par")
    else:   
        print("el tercer numero es impar")


def ej3():
    print('Ejercicios de práctica con números')

    '''
    Realice una calculadora, se ingresará por línea de comando dos números
    Luego se ingresará como tercera entrada al programa el símbolo de la operación
    que se desea ejecutar
    - Suma (+)
    - Resta (-)
    - Multiplicación (*)
    - División (/)
    - Exponente/Potencia (**)
    Se debe efectuar el cálculo correcto según la operación ingresada por consola
    Imprimir en pantalla la operación realizada y el resultado
    '''
    print("ingrese el numero 1 ")
    primer= int(input())
    print("ingrese el numero 2 ")
    segundo= int(input())
    print("""ahora ingrese alguno de estas operaciones: 
    Suma (+)
    Resta (-)
    Multiplicación (*)
    División (/)
    Exponente/Potencia (**)""")
    operacion = str(input())    
    if operacion == "+":
        print("la suma del primer numero y el segundo numero da:", primer + segundo)
    elif operacion == "-":
        print("la resta del primer numero y el segundo numero da:", primer - segundo)
    elif operacion == "*":    
        print("la multiplicacion del primer numero y el segundo numero da:", primer * segundo)
    elif operacion == "/":
        print("la division del primer numero y el segundo numero da:", primer / segundo)
    else: 
        operacion == "**"
        print("La exponenciancion del primer numero y el segundo numero da:", primer ** segundo)

def ej4():
    print('Ejercicios de práctica con cadenas')

    '''
    Realice un programa que solicite por consola 3 palabras cualesquiera
    Luego el programa debe consultar al usuario como quiere ordenar las palabras
    1 - Ordenar por orden alfabético (usando el operador ">")
    2 - Ordenar por cantidad de letras (longitud de la palabra)
    Si se ingresa "1" por consola se deben ordenar las 3 palabras por orden alfabético
    e imprimir en pantalla de la mayor a la menor
    Si se ingresa "2" por consola se deben ordenar las 3 palabras por cantidad de letras
    e imprimir en pantalla de la mayor a la menor
    '''
    print("ingrese la palabra 1") 
    primer= str(input())
    print("ingrese la palabra 2") 
    segunda= str(input())
    print("ingrese la palabra 3") 
    tercera= str(input())
    print(""" elija entre estas opciones tocando 1 o 2:
    1 - Ordenar alfabétticamente.
    2 - (Longitud de palabra)""")
    eleccion= int(input())
    juntas= primer,segunda,tercera

    if eleccion ==1:
        print(sorted(juntas))
    elif eleccion==2:
        print(sorted(juntas,key = len))
    else: 
        print("no eligio nunguna de ellas")

def ej5():
    print('Ejercicios de práctica con números')

    '''
    Realice un programa que solicite ingresar tres valores de temperatura
    De las temperaturas ingresadas por consola determinar:
    1 - ¿Cuáles de ellas es la máxima temperatura ingresada?
    2 - ¿Cuáles de ellas es la mínima temperatura ingresada?
    3 - ¿Cuál es el promedio de las temperaturas ingresadas?
    En cada caso imprimir en pantalla el resultado
    '''
    print("ingrese cantidad de temperatura 1")
    valor_1= float(input())
    print("ingrese cantidad de temperatura 2")
    valor_2= float(input())
    print("ingrese cantidad de temperatura 3")
    valor_3= float(input())
    total= cantidad_1,cantidad_2,cantidad_3 
    print("el maximo es:", max(total))
    print("el minimo es:", min(total))
    promedio= (cantidad_1+cantidad_2+cantidad_3) /3
    print('el promedio es:', promedio)

if __name__ == '__main__':
    print("Ejercicios de práctica")
    ej1()
    #ej2()
    #ej3()
    #ej4()
    #ej5()

