'''
- Utiliza la estrategia de divide y vencerás
- Basicamente se trata de tener un problema, este problema se va dividiendo en subproblemas
y asi sucesivamente hasta que quedan problemas muy faciles de resolver y asi resolver
el problema original

1. Dividir el array a la mitad
2. llamar al algoritmo recursivamente4
3. mezclar cada mitad ordenada en una sola matriz ordenada

CASO BASE: si la lista tiene 1 solo elemento
'''

def ordenamientoPorMezcla(lista):
    print('Dividir', lista)

    if len(lista) > 1:
        #lista = 5 elementos
        mitad = len(lista)//2 #mitad = 3
        mitadIzq = lista[:mitad] #guarda los primeros 3 elementos 
        mitadDer = lista[mitad:]

        #llamamos recursivamente a la funcion ordenamientoPorMezcla
        ordenamientoPorMezcla(mitadIzq) #ordena la primera mitad
        ordenamientoPorMezcla(mitadDer) #ordenar la segunda mitad

        mezclar(lista, mitadIzq,mitadDer)


def mezclar(arr, mitadIzq, mitadDer):
    indiceIzquierdo = 0
    indiceDerecho = 0
    indiceArr = 0

    #copiar y ordenar los elementos de los arreglos izquierdo y derecho

    while indiceIzquierdo < len(mitadIzq) and indiceDerecho < len(mitadDer):
        print(mitadIzq[indiceIzquierdo], '<' , mitadDer[indiceDerecho])
        if mitadIzq[indiceIzquierdo] < mitadDer[indiceDerecho]:
            arr[indiceArr] = mitadIzq[indiceIzquierdo]
            print(arr)
            indiceIzquierdo = indiceIzquierdo + 1
        else:
            print('Entre al Else')
            arr[indiceArr] = mitadDer[indiceDerecho]
            print(arr)
            indiceDerecho = indiceDerecho + 1
        indiceArr = indiceArr +1

    #Verificar si aun hay elementos en alguna de las dos mitades

    while indiceIzquierdo < len(mitadIzq):
        arr[indiceArr] = mitadIzq[indiceIzquierdo]
        print('@@@',arr)
        indiceIzquierdo = indiceIzquierdo + 1
        indiceArr = indiceArr + 1

    while indiceDerecho < len(mitadDer):
        arr[indiceArr] = mitadDer[indiceDerecho]
        indiceDerecho = indiceDerecho + 1
        indiceArr = indiceArr + 1


lista = [54,26,93,17,77,31,44,55,20]

ordenamientoPorMezcla(lista)

print(lista)
        

