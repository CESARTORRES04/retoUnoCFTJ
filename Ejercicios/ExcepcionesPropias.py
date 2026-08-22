#Excepciones personalizadas

class SaldoInsuficienteError(Exception):
    def __init__(self,saldo,monto):
        self.saldo = saldo
        self.monto = monto
        self.falta = saldo - monto
        super().__init__(f"Saldo insuficiente")



saldo = 200
monto = 30

if monto > saldo:
    raise SaldoInsuficienteError(saldo, monto)

print("Retiro realizado")





