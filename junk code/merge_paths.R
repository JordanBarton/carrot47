library(sf)
library(dplyr)
library(tidyverse)
library(tidyr)

path <- "C:\\Users\\username\\OneDrive\\Masters_project_second_semester\\current_paths"

hill<-read_csv("C:\\Users\\username\\OneDrive\\Masters_project_second_semester\\csvs\\coordsOfExtendedWainwrights.csv")%>%
  filter(.,W==1)%>%
  select(.,hillnumber)
  
df <- read_sf(paste0(path,'\\path ',as.character( hill$hillnumber[215] ) ,' .gpkg')) %>%
  mutate(.,origin = hill$hillnumber[215])



for(i in 1:214) {

  df_new <- read_sf(paste0(path,'\\path ',as.character( hill$hillnumber[i] ) ,' .gpkg')) %>%
    mutate(.,origin = hill$hillnumber[i])
  df <- rbind(df,df_new)
}
order$to[215] = order$from[1]


coords <- read_sf("C:\\Users\\username\\OneDrive\\Masters_project_second_semester\\maps\\extras\\summitPositions.gpkg")

df_total <- left_join(as_tibble(df),as_tibble(coords), by = c("cat" = "URI"))%>%
  select(.,from = origin,to = hillNumber,path=geom.x)

write_sf(df_total,"C:\\Users\\username\\OneDrive\\Masters_project_second_semester\\maps\\extras\\all_paths.gpkg")


order <- read_csv("C:\\Users\\username\\OneDrive\\Masters_project_second_semester\\processed_costs\\ordertidy.csv")%>%
  mutate(.,to=lead(from))

relevent_paths <- df_total %>%
  left_join(.,order, by = c("from","to"))%>%#Keswick
#need hillnumber corresponding to the to collum for the highest value of order
#then lookup this hillnumber -> 9999 and make the order the max order +1
  
  

final_peak <- as.numeric(relevent_paths[relevent_paths$order %in% max(relevent_paths$order , na.rm = TRUE),2])
x<-as.list(which(relevent_paths$from == final_peak))
y<-as.list(which(relevent_paths$to == 9999))
row_final <- as.numeric(intersect(x,y))
relevent_paths$order[row_final] =  max(relevent_paths$order , na.rm = TRUE) + 1



relevent_paths <- relevent_paths %>%
  filter(.,!is.na(order))

costs <- read_csv("C:\\Users\\username\\OneDrive\\Masters_project_second_semester\\processed_costs\\nn14k_machine.csv")

route <- relevent_paths%>%
  left_join(.,costs,by = c("from","to"))

if ( length(route$order) != max(route$order , na.rm = TRUE)){print("YOU ARE MISSING PATHS DONT USE THIS ROUTE")}


write_sf(route , paste0(path,'\\route','.gpkg'))
print(sum(route$time))

