lista = [1, 2, 3, "hola"]
numLista = [True, 10, 3, 56, 23, False, 0.5]

# devuelve la longitud
len(lista)

# agregando con append simialra a push()
lista.append("chau")

# agrgeando unelemento en una posicion especifica
lista.insert(2, "indice 2, elemento 3")

# agregando muchos elementos a una lista
lista.extend([5, 6, [1, 2]])

# eliminamos un elemento especifico
lista.pop(-1)

# eliminamos por valor
lista.remove("hola")

# ordena ascendentemente una lista de numeros
numLista.sort()

# revierte el orden de la lista
numLista.reverse()

# eliminar todo
lista.clear()

resultado = numLista

print(resultado)