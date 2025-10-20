import pandas as pd
import os

datos = {
    'Nombre': ['Alice', 'Bob', 'Charlie'],
    'Edad': [25, 30, 35],
    'Ciudad': ['Nueva York', 'Londres', 'París']
}

df = pd.DataFrame(datos)
print("DataFrame original:\n", df)

csv_file = 'datos.csv'
df.to_csv(csv_file, index=False)
print(f"\nDataFrame guardado en '{csv_file}'.")

if os.path.exists(csv_file):
    df_csv = pd.read_csv(csv_file)
    print(f"\nDataFrame leído desde '{csv_file}':\n", df_csv)

excel_file = 'datos.xlsx'
df.to_excel(excel_file, index=False, sheet_name='Personas')
print(f"\nDataFrame guardado en '{excel_file}' en la hoja 'Personas'.")

if os.path.exists(excel_file):
    df_excel = pd.read_excel(excel_file, sheet_name='Personas')
    print(f"\nDataFrame leído desde '{excel_file}':\n", df_excel)

print("\nColumnas del DataFrame:", df_csv.columns)
print("Edad promedio:", df_csv['Edad'].mean())
print("Personas mayores de 28:\n", df_csv[df_csv['Edad'] > 28])

df_csv['Pais'] = ['USA', 'UK', 'Francia']
df_csv.to_csv('datos_modificados.csv', index=False)
print("\nDataFrame modificado y guardado en 'datos_modificados.csv':\n", df_csv)
