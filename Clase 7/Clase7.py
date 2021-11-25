''' 
Clase padre o superclase o clase base
    - subClase o clase derivada

¿Para que nos sirve la herencia?
    - Reutilizar código
    - Agrupar las caracteristicas en comun que tienen los objetos/clases (Propiedades)
    - Agrupar los comportamientos en comun de estos objetos (Metodos/Funciones)
'''

#Vehiculos

from typing import ClassVar


class Vehiculos(): #SuperClase - Clase base - Clase padre

    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self.enMarcha = False
        self.acelera = False
        self.frena = False

    def arrancar(self):
        self.enMarcha = True
    
    def acelerar(self):
        self.acelera = True

    def frenar(self):
        self.frena = True

    def estado(self):
        print('Marca: ', self.marca, '\nModelo: ', self.modelo,
        '\nEn Marcha: ', self.enMarcha, '\nAcelerando: ', self.acelera,
        '\nFrenando: ', self.frena)

#crear objeto vehiculo

automovil = Vehiculos('BMW', 'M3')
automovil2 = Vehiculos('VW', 'Jetta GLI')
automovil.arrancar()
#automovil.estado()
#print("-----AUTOMOVIL 2------")
#automovil2.estado()

#HERENCIA
class Moto(Vehiculos):
    hacerCaballito = 'No estoy haciendo caballito'

    def caballito(self):
        self.hacerCaballito = 'Estoy haciendo un caballito'

    def estado(self):
        print('Marca: ', self.marca, '\nModelo: ', self.modelo,
        '\nEn Marcha: ', self.enMarcha, '\nAcelerando: ', self.acelera,
        '\nFrenando: ', self.frena, '\n', self.hacerCaballito)

motocicleta = Moto('Ducati', 'Panigale V4')
motocicleta.arrancar()
motocicleta.acelerar()
motocicleta.caballito()
#motocicleta.estado()

#CLASE CAMION
class camion(Vehiculos):

    def carga(self,cargar):
        self.cargar = cargar
        if(self.cargar):
            return 'El camion está cargado'
        else:
            return 'El camion no esta cargado'

micamion = camion('Hyundai', 'ASDFLKHJJ')
micamion.arrancar()
#micamion.estado()

estacargando = micamion.carga(True) #guardar en una variable el retorno de la funcion
#print(estacargando) #Imprimir el retorno de la funcion
#print(micamion.carga(True)) #imprimir directamente el retorno de la funcion


#Clase Vehiculos Eléctricos
class Velectricos(Vehiculos):
    #Vehiculos eléctricos
    def __init__(self, marca, modelo):
        super().__init__(marca, modelo)
        self.autonomia = 100 #Autonomía de la bateria
        self.cargando = False

    def cargarEnergia(self):
        self.cargando = True

    def estado(self):
        super().estado()
        print('La autonomia es:',self.autonomia, '\nEstá cargando? ', self.cargando)


#HERENCIA MÚLTIPLE
class biciElectrica( Velectricos, Vehiculos):
    pass

mibiciElec = biciElectrica('BMX', 'Elect')
mibiciElec.arrancar()
mibiciElec.cargarEnergia()
mibiciElec.estado()

'''
PRINCIPIO DE SUSTICION: 
ES SIEMPRE UN/UNA
El objeto que es una subclase siempre será un objato de la superclase.
 --> una motocicleta siempre es un vehiculo
 --> un vehiculo, no siempre es una motocicleta o un camion
'''

#FUNCION IS INSTANCE

'''
Nos indica si un objeto es instancia de una clase determinada,
isinstance, nos devuelve true, si pertenece a una clase en concreto
o false si no pertenece
'''

print(isinstance(mibiciElec, Velectricos))
print(isinstance(micamion, Velectricos))
print(isinstance(micamion, Vehiculos))
