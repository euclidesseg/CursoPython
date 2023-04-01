# DECLARANDO UNA FUNCON LAMBDA

# DECLARACION DE UNA FUNCION TRADICIONAL
"""
Las funciones lambdas solamente son aplicables cuando el retorno tiene solamente una sola linea
despues de los puntos se agrega sin la palabra retorno lo que va a retornar esta funcion,
ya que al ser lambda se tomara implicitamente que algo retorna
"""

"""
las expresiones lambdas no nos permiten agrear los paremetros entre parentesis
las funciones lambdas ademas deben ser una sola linea
"""
saludar = lambda nombre, area: f"Hola {nombre} estas aprendiendo {area}"

# LLAMANDO A LA FUNCION
saludo = saludar("Euclides", "python")
print(saludo)

