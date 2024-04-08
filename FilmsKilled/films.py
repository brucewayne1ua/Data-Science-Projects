import pandas as pd

import pandas as pd

# Чтение данных из файла CSV и создание DataFrame
df = pd.read_csv("filmdeathcounts.csv")

# Вычисление среднего рейтинга IMDB
average_imdb_rating = df['IMDB_Rating'].mean()

# Вывод среднего рейтинга IMDB
print("Средний рейтинг IMDB для фильмов:", average_imdb_rating)



# Чтение данных из файла CSV и создание DataFrame
df = pd.read_csv("filmdeathcounts.csv")

# Удаление разделителя из значений в столбце 'Genre'
df['Genre'] = df['Genre'].str.replace('|', '')

# Вывод первых нескольких строк DataFrame для проверки
print(df.head())



# Чтение данных из файла CSV и создание DataFrame
df = pd.read_csv("filmdeathcounts.csv")

# Переименование столбцов
df = df.rename(columns=lambda x: x.replace('_', ' '))

# Вывод первых нескольких строк DataFrame для проверки
print(df.head())