

periodoServicio =""
nombreEmpleado = ""
opcion = ""

print("*************************")
print("***CALCULAR VACACIONES***")
print("*************************")

nombreEmpleado = input("POR FAVOR INGRESA LA EL NOMBRE DEL EMPLEADO \n")
print("")

print("POR FAVOR INGRESA UNA OPCION SEGUN EL DEPARTAMENTO \n")
print("1: DEPARTAMENTO DE LOGISTICA")
print("2: DEPARTAMENTO DE ATENCION AL CLIENTE")
print("3: DEPARTAMENTO DE GERENCIA \n")
opcion = input("")

if(opcion == "1"):
    periodoServicio = int(input("POR FAVOR INGRESE LOS AÑOS DE SERVICIO DEL EMPLEADO \n"))
    if(periodoServicio > 1 )  and (periodoServicio <= 2):
        print(f'EL EMPLEADO {nombreEmpleado} OBTIENE 6 DIS DE VACACIONES')
    elif(periodoServicio > 2 ) and (periodoServicio <= 7):
        print(f'EL EMPLEADO {nombreEmpleado} TIENE 10 DIAS DE VACACIONES')
    elif(periodoServicio > 7 ):
        print(f'EL EMPLEADO {nombreEmpleado} TIENE 14 DIAS DE VACACIONES')
    else: print('EL EMPLEADO NO TIENE DERECHO A VACACIONES')
    
elif(opcion == "2"):
    periodoServicio = int(input("POR FAVOR INGRESE LOS AÑOS DE SERVICIO DEL EMPLEADO \n"))
    if(periodoServicio > 1 )  and (periodoServicio <= 2):
        print(f'EL EMPLEADO {nombreEmpleado} OBTIENE 7 DIS DE VACACIONES')
    elif(periodoServicio > 2 ) and (periodoServicio <= 7):
        print(f'EL EMPLEADO {nombreEmpleado} TIENE 12 DIAS DE VACACIONES')
    elif(periodoServicio > 7 ):
        print(f'EL EMPLEADO {nombreEmpleado} TIENE 15 DIAS DE VACACIONES')
    else: print('EL EMPLEADO NO TIENE DERECHO A VACACIONES')

elif(opcion == "3"):
    periodoServicio = int(input("POR FAVOR INGRESE LOS AÑOS DE SERVICIO DEL EMPLEADO \n"))
    if(periodoServicio > 1 )  and (periodoServicio <= 2):
        print(f'EL EMPLEADO {nombreEmpleado} OBTIENE 10 DIS DE VACACIONES')
    elif(periodoServicio > 2 ) and (periodoServicio <= 7):
        print(f'EL EMPLEADO {nombreEmpleado} TIENE 20 DIAS DE VACACIONES')
    elif(periodoServicio > 7 ):
        print(f'EL EMPLEADO {nombreEmpleado} TIENE 30 DIAS DE VACACIONES')
    else: print('EL EMPLEADO NO TIENE DERECHO A VACACIONES')

else: print("NO INGRESO LA OPCION CORRECTA")
