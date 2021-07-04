print('Dada la ecuación ax^2+bx+c=0')

a=float(input('a: '))
b=float(input('b: '))
c=float(input('c: '))

discriminante=b**2-4*a*c

if discriminante==0:
    solucion=-b/(2*a)
    print(f'SOLUCIÓN: {solucion}')
elif discriminante>0:
    solucion1=(-b+(discriminante)**0.5)/(2*a)
    solucion2=(-b-(discriminante)**0.5)/(2*a)
    print(f'SOLUCIÓN 1: {solucion1}')
    print(f'SOLUCIÓN 2: {solucion2}')
else:
    print('ECUACIÓN NO PRESENTA SOLUCIÓN REAL')