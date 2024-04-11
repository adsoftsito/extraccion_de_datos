import pandas as pd

print('Aplicacion de extraccion de datos')
df = pd.read_csv("inmuebles.csv", encoding = "utf-8")
print(df.head())
