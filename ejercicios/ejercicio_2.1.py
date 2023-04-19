def llenar_lista_compañeros(lista, cantidad = 5):
  for i in range(cantidad):
    compañero = {
      'nombre': "",
      'edad': ""
    }
    
    compañero["nombre"] = input("Ingresar nombre: ")
    compañero["edad"] = int(input("Ingresar edad: "))
    
    lista.append(compañero)
    
  lista = sorted(lista, key=lambda item: item['edad'])
  return lista

compañeros = llenar_lista_compañeros([], 3)
asistente = compañeros[0]
profesor = compañeros[-1]

frase = f"El asistente es {asistente['nombre']} de {asistente['edad']} años y el profesor es {profesor['nombre']} de {profesor['edad']} años"

print(frase)