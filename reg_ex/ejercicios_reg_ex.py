import re

# ocultar un numero de telefono de CABA

texto = "Mi numero es +54 11 4587-1234"

reg_ex = r"\+\d{2}\s\d{2}\s\d{4}-\d{4}"

remplazo = re.sub(reg_ex, "+** ****-****", texto) 

print(remplazo)