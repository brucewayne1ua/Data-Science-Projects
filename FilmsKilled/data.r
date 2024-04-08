library(dplyr)
library(ggplot2)

movie_body_counts <- read.csv('films.csv')

head(movie_body_counts)

str(movie_body_counts)

ggplot(movie_body_counts, aes(x=Body_Count)) +
 geom_histogram(bins=20, color="grey", fill="lightblue") 

 movie_body_counts %>%
 top_n(n = 10, Body_Count) %>%
 arrange(desc(Body_Count))

 movie_body_counts %>%
 top_n(n = 10, body_per_min) %>%
 arrange(desc(body_per_min))