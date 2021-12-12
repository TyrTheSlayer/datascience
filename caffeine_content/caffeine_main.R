#-------------------------------------------------------------------------------
# title: caffeine_main.R
# Author: Aedan Wells
# Date: 12/10/21
# Description: General code for caffeine analysis from kaggle, see
#              README for additional details
#-------------------------------------------------------------------------------

#setting working directory and importing the dataset----
setwd("~/datascience/caffeine_content/")
data <- read.csv("caffeine.csv")

#Section for library/package imports----
library(ggplot2)
library(dplyr)

#general data analysis, adding caffeine concentration----
head(data)
tail(data)
data <- mutate(data, caffeine_concentration = Caffeine..mg. / Volume..ml.)

#boxplot of type versus caffeine level----
ggplot(data, aes(type, Caffeine..mg., fill=type) )+
  geom_boxplot(outlier.colour = "red", outlier.shape = 1)+xlab("Type of Drink")+ 
  ylab("Caffeine (mg)")+ggtitle("Drink Type boxplot to caffeine")

#boxplot of type versus caffeine concentration----
ggplot(data, aes(type, caffeine_concentration, fill=type) )+
  geom_boxplot(outlier.colour = "red", outlier.shape = 1)+xlab("Type of Drink")+ 
  ylab("Caffeine Concetration (mg/ml)")+
  ggtitle("Drink Type boxplot to caffeine concentration")

#stat plot for frequency of drink type
ggplot(data, aes(type, fill=type))+stat_count(show.legend = FALSE)+
  xlab("Drink Type")+ylab("Frequency")+ggtitle("Drink Type Frequency")+ 
  theme(legend.position = "none")


#basic bar plot to see drink ranking----
data.sort1 <- data[order(-data$caffeine_concentration),]
ggplot(data.sort1[0:30,], aes(drink, caffeine_concentration, fill=type))+
  geom_col()+theme(axis.text.x = element_text(angle = 90, vjust = 0.5, hjust=1))+
  ggtitle("Top 30 drinks by Caffeine Concetration")+xlab("Drink")+
  ylab("Caffeine Concentration")


#-----------------------------------------------
#Machine learning section
#-----------------------------------------------

#tree to predict drink type----
library(tree)
data = select(data, -drink)
set.seed(122)
train = sample(1:nrow(data), nrow(data)*0.7)
tree.caffeine = tree(type~., data, subset=train)
summary(tree.caffeine)
plot(tree.caffeine)
text(tree.caffeine)

#testing the tree----
test.caffeine = data[-train,]
pred=predict(tree.caffeine, test.caffeine, type = "class")
table(pred, test.caffeine$type)

#check for need to prune----
cv.caffeine = cv.tree(tree.caffeine, FUN=prune.misclass)
cv.caffeine

prune.caffeine = prune.misclass(tree.caffeine, best = 11)
plot(prune.caffeine)
text(prune.caffeine)
pred=predict(prune.caffeine, test.caffeine, type = "class")
table(pred, test.caffeine$type)

