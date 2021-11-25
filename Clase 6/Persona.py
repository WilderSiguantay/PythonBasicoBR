class Persona:
    nombre = ''
    def inicializar(self, nom):
        self.nombre = nom

    def imprimir(self):
        print('Nombre', self.nombre)


#bloque principal

persona1 = Persona()
persona1.inicializar('Wilder')
persona1.imprimir()
print('El nombre de persona1 es: ', persona1.nombre)

persona2 = Persona()
persona2.inicializar('Karen')
persona2.imprimir()

persona3 = Persona()
persona3.inicializar('Javier')
persona3.imprimir()





