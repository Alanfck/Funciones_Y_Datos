import pandas as pd
import time
import matplotlib.pyplot as plt
from tabulate import tabulate

# Cargar los datos del primer y segundo dataset
start_total_time = time.time()
start_time = time.time()
data1 = pd.read_csv("ts_discography_released.csv")
elapsed_time = time.time() - start_time

print("Tiempo de carga del primer dataset de datos:", elapsed_time, "segundos")

start_time = time.time()
data2 = pd.read_csv("study_performance.csv")
elapsed_time = time.time() - start_time

print("Tiempo de carga del segundo dataset de datos:", elapsed_time, "segundos")   

# Mostrar las primeras filas de cada dataset de datos para entender la estructura
print("Primer dataset de datos:")
print(data1.head())
print("\nSegundo dataset de datos:")
print(data2.head())

# Obtener información general sobre los datos de cada dataset
print("\nInformación del primer dataset de datos:")
print(data1.info())
print("\nInformación del segundo dataset de datos:")
print(data2.info())

# Realizar un resumen estadístico de las columnas numéricas de cada dataset
#tablefmt='psql' para poder ver la tabla 
print("\nResumen estadístico del primer dataset de datos:")
print(tabulate(data1.describe(), headers='keys', tablefmt='psql'))
print("\nResumen estadístico del segundo dataset de datos:")
print(tabulate(data2.describe(), headers='keys', tablefmt='psql'))

# Contar la cantidad de valores únicos en cada dataset de datos
print("\nCantidad de valores únicos en el primer dataset de datos:")
print(tabulate(data1.nunique().reset_index(), headers=['Columna', 'Valores Únicos'], tablefmt='psql'))
print("\nCantidad de valores únicos en el segundo dataset de datos:")
print(tabulate(data2.nunique().reset_index(), headers=['Columna', 'Valores Únicos'], tablefmt='psql'))

# Explorar valores únicos en columnas específicas de cada dataset de datos
print("\nValores únicos en la columna 'category' del primer dataset de datos:")
print(tabulate(data1['category'].unique().reshape(-1, 1), headers=['Valores Únicos'], tablefmt='psql'))
print("\nValores únicos en la columna 'gender' del segundo dataset de datos:")
print(tabulate(data2['gender'].unique().reshape(-1, 1), headers=['Valores Únicos'], tablefmt='psql'))

# Explorar la distribución de ciertas columnas de cada dataset de datos
print("\nDistribución de 'category' en el primer dataset de datos:")
print(tabulate(data1['category'].value_counts().reset_index(), headers=['Categoría', 'Cantidad'], tablefmt='psql'))
print("\nDistribución de 'gender' en el segundo dataset de datos:")
print(tabulate(data2['gender'].value_counts().reset_index(), headers=['Género', 'Cantidad'], tablefmt='psql'))

# Tiempo total
total_elapsed_time = time.time() - start_total_time
print("Tiempo total del análisis:", total_elapsed_time, "segundos")

# Graficar la distribución del primer dataset 
data1['category'].value_counts().plot(kind='bar', title='Distribución de category en el primer dataset de datos')
plt.xlabel('Categoría')
plt.ylabel('Cantidad')
plt.show()

plt.hist(data1['song_page_views'], bins=20, edgecolor='black')
plt.title('Distribución de vistas de página por canción')
plt.xlabel('Número de vistas de página')
plt.ylabel('Frecuencia')
plt.show()

data1['song_release_date'].value_counts().plot(kind='line', marker='o', linestyle='-')
plt.title('Distribución de fechas de lanzamiento de canciones')
plt.xlabel('Fecha de Lanzamiento')
plt.ylabel('Cantidad de Canciones')
plt.xticks(rotation=45)
plt.show()

data1['song_artists'].apply(lambda x: len(x.split(','))).value_counts().plot(kind='bar')
plt.title('Distribución de cantidad de artistas por canción')
plt.xlabel('Cantidad de Artistas')
plt.ylabel('Cantidad de Canciones')
plt.show()

# Graficar la distribución del segundo dataset 
data2['gender'].value_counts().plot(kind='bar', title='Distribución de gender en el segundo dataset de datos')
plt.xlabel('Género')
plt.ylabel('Cantidad')
plt.show()

data2['math_score'].plot(kind='hist', bins=20, title='Distribución de las puntuaciones en matemáticas del segundo dataset de datos')
plt.xlabel('Puntuación')
plt.ylabel('Frecuencia')
plt.show()

data2['reading_score'].plot(kind='hist', bins=20, title='Distribución de las puntuaciones en lectura del segundo dataset de datos')
plt.xlabel('Puntuación')
plt.ylabel('Frecuencia')
plt.show()

data2['writing_score'].plot(kind='hist', bins=20, title='Distribución de las puntuaciones en escritura del segundo dataset de datos')
plt.xlabel('Puntuación')
plt.ylabel('Frecuencia')
plt.show()
