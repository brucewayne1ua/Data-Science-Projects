import pandas as pd
from sklearn.linear_model import LinearRegression

# Загрузка данных
df = pd.read_excel('Price.xlsx')

# Извлечение данных
prices = df['Price']

# Подготовка данных
X = prices[:-1]
y = prices[1:]

# Преобразование Series в DataFrame
X = pd.DataFrame(X)  # Или X = X.to_frame().T

# Обучение модели
model = LinearRegression()
model.fit(X, y)

# Прогнозирование цены
prediction = model.predict(X[+1:])

# Оценка точности
print('Accuracy:', model.score(X, y))

# Печать прогноза
print('Predicted price:', prediction)
