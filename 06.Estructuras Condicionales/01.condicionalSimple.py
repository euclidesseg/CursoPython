#  LA SENTENCIA CONDICIONAL SIMPLE Y COMPUESTAIF
#  A LO CONTRARIO DE OTROS LENGUAJES DE PROGRAMACION A LA HORA DE ESTABLESER UNA SENTENCIA IF
#  LA EJECUCION DE SU RESULTADO NO VA ENTRE PARENTESIS SI NO QUE IRA DESPUES DE : DOS PUNTOS 
#  Y OBLIGATORIAMENTE ON INDENTADO DE CODIGO COMO SE MUESTRA A CONTINUACION

if(6 > 8):
    print('Si es mayor que 8');
else: 
    print('No es mayor que 8');
    
print('');
print('Calculemos el dia de la semana');
print('')

diaSemana = int( input('Por favor ingresa un dia para calcular el dia de la semana') );

if(diaSemana == 1 ):
    print('El dia de la semana que ingresastes es lunes');
elif(diaSemana == 2 ):
    print('El dia de la semana que ingresastes es maetes');
elif(diaSemana == 3 ):
    print('El dia de la semana que ingresastes es miercoles');
elif(diaSemana == 4 ):
    print('El dia de la semana que ingresastes es jueves');
elif(diaSemana == 5 ):
    print('El dia de la semana que ingresastes es viernes');
elif(diaSemana == 6 ):
    print('El dia de la semana que ingresastes es sabado');
elif(diaSemana == 7 ):
    print('El dia de la semana que ingresastes es domingo');
else: print('Haz ingresado un numero desconocido');
