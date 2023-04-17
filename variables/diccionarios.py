diccionario_dict = dict(
  nombre = "Juan",
  apelldio = "Gomez",
  edad = 25
)

diccionario = {
  'nombre': "Juan",
  'apellido': "Gomez",
  'edad': 25,
  ("tupla", "tupla2"): "tupla" ,
  frozenset([1, 2]): "conjunto"
}

diccionario_fromkeys = dict.fromkeys(["nombre", "apellido", "edad"], 1)

print(diccionario)
print(diccionario_dict)
print(diccionario_fromkeys)