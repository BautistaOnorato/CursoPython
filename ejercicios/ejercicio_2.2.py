def es_primo(num):
  if num <= 1:
    return False
  
  for i in range(2, num):
    if num % i == 0:
      return False
  
  return True

def numeros_primos(num):
  lista_primos = [] 
  for i in range(num):
    if es_primo(i):
      lista_primos.append(i)
  return lista_primos

print(numeros_primos(4))
