def suma(nombre, *numeros):
  return sum(numeros), nombre

resulatdo, nombre = suma("Juan", 10, 5, 15, 8, 74, 8)

print(resulatdo, nombre)