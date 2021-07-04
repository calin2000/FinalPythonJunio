def datos_alumno():
    nombre=input('Nombre del alumno: ')
    try:
        nota1=float(input('Ingrese nota 1: '))
        nota2=float(input('Ingrese nota 2: '))
        nota3=float(input('Ingrese nota 3: '))

        if nota1>10 or nota2>10 or nota3>10 or nota1<1 or nota2<1 or nota3<1:
            print('ERROR: LAS NOTAS DEBEN SER DEL 1 AL 10')
            datos_alumno()
        else:
            alumno={
                'nombre': nombre,
                'nota1': nota1,
                'nota2': nota2,
                'nota3': nota3
            }

            return alumno

    except:
        print('ERROR: LAS NOTAS DEBEN SER DEL 1 AL 10')
        datos_alumno()

def aprobado(alumnado):
    aprobados=0
    cant_alumnos=len(alumnado)
    for alumno in alumnado:
        promedio=(alumno['nota1']+alumno['nota2']+alumno['nota3'])/3
        if promedio>=4:
            aprobados+=1
    print(f'NÚMERO DE APROBADOS: {aprobados}')
    print(f'NÚMERO DE DESAPROBADOS: {cant_alumnos-aprobados}')


alumnado=[]
for i in range(2):
    estudiante=datos_alumno()
    alumnado.append(estudiante)

aprobado(alumnado)

cant_alumnos=len(alumnado)
suma=0
for alumno in alumnado:
    suma=suma+alumno['nota1']+alumno['nota2']+alumno['nota3']

print(f'PROMEDIO DEL SALÓN: {suma/cant_alumnos}')





