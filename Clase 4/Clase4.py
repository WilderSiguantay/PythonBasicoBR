#Ejemplo FOR

''' 
-Java , C#, C++
for (int i=0; i<10; i++){
    //declaraciones o bloques de codigo
}
'''

#Sintaxis
#for objetoiterativo in secuencia:
    #declaraciones o bloques de codigo

#Pasos para crear el For
#1. for
#2. variable que va a manejar las iteraciones
#3. palabra reservada in
#4. secuencia u objeto a iterar
#5. declaraciones o bloques de codigo

#Iterar variable string
profesor = 'Wilder'

for letra in profesor:
    print(letra)

#Ejemplo con Lista

estudiantes = ['Karen', 'Javier','Lourdes','Juan', 'Gabriel', 'Alex']

for nombre in estudiantes:
    print(nombre)


#FUNCION RANGE()
#Iterar la cantidad de veces que definamos en el rango empezando desde 0

print('----SIN NINGUN LIMITE-----')

for x in range(5):
    print(x)

#Range(limiteInferior, limiteSuperior)
print("CON LIMITE SUPERIOR E INFERIOR")
for x in range(3,5):
    print(x)

#Range(limiteInferior, limiteSuperior, pasoDeIteracion)

print('LIMITE INFERIOR, SUPERIOR Y PASO')
for x in range(2,30,5):
    print(x)

#CICLO WHILE

print("CICLO WHILE")
i = 1

while i < 6:
    print(i)
    i +=1
    
#FUNCION BREAK

j = 1
print('FUNCION BREAK')
while j < 6:
    print(j)
    if j == 3:
        break
    j +=1

print("FUNCION CONTINUE")
i= 0
while i <6:
    i +=1
    if i == 3:
        continue
    print(i)

#SENTENCIA ELSE

print("--------ELSE-------")

i =0
while i<6:
    print(i)
    i+=1
else:
    print("i no es menor a 6, El valor de i es: " , i)



#Else con for
#Ejecutar un bloque de codigo al finalizar la iteracion del ciclo
print("----------ELSE CON FOR------------")
estudiantes = ['Karen', 'Javier','Lourdes','Juan', 'Gabriel', 'Alex']

for nombre in estudiantes:
    print(nombre)
else:
    print('Ya no hay estudiantes que imprimir')


#CICLOS ANIDADOS

#CICLO ANIDADO CON FOR
print('---------CICLO CON FOR ANIDADO----------')

nombres = ['Karen', 'Javier','Lourdes','Juan', 'Gabriel', 'Alex']
apellidos = ["De Leon", "Peñate", "Monroy", "Torcelli", "Hernandez", "Chaclan", "Solares"]

for nombre in nombres:
    for apellido in apellidos:
        print(nombre, " ", apellido)

#CICLO ANIDADO CON WHILE
i =0
j =0

print('-----------WHILE ANIDADOS-------------')

while i<3:
    while j<3:
        print(i,j)
        j += 1
    i +=1
    j = 0