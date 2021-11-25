class miClase:
    #atributos (propiedades/variables) de miClase
    name = 'Mi Clase'
    x = 10
    y = ['Mi', 'Clase']

    #funciones o métodos de MiClase
    def imprimirNombre(name):
        print(name)


#Crear un Objeto con Java
# miClase mc = new miClase() --JAVA

#Crear un Objeto con Python
mc = miClase() #un objeto es la instancia de una clase.
mc2 = miClase() #objeto numero 2
print('El nombre de mi objeto es:', mc.name)
print('El nombre de mi objeto2 es:', mc2.name)

#Modificar atributos de un objeto

mc.name = 'Mi primer objeto'
mc2.name = 'Mi segundo objeto'
print('CAMBIO DE NOMBRE DE OBJETOS')
print('El nombre de mi objeto es:', mc.name)
print('El nombre de mi objeto2 es:', mc2.name)

mc.imprimirNombre()











    
