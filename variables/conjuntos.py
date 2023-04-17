conjunto = frozenset([1, 2, 3, (4, 5, 6)])
conjunto_anidado = set([1, 2, conjunto])
# print(conjunto_anidado)

# Teoria de conjuntos

conjunto1 = {1,3,5,7}
conjunto2 = {1,3,5}

resultado_subconjunto = conjunto2.issubset(conjunto1)
resultado_superconjunto = conjunto1.issuperset(conjunto2)
verificar_iguales = conjunto1.isdisjoint(conjunto2)

print(resultado_subconjunto, resultado_superconjunto, verificar_iguales)