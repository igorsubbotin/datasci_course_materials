library(caret)
library(ggplot2)
library(rpart)
library(randomForest)
library(e1071)

data <- read.csv('seaflow_21min.csv', header=TRUE)
dim(data)
summary(data)
str(data)

#question1
dim(data[data$pop == 'synecho',])[1]

#question2
#39184

#question3
inTrain <- createDataPartition(y=data$pop, p=0.5, list=FALSE)
training <- data[inTrain,]
testing <- data[-inTrain,]
mean(training$time)

#question4
summary(data$pop)
plot(data$pe, data$chl_small, col=data$pop)
legend("topright", legend=levels(factor(data$pop)), text.col=seq_along(levels(factor(data$pop))))

#question5,6,7
model <- rpart(pop ~ fsc_small + fsc_perp + fsc_big + pe + chl_big + chl_small, data=training)
print(model)

#question8
pr <- predict(model,new=testing, type ="vector")
dim(training)[1]
sum(as.integer(pr == as.integer(testing$pop)))/(dim(training)[1])

#question9,10
model <- randomForest(pop ~ fsc_small + fsc_perp + fsc_big + pe + chl_big + chl_small, data=training)
pr <- predict(model,newdata=testing)
sum(as.integer(pr == testing$pop))/(dim(training)[1])

#question11,12
model <- svm(pop ~ fsc_small + fsc_perp + fsc_big + pe + chl_big + chl_small, data=training)
pr <- predict(model,newdata=testing)
table(pred = pr, true = testing$pop)
acc1 <- sum(as.integer(pr == testing$pop))/(dim(training)[1])

#question13
hist(data$fsc_small)
hist(data$fsc_perp)
hist(data$fsc_big)
hist(data$pe)
hist(data$chl_small)
hist(data$chl_big)

#question14
training1 <- subset(training, file_id != 208)
testing1 <- subset(testing, file_id != 208)
model <- svm(pop ~ fsc_small + fsc_perp + fsc_big + pe + chl_big + chl_small, data=training1)
pr <- predict(model,newdata=testing1)
acc2 <- sum(as.integer(pr == testing1$pop))/(dim(training1)[1])
acc1 - acc2