import sys

codigo=sys.argv[1]

if len(codigo)!=26:
    print('ERROR, INSUFICIENTES CARACTERES')
else:
    cod_minus=codigo.lower()
    cod_mayus=codigo.upper()

    abc_minus='abcdefghijklmnopqrstuvwxyz'
    abc_mayus=abc_minus.upper()

    frase=input('plaintext: ')

    frase_convertida=''
    for caracter in frase:
        try:
            indice=abc_minus.index(caracter)
            letra=cod_minus[indice]
        except:
            try:
                indice=abc_mayus.index(caracter)
                letra=cod_mayus[indice]
            except:
                letra=caracter
        
        frase_convertida=frase_convertida+letra
    
    print(frase_convertida)
