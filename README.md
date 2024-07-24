***Este proyecto tiene como objetivo analizar dos conjuntos de datos: "ts_discography_released.csv" y "study_performance.csv", asi como aprender a graficar algunas funciones basicas matematicas.***
*El análisis se centra en la exploración de la estructura de los datos, la obtención de información estadística, la identificación de patrones y la visualización de resultados mediante gráficos.*

**Pasos para ejecutar "dataset.py":**

1. Instalar las dependencias:
**pip install pandas matplotlib tabulate**

3. Ejecutar el script **dataset.py**.

Descripción del archivo dataset.py:

Este archivo contiene el código Python para el análisis de los datasets. El código se divide en las siguientes secciones:

***Carga de datos:***

Se cargan los datasets "ts_discography_released.csv" y "study_performance.csv" en variables (data1 y data2).
Se mide el tiempo de carga de cada dataset.

***Exploración inicial:***

Se muestran las primeras filas de cada dataset para comprender su estructura.
Se obtiene información general sobre cada dataset (tipo de datos, número de filas y columnas, etc.).

***Análisis estadístico:***

Se obtiene un resumen estadístico de las columnas numéricas de cada dataset (media, mediana, desviación estándar, etc.).
Se cuenta la cantidad de valores únicos en cada columna de cada dataset.

***Análisis de columnas específicas:***

Se exploran los valores únicos en las columnas "category" del primer dataset y "gender" del segundo dataset.
Se analiza la distribución de las mismas columnas mediante conteos y gráficos de barras.

***Análisis de fechas:***

Se analiza la distribución de las fechas de lanzamiento de canciones en el primer dataset mediante un gráfico de líneas.

***Análisis de artistas:***

Se analiza la distribución de la cantidad de artistas por canción en el primer dataset mediante un gráfico de barras.

***Análisis del rendimiento académico:***

Se analiza la distribución de las puntuaciones en matemáticas, lectura y escritura en el segundo dataset mediante histogramas.

***Visualización de resultados:***

Se generan gráficos de barras, histogramas y líneas para visualizar la distribución de las variables analizadas.
