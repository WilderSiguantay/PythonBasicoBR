class Person:

    #la funcion Init es el constructor o equivalente a constructor en otros lenguajes 

    #El metodo __init__ es el primer metodo que se ejecuta cuando se crea un objeto
    #se llama automaticamente. 
    #El metodo init puede recibir parametros que se utilizan normalmente para inicilizar atributos
    #de la clase
    #Es opcional, es una buena practica utilizarlo es común en programas python

    def __init__(self, name, age, alt, lugar):
        self.nombre = name
        self.edad = age
        self.altura = alt
        self.ubicacion = lugar

    #OPERACIONES O METODOS DE LA CLASE PERSON
    def presentacion(self):
        print('Hola, mi nombre es: ', self.nombre, ' Mi edad es: ', self.edad, ' y mido: ', self.altura)

    def getUbicacion(self):
        print('Soy de: ', self.ubicacion)

persona1 = Person(age=20,name='Juan', alt='1.80', lugar='Guatemala')
persona2 = Person('Julio', '25', 1.70, 'Guatemala')
persona2.presentacion()

#Modificar propiedades de un objeto
persona1.nombre = 'Jonny'
persona1.presentacion()

#Eliminar la propiedad de un objeto
print(persona1.edad)
del persona1.edad
#print(persona1.edad)

#Eliminar un objeto
del persona1
