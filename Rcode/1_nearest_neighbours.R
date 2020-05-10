library(dplyr)
library(tidyverse)

haversine <- function(lat1, lat2, long1, long2){
  lat1=lat1*pi/180
  lat2=lat2*pi/180
  long1=long1*pi/180
  long2=long2*pi/180
  
  h <- sin(.5 * (lat2 - lat1)) ^ 2 + cos(lat1) * cos(lat2) * (sin(.5 * (long2 - long1)) ^ 2)
  
  r <- 12756 / 2
  
  return(2e3 * r * asin(sqrt(h)))
}



df <- read_csv("C:\\Users\\username\\OneDrive\\Masters_project_second_semester\\csvs\\coordsOfExtendedWainwrights.csv")%>%
#  filter(.,W==1)%>%  
  dplyr::select(.,hillnumber,latitude,longitude)

places <- dplyr::select(df,hillnumber)  %>%
  mutate(.,i=1) %>%
  left_join(.,.,by="i")%>%
  dplyr::select(from=hillnumber.x,to=hillnumber.y)%>%
  filter(.,to!=from)%>%
  left_join(.,df,by = c("from" = "hillnumber"))%>%
  left_join(.,df,by = c("to" = "hillnumber"))%>%
  mutate(.,distance = haversine(lat1 = latitude.x,
                                lat2 = latitude.y,
                                long1 = longitude.x,
                                long2 = longitude.y))%>%
  dplyr::select(.,from,to,distance)%>%
  group_by(.,from)%>%
  arrange(.,distance)%>%
  slice(.,1:13)%>%
  dplyr::select(.,from,to)


write_csv(places,"C:\\Users\\username\\OneDrive\\Masters_project_second_semester\\csvs\\nearest_neighbours.csv")


  

#convert into tidy, every hillnumber needs to have every other hillnumber as go to

#for each hill we need to be able to calculated n nearset neighbour




