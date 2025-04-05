import pandas as pd
import re
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

netflix = pd.read_csv("netflix1.csv", delimiter=",", index_col = 0)

netflix_sd = netflix.drop_duplicates().fillna(0).copy()
netflix_sd["date_added"] = pd.to_datetime(netflix_sd["date_added"])

# extraer peliculas
movies = netflix_sd[netflix_sd['type'] == 'Movie'].copy()
print(movies.sample(10))

# quitar columnas innecesarias
movies = movies.drop(columns=['type', 'title', 'date_added', 'director', 'country', 'rating', 'listed_in'])
print(movies.sample(10))

movies['duration_minutes'] = movies['duration'].str.extract('(\d+)').astype(float)
movies1700 = movies[movies['release_year'] >= 1940].copy()
tabla_comparativa = movies1700.groupby('release_year')['duration_minutes'].mean().reset_index()

print(tabla_comparativa)

# haccer un gráfico de la duración promedio de las películas por año
plt.figure(figsize=(12, 6))
plt.plot(tabla_comparativa['release_year'], tabla_comparativa['duration_minutes'], marker='o')
plt.title('Duración promedio de películas por año') 
plt.xlabel('Año de estreno')
plt.ylabel('Duración (minutos)')
plt.xticks(np.arange(1940, 2025, 3))
plt.grid()
plt.show()