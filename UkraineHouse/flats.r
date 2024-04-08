
library(dplyr)

# Замените "путь_к_файлу/flats.csv" на путь к вашему файлу flats.csv
flats <- read.csv("flats.csv", stringsAsFactors=FALSE, encoding="UTF-8", dec=",")

lviv_one <- flats %>%
    filter(Місто == "Львів", Кімнат == 1)

median_lviv <- median(lviv_one$Площа, na.rm = TRUE)
print(median_lviv)
