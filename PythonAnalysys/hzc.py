from pyspark.sql import SparkSession
from pyspark.sql.functions import col

# Создание сессии Spark
spark = SparkSession.builder \
    .appName("Simple PySpark Example") \
    .getOrCreate()

# Чтение данных из CSV файла
df = spark.read.csv("housing.csv", header=True, inferSchema=True)

# Вывод первых нескольких строк данных
df.show()

# Выполнение операции агрегации (например, подсчет количества записей)
count = df.count()
print("Total count:", count)

# Закрытие сессии Spark
spark.stop()
