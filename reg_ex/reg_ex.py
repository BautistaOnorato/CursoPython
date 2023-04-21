import re

texto = '''Primera linea de texto 1.
Segunda linea de texto 2.
Segunda linea de texto 2.
Segunda linea de texto 222.
Segunda linea de texto 2.
Tercera linea de texto 3.
'''
# Haciendo una busqueda simple
resultado = re.findall("linea", texto)

# Busca digitos numericos del 0 al 9

resultado = re.findall(r"\d", texto)

# Busca digitos que no vayan del 0 al 9

resultado = re.findall(r"\D", texto)

# Busca alfanumericos [a-z A-Z 0-9 _]

resultado = re.findall(r"\w", texto)

# Busca todo menos alfanumericos [a-z A-Z 0-9 _]

resultado = re.findall(r"\W", texto)

# busca espacios en blancos -> espacios, tabs, \n

resultado = re.findall(r"\s", texto)

# busca todo menos espacios en blancos -> espacios, tabs, \n

resultado = re.findall(r"\S", texto)

# busca todo menos \n

resultado = re.findall(r".", texto)

# busca \n

resultado = re.findall(r"\n", texto)

# cancela el caracter especial y busca un valor especifico

resultado = re.findall(r"\.", texto)

# armando una cadena que busque un numero, seguido de un punto y seguido de un espacio

resultado = re.findall(r"\d\.\s", texto)

# busca el comienzo de una linea

resultado = re.findall(r"^Segunda", texto, flags=re.M)

# busca el final de una linea

resultado = re.findall(r".$", texto, flags=re.M)

# busca {x} veces el valor de la izquierda

resultado = re.findall(r"\d{3}", texto)

# {n,m} al menos n max m

resultado = re.findall(r"\d{1,2}", texto)

# busca una cosa o la otra

resultado = re.findall(r"\d{3}|Primera", texto)

print(resultado)