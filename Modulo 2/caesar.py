import sys
from typing import DefaultDict

while True:
    #VERIFICAR ARGUMENTO
    if len(sys.argv)>2 or len(sys.argv)==1 or int(sys.argv[1])<1:
        print('ERROR')
        break

    #INICIO DE CÓDIGO
    else:
        key=int(sys.argv[1])
        
        #ABECEDARIO
        abc=list('abcdefghijklmnopqrstuvwxyz')
        ABC=list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')

        #PEDIR PALABRA ORIGINAL
        plaintext=list(input('plaintext: '))

        #CAMBIO DE LETRA
        ciphertext=[]
        for letra in plaintext:
            try:
                #LETRA EN MINÚSCULA
                ubi_abc=abc.index(letra)         
                nueva_ubi=ubi_abc+key

                #SI EL KEY ES MAYOR A 25
                if nueva_ubi>25:
                    div=nueva_ubi//25
                    nueva_ubi=nueva_ubi-25*div-1

                nueva_letra=abc[nueva_ubi]
                ciphertext.append(nueva_letra)

            except:
                try:
                    #LETRA EN MAYÚSCULA
                    ubi_abc=ABC.index(letra)         
                    nueva_ubi=ubi_abc+key

                    #SI EL KEY ES MAYOR A 25
                    if nueva_ubi>25:
                        div=nueva_ubi//25
                        nueva_ubi=nueva_ubi-25*div-1

                    nueva_letra=ABC[nueva_ubi]
                    ciphertext.append(nueva_letra)

                except:
                    ciphertext.append(letra)

        #INTEGRAR ELEMENTOS DE LISTA A STRING
        ciphertext_str=''
        for let in ciphertext:
            ciphertext_str=ciphertext_str+let

        print(f'ciphertext: {ciphertext_str}')

    break
