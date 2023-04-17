nombre = "juan"
saludo = "mi nombre es juan"
numero = "123456"

# convierte a mayusculas
nombre.upper()
# convierte a minusculas
nombre.lower()
# coniverte a minusculas y despues cambia la primer letra a mayusculas
nombre.capitalize()
# busca un valor y retorna su inidice si la encuentra y -1 si no
nombre.find("u") # devuelve 1
# igual a find() pero si no encuentra devuelve una excepcion
nombre.index("u")
# verifica si tiene solo numeros
numero.isnumeric()
# verifica si es alfanumerico. Solo letras
nombre.isalpha()
# devuelve cuantas veces encuentra una coincidencia
nombre.count("a")
# devuelve cantidad de caracteres
len(nombre)
# verificar si un string empieza con un caracter especifico
nombre.startswith("j")
# verificar si un string termina con un caracter especifico
nombre.endswith("n")
# remplaza una parte del string por otra
saludo.replace("juan", "marcos")
# separar strigns por el valor pasado. la convierte a list
saludo.split(" ")
resultado = saludo.split(" ")
print(resultado)
