import pandas as pd

print('Aplicacion de extraccion de datos')
df = pd.read_excel("datos_facturacion.xlsx")
print(df.info)

filtro2_1=df[(df["CVE_CLPV"] >= 1000) & (df["CVE_CLPV"]<=2000)]
print(filtro2_1)
filtro2_1.to_csv("entregable_act2_1.csv")

