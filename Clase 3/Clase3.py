a = 33
b = 100

if a < b:
    print("A es menor a B")
    print('A es igual a: ' , a)
    print('B es igual a: ' , b)

#IDENTACION EN PYTHON
#Python utiliza la sangria o identacion para indicar un bloque de codigo

print('Bloque 0')
if 5>2:
    #Bloque 1 adentro del bloque 0
    print('5 es mayor a 2')

    #bloque 2 adentro del bloque 0
    if 3 > 2: 
        #Bloque 1 adentro del bloque 2 adentro del bloque 0
        print('Hola desde el bloque 1, del bloque 2 que esta adentro del bloque 0')

    #Bloque 3 adentro del bloque 0
    print("Hola desde el bloque 3 adentro del bloque 0")

#Bloque 1
print('Hola desde el bloque 1')


#ELIF
a = 50
b = 10

if a >b:
    print('A es mayor que B')
elif a == b:
    print('A es igual a B')
elif a < b:
    print('A es menor a B')

print('Salimos de If')

respuesta = a != b
print('#####################')
print(respuesta)


tengoSueno = False

if tengoSueno:
    print('Tengo sueño!')


#ELSE

x = 25
y = 25

if x < y:
    print('X es menor a Y')
elif x > y:
    print('X es mayor a Y')
else:
    print('Y es igual que X')

#OPERADOR AND || OR

'''
El AND FUNCIONA COMO LA MULTIPLICACION
0 * 0 = 0
0 * 1 = 0
1 * 0 = 0
1 * 1 = 1
------------
1 = true
0 = false
------------
'''
x = 20
y = 21
z = 20

print('-----CONDICION AND -----')

condicion1 = x == y
condicion2 = x == z
condicion3 = y == z

print('Condicion 1: ', condicion1, ' Condicion 2: ', condicion2, 'Condicion 3: ', condicion3)

print(x == y and x ==z and y == z)

if x == y and x ==z:
    print('Esta condicion se cumple')
else:
    print('Esta condicion no se cumple')


#CONDICION OR

'''
EL OR FUNCIONA COMO LA SUMA
0 + 0 = 0
0 + 1 = 1
1 + 0 = 1
1 + 1 = 1
------------
1 = true
0 = false
------------
'''

print("****************CONDICION OR****************")


print(x == y or x ==z or y == z)

if x == y or x ==z:
    print('Esta condicion se cumple')
else:
    print('Esta condicion no se cumple')

#IF ANIDADOS

tengoCovid = False
tengoFiebre = False
grados = 40

print("################## EJEMPLO IF ANIDADO ##############")
if tengoCovid:
    print('No salir de casa')
    if tengoFiebre:
        print('Guardar Reposo')
        if grados > 37:
            print('Tomar medicina')
        else:
            print('Temperatura normal')
    else:
        print('Cuidar temperatura')
else: 
    print('Debo cuidarme')
    if tengoFiebre:
        print('Probables sintomas de covid')
        if grados > 37:
            print('Tomar Medicina')
        else:
            print('Temperatura normal')
    else:
        print('Sigue cuidandote')

