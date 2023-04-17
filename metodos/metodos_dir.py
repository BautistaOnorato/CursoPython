diccionario = {
  'nombre': "Bautista",
  'apellido': "Onorato",
  'edad': 18
}

# devuelve las claves en un objeto iterable
diccionario.keys()

# busca por clave y devuelve el valor
diccionario.get('nombre') # si no lo encuentra devuelve None
diccionario['nombre'] # si no lo encuentra devuelve error

# eliminando un elemento del diccionario
diccionario.pop('apellido')

# obteniendo un objeto iterable
diccionario.items()

# elimina todos los elementos
# diccionario.clear()

resultado = diccionario.items()

print(resultado)