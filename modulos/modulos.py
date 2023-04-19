# import modulo_saludar
# import modulo_saludar as m_saludar
import sys
sys.path.append('c:\\Users\\bauti\\OneDrive\\Escritorio\\pruebas\\python\\funciones')
from modulo_saludar import saludar
from enrutar_modulos.nombres import martin, relato
import crear_funciones as random_pass

saludo = saludar(martin)
print(saludo)

relato(martin)

contrasena = random_pass.crear_contrasena_random(8)
print(contrasena)