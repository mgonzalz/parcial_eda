'''
A continuación, construye una aplicación que permita crear los tres tipos de cuentas. El ID tiene que ser un número entero incremental, el nombre del titular puede ser inventado, la fecha de apertura y fecha de vencimiento deben ser aleatorias siendo la fecha de apertura más antigua que la fecha de vencimiento, y el número de cuenta tiene que ser un número aleatorio de 12 dígitos. Cuando las cuentas estén iniciadas a un sueldo inicial de 10.000 €, transferir dinero de unas a otras las cantidades de 2000 €, ingresar 575 € y retirar dinero 78 €. 
'''
from datetime import datetime
class Cuenta:
    def __init__(self, ID, nombre, fecha_apertura, numero_cuenta, saldo):
        self.ID = ID
        self.nombre = nombre
        self.fecha_apertura = fecha_apertura
        self.numero_cuenta = numero_cuenta
        self.saldo = saldo
    def retirar(self, cantidad):
        if cantidad > self.saldo:
            print('No se puede retirar esa cantidad de dinero.')
        else:
            self.saldo -= cantidad
            print('Se ha retirado', cantidad, '€ de la cuenta.')
    def ingresar(self, cantidad):
        self.saldo += cantidad
        print('Se ha ingresado', cantidad, '€ en la cuenta.')
    def transferir(self, cantidad, cuenta):
        if cantidad > self.saldo:
            print('No se puede transferir esa cantidad de dinero.')
        else:
            self.saldo -= cantidad
            cuenta.saldo += cantidad
            print('Se ha transferido', cantidad, '€ a la cuenta', cuenta.ID)
    def __str__(self):
        return 'ID: ' + str(self.ID)
class CuentaPlazoFijo(Cuenta):
    def __init__(self, ID, nombre, fecha_apertura, numero_cuenta, saldo, fecha_vencimiento):
        super().__init__(ID, nombre, fecha_apertura, numero_cuenta, saldo)
        self.fecha_vencimiento = fecha_vencimiento
    def retirar(self, cantidad):
        if cantidad > self.saldo and self.fecha_vencimiento > datetime.now(): #datetime.now() devuelve la fecha
            self.saldo -= cantidad
            self.saldo -= cantidad * 0.05
            print('Se ha retirado', cantidad, '€ de la cuenta.')
        elif cantidad > self.saldo and self.fecha_vencimiento < datetime.now():
            print('No se puede retirar esa cantidad de dinero.')
        else:
            self.saldo -= cantidad
            print('Se ha retirado', cantidad, '€ de la cuenta.')

class CuentaVip(Cuenta):
    def __init__(self, ID, nombre, fecha_apertura, numero_cuenta, saldo, saldo_maximo):
        super().__init__(ID, nombre, fecha_apertura, numero_cuenta, saldo)
        self.saldo_maximo = saldo_maximo
    def retirar(self, cantidad):
        if cantidad > self.saldo and self.saldo - cantidad > self.saldo_maximo:
            print('No se puede retirar esa cantidad de dinero.')
        else:
            self.saldo -= cantidad
            print('Se ha retirado', cantidad, '€ de la cuenta.')


