while True:
    try:
        altura=int(input('Ingrese altura: '))
        if altura>8 or altura<1:
            print('INGRESE VALOR ENTRE 1 Y 8')
            continue
        else:
            frase=' '
            for i in range(1,altura+1):
                print((altura-i)*frase+i*'#')           
            break
    except:
        print('Valor inválido')