frutas = ["pera", "manzana", "naranja", "limon"]
text = "Hola como andas?"
numeros = [10, 5, 8, 6]

print('----------------')  

for fruta in frutas:
  if fruta == "pera":
    continue
  print(f'Me voy a comer un/a: {fruta}')
  
print('----------------')  

for fruta in frutas:
  if fruta == "naranja":
    print(f'Me comi un/a {fruta} y me cayo mal. No sigo')
    break
  print(f'Me voy a comer un/a: {fruta}')
  
print('----------------')

for caracter in text:
  print(caracter)
  
print('----------------')  

numeros_duplicados = [x*2 for x in numeros]

print(numeros_duplicados)