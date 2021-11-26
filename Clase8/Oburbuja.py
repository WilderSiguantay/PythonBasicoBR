lista = [5,7,9,2,4,3,1,6,8]

for i in range(len(lista)-1): #recorre la lista
    for j in range(len(lista)-1): #nos sirve para comparar los elementos de la lista
        if(lista[j] > lista[j+1]): #lista[indice/posicion]
            #lista[j], lista[j+1] = lista[j+1], lista[j]
            temporal = lista[j]
            lista[j] = lista[j+1]
            lista[j+1] = temporal

    print('Pasada No.: ', i+1, '\n', lista)
print('RESULTADO FINAL',lista)

