

def fibonacci(num):
  lista_fibonacci = [0]
  a, b = 0, 1
  for i in range(num):
    if b > num: return lista_fibonacci
    else:
      lista_fibonacci.append(b)
      a, b = b, a + b
  return lista_fibonacci

# print(fibonacci(6))