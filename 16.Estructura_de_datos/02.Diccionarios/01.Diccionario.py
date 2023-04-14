'''
EN PYTHON UN DICCIONARIO ES UNA ESTRUCTURA DE DATOS QUE SE UTILIZA PARA ALMACENAR UN CONJUNTO
DE ELEMENTOS NO ORDENADOS Y AL IGUAL QUE LAS LISTAS PUEDEN SER HOMOGENEOS O HERTEROGENEOS 
DESPUES DE CREADOS SU CONTENIDO SE PUEDE MODIFICAR SU SINTAXIS ES LA SIGUIENTE

nombre_diccionario = {"id" : elemento, "nombre" : euclides}

EN PYTHON AL IGUAL QUE OTROS LENGUAJES CADA ELEMENTO DE UN DICCIONARIO DEBE TENER UNA CLAVE DIFERENTE
PUEDEN SER IGUALES SUS VALORES MAS NO SUS CLAVES
'''
'''
EN PYTON TAMBIEN PODEMOS CREAR LISTAS Y DICCIONAIOS DENTRO DE UN DICCIONARIO
NOTA: TAMBIEN PODEMOS CREAR DICCIONARIO DENTRO DE LISTAS
'''


alumno = {"id" : 1,
          "nombre" : 'Eudlides',
          "materias" : ["programacion", "Calculo", "Fisica"],
          "universidad" : {"nombre" : "TDA",
                           "direccion" : "calle 72"
                           }
          }

print(f'Este alumno tiene los datos\nid {alumno["id"]}, \nnombre {alumno["nombre"]}')

# Imprimiendo las materias del alumno
print(f'\nmaterias{alumno["materias"]}')

# Imprimiendo la universidad del alumno
print(f'\nuniversidad {alumno["universidad"] ["nombre"]}')

# Modificando un dato del diccionario
alumno["universidad"] ["nombre"] = 'ITM'
print(f'\nuniversidad {alumno["universidad"] ["nombre"]}')

alumno.