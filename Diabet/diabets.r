library(openxlsx)


diabetes_data <- read.csv("Diabetes.csv")

head(diabetes_data,3) 

#Среднее значение уровня глюкозы в крови
mean_glucose <- mean(diabetes_data$Age)
print(paste("Среднее значение уровня глюкозы:", mean_glucose))

#Вычисление моды возраста диабетиков
age_freq <- table(diabetes_data$Age)
age_mode <- as.numeric(names(age_freq)[which.max(age_freq)])
print(paste("Чаще всего диабет наблюдается у людей в возрасте: ", age_mode))


# Вычисление корреляции Связь между глюкозой и инсулином
correlation_matrix <- cor(diabetes_data[, c("Glucose", "Insulin")])

# Вывод матрицы корреляции
print(correlation_matrix)




# Создание новых заголовков
new_colnames <- c("Pregnancies", "Glucose", "Blood Pressure", "Skin Thickness", "Insulin", "BMI", "Diabetes Pedigree Function", "Age", "Outcome")

# Назначение новых заголовков
colnames(diabetes_data) <- new_colnames

# Создание индексации строк начиная с 1
diabetes_data$Index <- 1:nrow(diabetes_data)

# Переставляем столбец с индексом на первое место
diabetes_data <- diabetes_data[, c("Index", new_colnames)]

# Сохранение данных в формате Excel с новыми заголовками
write.xlsx(x = diabetes_data, file = "Diabetes_statistic.xlsx", rowNames = FALSE)