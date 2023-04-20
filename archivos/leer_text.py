archivo_sin_leer = open("archivos\\texto.txt", encoding="UTF=8")
# archivo = archivo_sin_leer.read()
# lineas = archivo_sin_leer.readlines()
linea1 = archivo_sin_leer.readline(10)

archivo_sin_leer.close()

archivo_sin_leer = open("archivos\\texto.txt", encoding="UTF=8")

linea1_entera = archivo_sin_leer.readline()

archivo_sin_leer.close()

print(linea1)
print(linea1_entera)