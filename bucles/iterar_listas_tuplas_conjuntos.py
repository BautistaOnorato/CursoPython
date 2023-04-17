animales = ["perro", "gato", "cocodrilo", "loro"]
numeros = (1, 2, 3, 4)
resultado = 0

print('----------------')  

for animal in animales:
  print(f'ahora la variable es igual a: {animal}')
  
print('----------------')  
  
for numero in numeros:
  resultado += numero

for numero, animal in zip(animales, numeros):
  print(f'numero: {numero}, animal: {animal}')
  
print('----------------')
  
for numero in range(5,10):
  print(numero)
  
print('----------------')  
  
for num in enumerate(numeros):
  print(f'el indice es: {num[0]} y el valor es: {num[1]}')
  
print('----------------')  

for num in numeros:
  print(num)
else:
  print("el bucle termino")

# print(resultado)