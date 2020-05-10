library(tidyverse)
library(dplyr)
library(janitor)
library(caret)
library(ellipse)
library(rlang)

all_data <- read.csv("C:/Users/username/OneDrive/Masters_project_second_semester/footpath_information.csv")
  
data_trimmed <- all_data%>%
  select(.,full_id,
         highway,
         hiking,
      
         sac_scale,
         name,
         designation,
         surface,
         bicycle,
         step_count,
         lit,
         step_count,
         trail_visibility,
         sidewalk,
         osm_type,
         handrail,
         handrail.left,
         handrail.center,
         handrail.right,
         source.geometry,
         source.position,
         incline,
         abutters,
         smoothness,
         sidewalk,
         width,
         motor_vehicle,
         ford,
         cycleway,
         surface_2,
         visibility,
         source.designation,
         motorcar,
         steps,
         covered,
         footway,
         waterway,
         track_visibility,
         lit_1,surface_1,
         tracktype,
         scramble,
         scramble_grade,
         embankment,
         boggy,
         gradient,
         tactile_paving,
         cutting,
         surface_1,
         lit_1,
         foot,
       )

#ggplot(data=df_trimmed%>%filter(.,trail_visibility!=''))+
#  geom_bar(mapping=aes(x=trail_visibility,fill=sac_scale))




data_set <- data_trimmed%>%
          select(.,highway,surface,foot,name,sac_scale,hiking)%>%
          
  
          mutate(.,difficulty = case_when(
          sac_scale == "alpine_hiking" ~ 'hard',
          sac_scale == "demanding_alpine_hiking" ~ 'extreme' ,
          sac_scale == "difficult_alpine_hiking" ~ 'extreme',
          sac_scale == "demanding_mountain_hiking"~ 'extreme',
          sac_scale == "hiking"~ 'hard',
          sac_scale == "hiking; mountain_hiking"~ 'hard',
          sac_scale == "mountain_hiking;hiking"~ 'hard',
          hiking    == "yes" ~ 'hard',
          TRUE ~ NA_character_)) %>%
        
          mutate(.,surface = case_when(
          surface !='' ~ as.character(surface),
          TRUE ~ NA_character_))%>%

          mutate(.,name = case_when(
          name !='' ~ 'yes',
          TRUE ~ NA_character_))%>%
          
          mutate(.,hiking = case_when(
          hiking !='' ~ as.character(hiking),
          TRUE ~ NA_character_))%>%
          
          mutate(.,foot = case_when(
          name !='' ~ as.character(foot),
          TRUE ~ NA_character_))%>%
    
        select(.,-sac_scale)
  

data_set <- data_set[order(data_set$difficulty),]%>%
  slice(.,1:473)

data_set[is.na(data_set)] <- 'no idea'
data_set$foot[data_set$foot == '']<-"no idea"




validation_set <- createDataPartition(data_set$difficulty , p=0.70 , list = FALSE)
validation <- data_set[-validation_set,]
data_set <- data_set[validation_set,]



unique(data_set$highway)

unique(data_set$surface)


unique(data_set$foot)

unique(data_set$designation)


unique(data_set$name)


unique(data_set$hiking)


unique(data_set$difficulty)


control <- trainControl(method='cv',number = 10)
metric <- "Accuracy"

set.seed(7)
fit.lda <- train(difficulty~. , data=data_set , method = "lda" , metric=metric , trControl = control)

predictions <- predict(fit.lda,validation)

table(predictions)


confusionMatrix(predictions,validation$difficulty)
