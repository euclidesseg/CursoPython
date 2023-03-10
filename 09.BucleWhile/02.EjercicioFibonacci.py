# IMPRIMIR LA SUCESION FIBONACCI DESDE EL NUMERO 0 HASTA EL 1597 
# CON RECOMENDACION DE NO ECCEDER LAS 7 LINEAS DE CODIGO

a = 0; b = 1; c = a;
while(a < 1597):
    a = a + c;
    c = b;
    b = a;
    print(f'{a}')
print('fin')
