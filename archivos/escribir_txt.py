with open("./archivos\\texto.txt", 'a', encoding="UTF-8") as archivo:
  # Sobreescribe
  # archivo.write("Escribi en un archivo. Sigue siendo bastante medio pelo.")
 for i in range(5):
   archivo.write(f'Linea {i + 1} agregada.\n')