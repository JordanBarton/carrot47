library(caret)
library(ellipse)
library(tidyverse)


#read the data
data(iris)
df<-iris

#split the data into the training set and the validation set
validation_set <- createDataPartition(df$Species , p=0.2 , list = FALSE)
validation <- df[-validation_set,]
df <- df[validation_set,]



#print lots of tables, not too important
dim(df)
sapply(df, class)
glimpse(df)
levels(df$Species)
summary(df)
perc<-prop.table(table(df$Species))*100
cbind(freq=table(df$Species),percentage=perc)


#multivariate plots
x<-df[,1:4]
y<-df[,5]
featurePlot(x=x,y=y , plot = "ellipse")
featurePlot(x=x,y=y , plot = "box")
featurePlot(x=x,y=y , plot = "density")


#number of resamplings
control <- trainControl(method='cv',number = 10)
metric <- "Accuracy"

#train from training set
set.seed(7)
fit.lda <- train(Species~. , data=df , method = "lda" , metric=metric , trControl = control)


#set.seed(7)
#fit.knn <- train(Species~. , data=df , method = "knn" , metric=metric , trControl = control)


#set.seed(7)
#fit.rpart <- train(Species~. , data=df , method = "rpart" , metric=metric , trControl = control)


#set.seed(7)
#fit.svm <- train(Species~. , data=df , method = "svmRadial" , metric=metric , trControl = control)


#set.seed(7)
#fit.rf <- train(Species~. , data=df , method = "rf" , metric=metric , trControl = control)


#determine best model
#results <- resamples(list(lda=fit.lda, part=fit.rpart, knn=fit.knn, svm=fit.svm, rf=fit.rf))
#summary(results)
#dotplot(results)
#print(fit.lda)
#print(fit.knn)
#print(fit.rpart)
#print(fit.svm)
#print(fit.rf)


#check predictions of validation set and display
predictions <- predict(fit.lda,validation)
confusionMatrix(predictions,validation$Species)