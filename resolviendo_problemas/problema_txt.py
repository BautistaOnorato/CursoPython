nombres = ["Juan", "Pedro", "Camila", "Matias", "Marteeeeen"]
apellidos = ["Justo", "Perez", "Gonzales", "Flores", "Pa ler mo"]

with open("resolviendo_problemas\\nombres_y_apellidos.txt", "w", encoding='UTF-8') as archivo:
  archivo.writelines("Los datos son:\n\n")
  [archivo.writelines(f"{n} {a}\n") for n,a in zip(nombres, apellidos)]