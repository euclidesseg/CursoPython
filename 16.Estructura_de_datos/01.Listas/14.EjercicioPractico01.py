# DESARROLLAR UN PROGRAMA QUE SOLICITE DESDE TECLADO LA LINGITUD DE UNA LISTA QUE CONTANGA UNICAMENTE 
# DATOS DE TIPO ENTERO MOSTRAR ENPANTALLA LA LISTA DE NUMEROS Y LA SUMA DE TODOS LOS NUMEROS

limite = int(input(' Por favor diga cuantos numeros enteros contendra '))
lista_numerica = []
suma_de_lista = 0

for i in range(limite):
    valor = int(input(f'Ingrese el valor # {i} para la lista \n ' ))
    lista_numerica.append(valor)
    
    
suma_de_lista = sum(lista_numerica)
print(f'La lista obtenida es \n {lista_numerica}')
print(f'la suma de la lista es \n {suma_de_lista}')