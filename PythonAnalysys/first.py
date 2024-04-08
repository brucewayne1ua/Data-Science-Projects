import numpy as np
import pandas as pd 

# Загрузка данных из файла Excel
df = pd.read_excel("Datas.xlsx", sheet_name="Лист1")

# Рассчет среднего возраста
average_age = df["Возраст"].mean()

# Расчет общей зарплаты

middle_salary = df["Средняя зарплата"].sum()

Array = [3,1,22,5,45,642,11,2235,33346,1123]
SortArray = np.sort(Array)

print(middle_salary)
print("Средний возраст:", average_age)
print(SortArray)



