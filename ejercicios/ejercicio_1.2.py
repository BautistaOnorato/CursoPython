texto_usuario = input("Ingrese un texto: ")
cant_palabras = len(texto_usuario.split(" "))
tiempo_de_diccion_promedio = cant_palabras / 2
tiempo_de_diccion_dalto = cant_palabras / 2 * 0.3

print(f'Tardaste {tiempo_de_diccion_promedio} segundos en decir {cant_palabras} palabras')
print(f'Dalto tardaria {tiempo_de_diccion_dalto} segundos')
if tiempo_de_diccion_promedio > 60:
  print("Para flaco tampoco te pedí un testamento")
  