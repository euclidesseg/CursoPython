'''
Supongamos que tenemos una aplicaciÃ³n para gestionar tareas pendientes de un equipo de trabajo.
Para ello, debemos crear una lista de tareas y asignarlas a los distintos miembros del equipo.

Crear una lista vacÃ­a llamada tareas_pendientes.
Crear un diccionario vacÃ­o llamado miembro_equipo que tendrÃ¡ como 
claves el nombre de los miembros del equipo y como valores una lista 
vacÃ­a para almacenar las tareas asignadas a cada uno.
Solicitar al usuario que ingrese una tarea nueva. 

La tarea debe incluir: una descripciÃ³n, la fecha de vencimiento y el miembro del equipo asignado.
Verificar si el miembro del equipo ya estÃ¡ en el diccionario. 
Si no lo estÃ¡, agregarlo y asignarle la tarea. Si ya estÃ¡, agregar la tarea a la lista correspondiente.
Agregar la tarea a la lista de tareas_pendientes.
Mostrar la lista de tareas_pendientes ordenada por fecha de vencimiento.

Solicitar al usuario que ingrese el nombre de un miembro del equipo para mostrar sus tareas asignadas.
Buscar en el diccionario miembro_equipo la lista de tareas correspondiente al miembro 
ingresado y mostrarla en pantalla.
Solicitar al usuario que ingrese el nombre de una tarea para marcarla como completada.

Buscar la tarea en la lista de tareas_pendientes y eliminarla.
Buscar la tarea en todas las listas del diccionario miembro_equipo y eliminarla si estÃ¡ presente.
Mostrar la lista de tareas_pendientes actualizada y la lista de tareas asignadas al miembro del equipo correspondiente actualizada
'''
tareas_pendientes = []
tareas_completadas = []
miembros_equipo = []

id_tarea = 0

print('* ***************** *')
print('*                   *')
print('* GESTION DE TAREAS *')
print('*                   *')
print('* ***************** *\n')

print('* ********* *')
print('* ACCIONES  *')
print('* ********* *\n')

while True:
    print('1: INGRESAR TAREA NUEVA')
    print('2: MOSTRAR TAREAS POR MIEMBRO DE EQUIPO')
    print('3: MOSTRAR TAREAS PENDIENTES')
    print('4: MOSTRAR TAREAS COMPLETADAS')
    print('5: ELIMINAR TAREA')
    print('6: ACTUALIZAR ESTADO Y FECHA DE TAREA')
    print('0: ABANDONAR Y SALIR\n')
    
    accion = int(input('POR FAVOR ESCOJA UNA ACCIÓN: '))
    
    if accion == 1:
        # Creamos la tarea
        tarea = {}
        tarea["id"] = id_tarea
        tarea["descripcion"] = input('POR FAVOR INGRESE UNA DESCRIPCIÓN PARA LA TAREA: ')
        tarea["fechaVencimiento"] = input('POR FAVOR INGRESE LA FECHA DE VENCIMIENTO DE LA TAREA: ')
        tarea["estado"] = int(input('POR FAVOR INGRESE EL ESTADO DE LA TAREA (1: COMPLETADA, 0: INCOMPLETA): '))
        tarea["nombre_miembro"] = input('POR FAVOR INGRESE EL NOMBRE AL CUAL ASIGNARÁ LA TAREA: ')
        
        id_tarea += 1
        
        miembro_existente = False
        
        # Verificamos si el miembro de equipo ya existe en la lista
        for miembro in miembros_equipo:
            if miembro["nombre"] == tarea["nombre_miembro"]:
                miembro["tasks"].append(tarea["id"])
                miembro_existente = True
                break
        
        # Si no existe el miembro, lo creamos y asignamos la tarea
        if not miembro_existente:
            miembro_nuevo = {"nombre": tarea["nombre_miembro"], "tasks": [tarea["id"]]}
            miembros_equipo.append(miembro_nuevo)
        
        tareas_pendientes.append(tarea)
        print(f'{miembros_equipo}\n')
        print(f'Tareas Pendientes: {tareas_pendientes}\n')
    
    elif accion == 2:
        nombre_miembro = input("Ingrese el nombre del usuario que desea Buscar\n")
        for miembro in miembros_equipo:
            if(miembro["nombre"] == nombre_miembro):
                print(f'Tareas asignadas al miembro {nombre_miembro}\n')
                print(miembro["tasks"])
            else:
                print("Este miemro no existe")
    
    elif accion == 3:
        print(f'Tareas pendientes\n {tareas_pendientes}')
    
    elif accion == 4: 
        print(f'Tareas Completadas\n {tareas_completadas}')
    
    elif accion == 5:
        id = int(input("Por favor ingrese el id de la tarea que desea eliminar"))
        for tarea in tareas_completadas:
            if(tarea["id"] == id):
                tareas_completadas.remove(tarea)
                print("Se ha eliminado la tarea")
                print("la tarea fur eliminada de tareas completadas")
            else:print("la tarea no se encontro en tareas completadas")
        for tarea in tareas_pendientes:
            if(tarea["id"] == id):
                tareas_pendientes.remove(tarea)
                print("Se ha eliminado de tareas pendientes")
            else: print("No se encontro en tareas pendientes") 
            
    elif accion == 6:
        id = int(input("Ingrese el id de la tarea que desea editar\n"))
        print("Solo podra editar las tareas pendientes\n")
        for tarea in tareas_pendientes:
           if(tarea["id"] == id):
              tarea["fechaVencimiento"] = input('POR FAVOR INGRESE LA FECHA DE VENCIMIENTO DE LA TAREA: ')
              tarea["estado"] = int(input('POR FAVOR INGRESE EL ESTADO DE LA TAREA (1: COMPLETADA, 0: INCOMPLETA): '))
              if(tarea["estado"] == 1):
                  tareas_completadas.append(tarea)
              else: pass
        else:
            print("tarea no encontrada \n")   
    
    elif accion == 0:
        print('HAS ESCOGIDO 0, EL PROGRAMA TERMINÓ')
        break
    
    else:
        print('FIN')