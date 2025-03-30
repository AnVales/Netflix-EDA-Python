# abrir los datos
import pandas as pd
import re

netflix = pd.read_csv("netflix1.csv", delimiter=",", index_col = 0)
print('sample: ',netflix.sample(10))

# ¿Cuántos valores nulos encontrás en los datos?
print('\n valores nulos: ', netflix.isna().sum())

# hay valores nulos puestos como "Not Given"
print('\n valores ausentes con NOT GIVEN: ', (netflix == "Not Given").sum().sum())
# faltan director 2588 veces y country 287 veces.

# ¿tendremos archivos duplicados?
print('\n valores duplicados: ', netflix.duplicated().sum())
# dice que hay 2 duplicados

# quitamos los duplicados
netflix_sd = netflix.drop_duplicates().copy()
print('\n valores duplicados: ', netflix_sd.duplicated().sum())

# tipo de valores que tenemos
print(netflix_sd.dtypes)
# date_added      object

# cambiar tipo de dato en date_added a fecha
netflix_sd["date_added"] = pd.to_datetime(netflix_sd["date_added"])

# ¿son series?
netflix_sd['serie_duration'] = netflix_sd['duration'].str.extract(r'(\d+) Season').fillna(0)

# ¿son peliculas?
netflix_sd['pelicula_duration'] = netflix_sd['duration'].str.extract(r'(\d+) min').fillna(0)

# reorganizacion de columnas
netflix_sd = netflix_sd.drop(columns=['duration', 'type'])
col_cat = ['title', 'director', 'country', 'rating', 'listed_in']
netflix_sd[col_cat] = netflix_sd[col_cat].astype('category')

time_cat = ['serie_duration', 'pelicula_duration']
netflix_sd[time_cat] = netflix_sd[time_cat].astype('int64')

