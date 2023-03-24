'''
Considere los objetos siguientes:
- Animal
- Mamífero
- Ovíparo
- Pollo
- Gato
- Ornitorrinco
Describa las relaciones entre los diferentes objetos. El diagrama asociado se llama diagrama de clases.
Dar un ejemplo de descripción algorítmica de las clases asociadas (únicamente la declaración de clase XXX).
¿Es posible implementar estos objetos en Python?
'''

#SUPERCLASE/CLASE MADRE:
class Animal:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    def nombre(self):
        return 'NOMBRE: ' + self.nombre
    def edad(self):
        return 'EDAD: ' + str(self.edad)

#SUBCLASE/CLASE HIJA:
class Mamifero(Animal):
    def __init__(self, nombre, edad, tipo):
        super().__init__(nombre, edad)
        self.tipo = tipo
    def tipo(self):
        return self.tipo

class Gato(Mamifero):
    def __init__(self, nombre, edad):
        super().__init__(nombre, edad, 'mamífero')
        self.animal = 'gato'
    def __str__(self):
        return self.nombre + ' es un ' + self.animal + ' ' + self.tipo + ' de ' + str(self.edad) + ' años.'

class Oviparo(Animal):
    def __init__(self, nombre, edad, tipo):
        super().__init__(nombre, edad)
        self.tipo = tipo
    def tipo(self):
        return self.tipo

class Pollo(Oviparo):
    def __init__(self, nombre, edad):
        super().__init__(nombre, edad, 'ovíparo')
        self.animal = 'pollo'
    def __str__(self):
        return self.nombre + ' es un ' + self.animal + ' ' + self.tipo + ' de ' + str(self.edad) + ' años.'

class Ornitorrinco(Mamifero):
    def __init__(self, nombre, edad):
        super().__init__(nombre, edad, 'mamífero')
        self.animal = 'ornitorrinco'
    def __str__(self):
        return self.nombre + ' es un ' + self.animal + ' ' + self.tipo + 'y ovíparo de ' + str(self.edad) + ' años.'
#PROGRAMA PRINCIPAL:
gato1 = Gato('Sebastian', 5)
print(gato1)

pollo1 = Pollo('Piolín', 2)
print(pollo1)

ornitorrinco1 = Ornitorrinco('Perry', 1)
print(ornitorrinco1)
