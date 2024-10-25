import pandas as pd


ventas_df = pd.read_csv("datos_de_ventas.csv")

print(ventas_df.head())


print(ventas_df.tail(3))


print(ventas_df.info())


media_cantidad = ventas_df['Cantidad'].mean()
mediana_cantiadad = ventas_df['Cantidad'].mean()
desviacion_cantidad = ventas_df['Cantidad'].std()


print(f"Media de cantidad:{media_cantidad}")
print(f"Mediana de cantidad:{mediana_cantiadad}")
print(f"Desviacion de cantidad: {desviacion_cantidad}")



