num_card=str(input('Ingrese su número de tarjeta: '))

digitos=len(num_card)

#ALGORITMO DE LUHN
num_card_reverse=num_card[::-1]

lista_dobles=[]
lista_excluidos=[]
for indice,a in enumerate(num_card_reverse):
    if indice!=0 and indice%2!=0:
        a=int(a)
        doble=2*a
        a=str(a)
        lista_dobles.append(doble)
    else:
        a=int(a)
        lista_excluidos.append(a)

suma_digitos=0
for i in lista_dobles:
    i=str(i)
    for cifra in i:
        cifra=int(cifra)
        suma_digitos=suma_digitos+cifra

suma_excluidos=0
for num in lista_excluidos:
    suma_excluidos=suma_excluidos+num

num_validador=suma_digitos+suma_excluidos
num_validador=str(num_validador)

if num_validador[-1]=='0':
    validez=True
    print('VALID')
else:
    validez=False
    print('INVALID')




while validez==True:
    if digitos==15 and num_card[:2] in ['34','37']:
        print('AMEX')

    elif digitos in [13,16] and num_card[0]=='4':
        print('VISA')

    elif digitos==16 and num_card[:2] in ['51','52','53','54','55']:
        print('MASTERCARD')

    else:
        print('INVALID')
    break



