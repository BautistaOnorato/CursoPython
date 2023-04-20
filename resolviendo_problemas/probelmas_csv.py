import pandas as pd

df = pd.read_csv("archivos\\datos.csv")

df['edad'] = df['edad'].astype(str)

# print(type(df['edad'][0]))

df['apellido'].replace("Goméz", "Ramirez", inplace=True)

print(df)

df = df.dropna()
df = df.drop_duplicates()

print(df)

df.to_csv("archivos\\datos.csv")