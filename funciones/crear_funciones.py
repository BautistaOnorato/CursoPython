def saludar(nombre, apellido = "Gomez" ):
  print(f"Hola {nombre} {apellido} como andas?")
  
saludar("Juan", "Perez")

def crear_contrasena_random(num):
  lista_char = "abcdefjhijklmnopqrstuvwxyz"
  num_entero = str(num)
  num = int(num_entero[0])
  c1 = num - 2
  c2 = num
  c3 = num - 5
  contrasena = f'{lista_char[c1]}{lista_char[c2]}{lista_char[c3]}{num * 2}'
  return contrasena
  
contrasena = crear_contrasena_random(2)

print(contrasena)