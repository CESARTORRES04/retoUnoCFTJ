

#Encapsulación 
#Herencia
#Polimorfismo
#Abstracción



#Clase padre
class CuentaBancaria:
    def __init__(self,titular_parametro,numero_cuenta_parametro):
        self.titular = titular_parametro
        self.numero_cuenta = numero_cuenta_parametro
        self.__saldo = 0
    
    #GETTER y SETTER
    #GET y SET
    #Obtener y asignar(establecer)
    @property
    def saldo(self):
        return self.__saldo
    
    @saldo.setter
    def saldo(self, nuevo_saldo):
        self.__saldo = nuevo_saldo
    
    def depositar(self, cantidad):
        if cantidad > 0:
            self.__saldo += cantidad
            print("Se depositaron :",cantidad)
        else:
            print("Cantidad incorrecta")

    def retirar(self, cantidad):
        if cantidad > 0 and cantidad < self.__saldo:
            self.__saldo = self.__saldo - cantidad
            print("Se retiro : ",cantidad)
            print("Y su saldo actual es de : ",self.__saldo)
 
        else:
            print("Cantidad invalida")


#clase hija
class CuentaAhorro(CuentaBancaria):
    def __init__(self, titular_parametro, numero_cuenta_parametro,beneficiario_parametro):
        super().__init__(titular_parametro, numero_cuenta_parametro)
        self.beneficiario = beneficiario_parametro
    
    def calcularIntereses(self):

        return self.saldo * 1.10

class CuentaEmpresarial(CuentaBancaria):
    def __init__(self, titular_parametro, numero_cuenta_parametro):
        super().__init__(titular_parametro, numero_cuenta_parametro)
        self.tipo_cuenta = "Cuenta empresarial nivel 1"

    def validarTipoCuenta(self):
        if self.__saldo > 20000:
            self.tipo_cuenta = "Cuenta empresarial nivel 2"
        else:
            print(self.tipo_cuenta)



    






cuenta_cesar = CuentaAhorro("Cesar Torres","757567765","German Torres")
cuenta_cesar.depositar(2000)
print(cuenta_cesar.calcularIntereses())

