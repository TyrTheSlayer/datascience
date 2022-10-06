#CAHSI Datascience Competition
#@authors Aedan Wells, Jennifer Minnich, Otto Strack
#Date 10/6

setwd("~/datascience/CAHSI/")

train = read.csv("D1.csv")
ytrain = train[ , ncol(train), drop = FALSE]
xtrain = train[,-ncol(train)]

model = lm(ytrain ~ xtrain)
