# EN ESTE CAPITULO APRENDEREMOS A INVERTIR LOS ELEMENTOS DE UNALISTA USANDO EL METODO reverse()
# ESTE METODO MODIFICA LAS POCISIOES DE LA LISTA
# ES DECIR EL PRIMER ELEMENTO SE CONVERTIRA AN EN EL ULTIMOP ELEMENTO DE LA LISTA Y ASI SUCESIVAMENTE
# SINTAXIS:
'''
nombre_lista.reverse()
'''

jugadores = ['Crsitiano', 'Messi', 'Ramos', 'Ronaldiño', 'Benzema',]
jugadoresRever = []
print(F'Lista original \n {jugadores}')

# invertir la lista
jugadores.reverse()
print(f'Lista invertida con reverse() \n {jugadores}')

for i in range(len(jugadores)-1, -1, -1):
    jugador = jugadores[i]
    jugadoresRever.append(jugador)


print(f' \n Lista invertida nuevamente con la clase range \n {jugadoresRever}')