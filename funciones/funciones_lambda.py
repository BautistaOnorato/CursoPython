numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9]

numeros_pares = filter(lambda numero: numero % 2 == 0, numeros)

print(list(numeros_pares))