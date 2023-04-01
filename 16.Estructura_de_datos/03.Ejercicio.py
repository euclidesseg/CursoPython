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

print('* ***************** *')
print('*                   *')
print('* GESTION DE TAREAS *')
print('*                   *')
print('* ***************** *\n')

tareas__pendientes = []
tareas__completadas = []
todas__las__tareas = []
miembros_equipo = [{"nombre":'', "tasks":[]}]
task = {}
id_tarea = 0

print('* ********* *')
print('* ACCIONES  *')
print('* ********* *\n')

inicio = 1

while(inicio != 0 ):
    print('1: INGREAR TAREA NUEVA')
    print('2: MOSTRAR TAREAS POR MIEMBRO DE EQUIPO')
    print('3: MOSTRAR TAREAS PENDIENTES')
    print('4: MOSTRAR TAREAS COMPLETADAS')
    print('5: ELIMINAR TAREA')
    print('6: ACTUALIZAR TAREA')
    print('0: ABANDONAR Y SALIR\n')
    accion = int(input('POR FAVOR ESCOJE UNA ACCION: '))

    if(accion == 1):
        #Creamos la tarea
        task["id"] = id_tarea
        task["descripcion"] = input('POR FAVOR INGRESE UNA DESCRIPCION PARA LA TAREA:  ')
        task["fechaVencimiento"] = input('POR FAVOR INGRESE LA FECHA DE VENCIMIENTO DE LA TAREA:  ')
        task["estado"] = int(input('POR FAVOR INGRESE EL ESTADO DE LA TAREA 1: COMPLETADA 0 INCOMPLETA:  '))
        task["nombre_miembro"] = input('POR FAVOR INGRESE EL NOMBRE AL CUAL ASIGNARA LA TAREA:\n')        
        
        id_tarea = id_tarea + 1
        for miembro in miembros_equipo:
            if(miembro["nombre"] != task["nombre_miembro"]):
                print('ESTE MIEMBRO DE EQUIPO NO EXISTE SE CREARA Y ASIGNARA TAREA AUTOMATICAMENTE\n')
                miembro_nuevo = {}
                tarea_agregar = []
                miembro_nuevo['nombre'] = task['nombre_miembro']
                tarea_agregar.append(task['id'])
                miembro_nuevo['tasks':[]]
                miembros_equipo.append(miembro_nuevo)
            else:pass
                
        tareas__pendientes.append(task)
        print(f'{miembros_equipo}\n')
        print(f'{tareas__pendientes}\n')
    elif(accion == 2):
        pass
    elif(accion == 3):
        pass
    elif(accion == 4):
        pass
    elif(accion == 5):
        pass
    elif(accion == 6):
        pass
    elif(accion == 0):
        print('HAS ESCOJIDO 0 EL PROGRAMA TERMINO')
        inicio = 0
    else:
        print('POR FAVOR ESCOJE UNA ACCON VALIDA DE LA LISTA DE ACCIONES\n')
print('FIN')
