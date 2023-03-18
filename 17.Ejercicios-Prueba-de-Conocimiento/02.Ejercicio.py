# 
import operator
cuentas = [
    
    ]

for i in range(3):
    cuenta = {}
    cuenta["saldo"] = int(input(f"Ingresa el saldo de la cuenta # {i+1} "))
    cuenta["id"] = i
    cuentas.append(cuenta)
lista2 = cuentas.sort(key = lambda cuenta:cuenta["saldo"], reverse = True)
print(cuentas)
print(lista2)
print("End")