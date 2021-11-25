#creacion de una funcion
#Sintaxis para crear un funcion en python
#def nombre_funcion(_parametros||argumentosñ):
    #bloque de codigo\

def funcion1():
    #pass instruccion que puede ser utilizada cuando querramos una sentencia sintacticamente bien
    #pero en realidad no hace nada
    print('Hola Funcion')


#llamar a funcion
funcion1()

#Funcion que recibe un parametro/argumento

def saludar(nombre):
    print('Hola ', nombre , '!')


#llamar a funcion con 1 argumento
saludar('Karen')
saludar('Javier')

#FUNCION CON ARGUMENTOS CLAVE VALOR

def verificar(child1, child2, child3):
    print("El niño mas pequeño es: ", child1)


#llamar a funcion y pasar argumentos clave= valor
verificar("Juan","Luis","Julio")
verificar(child1='Julio', child3='Juan', child2='Luis')


#FUNCION QUE RECIBE DOS PARAMETROS

def concatenarNombre(nombre, apellido):
    print(nombre, " ", apellido)

concatenarNombre("Wilder" , "Siguantay")

print('**************FUNCIONES CON RETORNO***************')

#Funcion sin retorno
def sumar(n1, n2):
    resultado = 0
    resultado = n1 + n2
    print('La suma es: ', resultado)

#llamada a funcion sin retorno
sumar(5,4)

#Funciones con retorno
def sumar(n1, n2):
    resultado = 0
    resultado = n1 + n2
    return resultado

#llamada a funcion con retorno
suma = sumar(9,8)
multiplicacion = suma * 2
print('La suma con retorno es: ' , multiplicacion)


def areaCuadrado(lado):
    return lado**2

areaDeUnCuadrado = areaCuadrado(4)
print('El area del cuadrado es: ' , areaDeUnCuadrado)





