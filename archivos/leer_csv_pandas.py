import pandas as pd

df = pd.read_csv("archivos\\datos.csv")
df2 = pd.read_csv("archivos\\datos.csv")

nombres = df['nombre']

# ordenando ascendente y descendentemente
df_ordenado_a = df.sort_values("edad")
df_ordenado_d = df.sort_values("edad", ascending=False)

# concatenando data frames
df_concatenado = pd.concat([df, df2])

# primeros x registros y ltimos x registros
primer_registro = df.head(1)
ultimos_tres_registros = df.tail(3)

# obteniendo total de filas y columnas
filas_totales, columnas_totales = df.shape

# datos estadisticos
df_info = df.describe()

# accediendo a un elemento especifico con loc
elemento_especifico = df.loc[3, "edad"]

# accediendo a un elemento especifico con iloc
elemento_especifico_iloc = df.iloc[3, 2]

# accediendo a todas los apellidos
apellidos = df.iloc[:,1]

# accediendo a la fila 3
fila_3 = df.loc[2,:]

# accediendo a filas con edad >= 30

mayor_a_29 = df.loc[df['edad']>=30,:]

print(mayor_a_29)