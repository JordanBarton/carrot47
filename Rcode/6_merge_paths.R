library(sf)
library(dplyr)
library(tidyverse)
library(tidyr)

#take in lookup table
#take in each path and merge them to make all_paths
#take in coords
#take in model order -> return route.gpkg
#take in paul order -> return route.gpkg
#print costs

path <- "C:\\Users\\username\\OneDrive\\Masters_project_second_semester\\processed_costs\\routes"

hill<-read_csv("C:\\Users\\username\\OneDrive\\Masters_project_second_semester\\csvs\\coordsOfExtendedWainwrights.csv")%>%
#  filter(.,W==1)%>%
  dplyr::select(.,hillnumber)

  
df <- read_sf(paste0(path,'\\path ',as.character( hill$hillnumber[print(length(hill$hillnumber))] ) ,' .gpkg')) %>%
  mutate(.,origin = hill$hillnumber[print(length(hill$hillnumber))])



for(i in 1:length(hill$hillnumber)) {

  df_new <- read_sf(paste0(path,'\\path ',as.character( hill$hillnumber[i] ) ,' .gpkg')) %>%
    mutate(.,origin = hill$hillnumber[i])
  df <- rbind(df,df_new)
}




coords <- read_sf("C:\\Users\\username\\OneDrive\\Masters_project_second_semester\\maps\\extras_outer_2\\summit_positions_outer_27700.gpkg")

coords <- coords%>%
  mutate(.,URI = row_number())


df_total <- left_join(as_tibble(df),as_tibble(coords), by = c("cat" = "URI"))%>%
  dplyr::select(.,from = origin,to = hillnumber,path=geom.x)

write_sf(df_total,"C:\\Users\\username\\OneDrive\\Masters_project_second_semester\\processed_costs\\outer_paths\\all_paths.gpkg")

#model####
order <- read_csv("C:\\Users\\username\\OneDrive\\Masters_project_second_semester\\csvs\\paul_order.csv")%>%
  mutate(.,to=lead(from))

df_total <- read_sf("C:\\Users\\username\\OneDrive\\Masters_project_second_semester\\routes\\all_paths\\all_paths_new_0133.gpkg")%>%
  mutate(from = as.numeric(as.character(df_total$from))  ,  to = as.numeric(as.character(df_total$to))  )


relevent_paths <- df_total %>%
  left_join(.,order, by = c("from","to"))


#Keswick
#need hillnumber corresponding to the to collum for the highest value of order
#then lookup this hillnumber -> 9999 and make the order the max order +1

final_peak <- as.numeric(relevent_paths[relevent_paths$order %in% max(relevent_paths$order , na.rm = TRUE),2])
x<-as.list(which(relevent_paths$from == final_peak))
y<-as.list(which(relevent_paths$to == 9999))
row_final <- as.numeric(intersect(x,y))
relevent_paths$order[row_final] =  max(relevent_paths$order , na.rm = TRUE) + 1



relevent_paths <- relevent_paths %>%
  filter(.,!is.na(order))

costs <- read_csv("C:\\Users\\username\\OneDrive\\Masters_project_second_semester\\processed_costs\\outer_costs\\tidy.csv")

route <- relevent_paths%>%
  left_join(.,costs,by = c("from","to"))

if ( length(route$order) != max(route$order , na.rm = TRUE)){print("YOU ARE MISSING PATHS DONT USE THIS ROUTE")}


write_sf(route , paste0(path,'\\route','.gpkg'))
total <- sum(route$time)







#paul####
order_paul <- read_csv("C:\\Users\\username\\OneDrive\\Masters_project_second_semester\\csvs\\paul_order.csv")
order_paul<- order_paul%>%
  mutate(.,to=lead(from))%>%
  filter(.,row_number()!= length(order_paul$from))


max = length(order_paul$from)
final_peak_paul <- as.numeric(order_paul[order_paul$from %in% max(order_paul$from , na.rm = TRUE),2])
order_paul$to[max] = final_peak_paul


relevent_paths_paul <- df_total %>%
  left_join(.,order_paul, by = c("from","to"))
#Keswick
#need hillnumber corresponding to the to collum for the highest value of order
#then lookup this hillnumber -> 9999 and make the order the max order +1
  

relevent_paths_paul <- relevent_paths_paul %>%
  filter(.,!is.na(order))

costs <- read_csv("C:\\Users\\username\\OneDrive\\Masters_project_second_semester\\processed_costs\\nn14k_machine.csv")

route_paul <- relevent_paths_paul%>%
  left_join(.,costs,by = c("from","to"))

if ( length(route_paul$order) != max(route_paul$order , na.rm = TRUE)){print("YOU ARE MISSING PATHS DONT USE THIS ROUTE")}


write_sf(route_paul , paste0(path,'\\route_paul','.gpkg'))
total_paul <- sum(route_paul$time)

print(total)
print(total_paul)
print(paste0(total/total_paul*100,'%'))

