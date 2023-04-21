def sumar_dos():
  while True:
    a = input("Numero 1: ")
    b = input("Numero 2: ")
    try:
      resultado = float(a) + float(b)
    except Exception as e:
      print("Ingrese un número en vez de un texto")
      print(f"{type(e).__name__}: {e}")
    else:
      break
    finally:
      print("Finally")
  return resultado

print(sumar_dos())