# abrir los datos
import pandas as pd
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

# tipo de valores que tenemos
print(netflix.dtypes)
# date_added      object

# cambiar tipo de dato en date_added a fecha
netflix["date_added"] = pd.to_datetime(netflix["date_added"])
# print(netflix.dtypes)

# Puedes eliminar columnas que no te aportan información? 
# ¿Cuáles son? 
