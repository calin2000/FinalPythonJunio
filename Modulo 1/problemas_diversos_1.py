saldo_inicial=float(input('Ingrese su saldo inicial: '))

anho1=round(saldo_inicial*1.04,2)
anho2=round(saldo_inicial*1.04**2,2)
anho3=round(saldo_inicial*1.04**3,2)


print(f'AHORRO AÑO 1: S/.{anho1}')
print(f'AHORRO AÑO 2: S/.{anho2}')
print(f'AHORRO AÑO 3: S/.{anho3}')