#CAHSI Datascience Competition
#@authors Aedan Wells, Jennifer Minnich, Otto Strack
#Date 10/6

setwd("~/ML/mlhw2/")
library('ggplot2')

train = read.csv("iris_csv.csv")
ggplot(iris, aes(x = Petal.Width, y = Sepal.Width, colour = Species)) + geom_point() + ggtitle('Species by Petal and Sepal Width')

