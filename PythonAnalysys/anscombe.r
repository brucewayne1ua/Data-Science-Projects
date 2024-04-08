# Функция для вычисления полинома Лагранжа
lagrange_polynomial <- function(x, y) {
  n <- length(x)
  L <- function(i) {
    numerator <- prod(x[i] - x[-i])
    denominator <- prod(x[i] - x[-i])
    return(numerator/denominator)
  }
  
  P <- function(x_val) {
    result <- sum(y * sapply(1:n, function(i) L(i) * x_val))
    return(result)
  }
  
  return(P)
}

# Пример использования
x <- c(1, 2, 3, 4)
y <- c(3, 5, 7, 9)

# Создание полинома Лагранжа
lagrange <- lagrange_polynomial(x, y)

# Вычисление значения полинома в точке
result <- lagrange(2.5)
print(result)  # Выводит результат
