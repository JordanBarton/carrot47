#analyse pauls route
library(lubridate)
library(tidyverse)

haversine <- function(lat1, lat2, long1, long2, in_miles = FALSE){
  lat1=lat1*pi/180
  lat2=lat2*pi/180
  long1=long1*pi/180
  long2=long2*pi/180
 
  h <- sin(.5 * (lat2 - lat1)) ^ 2 + cos(lat1) * cos(lat2) * (sin(.5 * (long2 - long1)) ^ 2)
  
  r <- 12756 / 2
  
  if (in_miles)
    r <- r * 0.621371e3
  
  return(2e3 * r * asin(sqrt(h)))
}

wainwrights_coords <- read_csv("C:\\Users\\username\\OneDrive\\Masters_project_second_semester\\csvs\\coordsOfExtendedWainwrights.csv") %>% filter(.,W==1)



df <- read_csv("C:\\Users\\username\\OneDrive\\Masters_project_second_semester\\csvs\\Paul tierney route.csv",col_names = c("LEG","START TIME","TIME ELAPSED")) %>%
  transmute(.,
            LEG,
            time_taken = hms(`TIME ELAPSED`),
            time_taken = as.integer(seconds(time_taken))) %>%
  left_join(.,wainwrights_coords,by = c("LEG" = "hillname") ) %>%
  select(.,from=LEG , time_taken ,lat1=latitude,long1=longitude, from_number = hillnumber) %>%
  mutate(., 
         to = lead(from),
         time_taken = lead(time_taken),
         to_number = lead(from_number)) %>%
  mutate(.,
         lat2 = lead(lat1),
         long2 = lead(long1),
         distance_travelled = haversine(lat1, lat2, long1, long2)) %>%
  mutate(.,
         velocity = distance_travelled/time_taken)%>%
  mutate(.,
         ratio= velocity/mean(velocity,na.rm=TRUE))%>%
  mutate(.,order=row_number())
df[1,5] = 9999

ggplot(data=df,aes(x=ratio))+
  geom_histogram()




order <- select(df,order,from=from_number)
write_csv(order,"C:\\Users\\username\\OneDrive\\Masters_project_second_semester\\csvs\\paul_order.csv")
















#dM <- read_csv("modelRoute.csv",col_names = TRUE)

#ggplot(data=dM,aes(x=ratio))+
#  geom_histogram()



#r=as.data.frame(dM$ratio/df$ratio)
#ggplot(data = r, aes(x=dM$ratio/df$ratio))+
#  geom_histogram()


