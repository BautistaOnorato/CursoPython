class MiExcepcion(Exception):
  def __init__(self, err):
    print(f"Error: {err}")
    
try:
  raise MiExcepcion("Burro")
except:
  print("Hola")