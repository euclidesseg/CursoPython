
empanadas = [];
opcion = 1
while(opcion != 0):
    print("1. Ingresar Una Empanada \n")
    print("2. Mostrar todas las empanadas ingresadas \n")
    print("3. Buscar empanada por id \n")
    print("4. Editar una empanada \n")
    print("5. Eliminar una empanada \n")
    print("0. Salir \n")
  
    task = int(input("Ingresa la Opcion popr favor \n"));
    if(task == 1 ):
        empanada = {}
        empanada["id"] = int(input("Ingrese el id de la empanada \n"))
        empanada["nombre"] = input("Ingrese el nombre de la empanada \n")
        empanada["precio"] = float(input("Ingrese el precio de la empanada \n"))
        empanada["popularidad"] = int(input("Ingrese la popularidad de la empanada \n"))
        empanada["fecha v"] = input("Ingrese la fecha de vencimiento de la empanada \n")
        
        empanadas.append(empanada)
        print("Elemento agregado")
    elif(task == 2 ):
        for empanada in empanadas:
            print(empanada)
    elif(task == 3 ):
        empanadaId = int(input("Inngresa el id de la empanada que desea buscar \n"))
        for emapada in empanadas:
            if(empanada["id"] == empanadaId):
               print(empanada)
            else:
                print("Empanada no encontrada \n")
    elif(task == 4 ):
        idEmpanada = int(input("Ingrese el id de la empanda que desea editar \n"))
        for emapada in empanadas:
           if(empanada["id"] == idEmpanada):
              emapada["nombre"] = input("Ingrese el nombre de la empanada")
              emapada["precio"] = float(input("Ingrese el precio de la empanada \n"))
              emapada["popularidad"] = int(input("Ingrese la popularidad de la empanada \n"))
           else:
               print("Empanada no encontrada \n")
    elif(task == 5 ):
        idEmpanada = int(input("Ingrese el id de la empanda que desea eliminar \n"))
        for emapada in empanadas:
           if(empanada["id"] == idEmpanada):
              empanadas.remove(empanada) 
              print("Elemento eliminado")
        else:
            print("Empanada no encontrada \n")   
    elif(task == 0 ):
        opcion = 0
    else:
        print("Opcion Incorrecta")

print("fin")