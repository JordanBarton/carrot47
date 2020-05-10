library(tidyr)
library(tidyverse)
library(dplyr)
library(sf)
library(geojson)
library(geojsonlint)

empty <- st_as_sfad(.$geom, default = empty), from = geom)%>%
  dplyr::select(.,hillNumber,from,to)%>%
  st_drop_geometry(.)
ordered_df[215,3] = ordered_dfc("POINT(EMPTY)")

order <- read_csv("C:\\Users\\username\\OneDrive\\Masters_project_second_semester\\processed_costs\\ordertidy.csv")

coords <- read_sf("C:\\Users\\username\\OneDrive\\Masters_project_second_semester\\maps\\extras\\summitPositions_27700.gpkg")

df <- left_join(coords,order, by = c("hillNumber" = "from")) %>%
  select(.,-URI,-hillName)
  
index<-order(df$order)

ordered_df <- df[index,]%>%
  mutate(.,to = le[1,2])



df <- ordered_df
df1 <- df %>% slice(rep(1:n(), each = 2)) 

df2 <- mutate(df1,from_coords = unlist(ordered_df$from))%>%
  mutate(.,to_coords = unlist(ordered_df$to))%>%
  dplyr::select(.,-from,-to)%>%
  mutate(.,from_x = from_coords, from_y = lead(.$from_coords),to_x=to_coords, to_y=lead(.$to_coords))
  

toDelete <- seq(1, nrow(df2), 2)
df3 <- df2[ toDelete ,]%>%
  select(.,-from_coords,-to_coords)
  

df4 <- mutate(df3,x = paste('{"type": "LineString", "coordinates": [ [',as.character(df3$from_x),',',as.character(df3$from_y),'] , [',as.character(df3$to_x),',',as.character(df3$to_y),'] ] }'))

df5 <- mutate(df4 , y = linestring(x))

x <- '{"type": "LineString", "coordinates": [ [ 326635.171154654 , 523437.559389753 ] , [ 327922.009580651 , 524699.026179244 ] ] }'
z <- linestring(x)
geo_write(z, f <- tempfile(fileext = ".geojson"))
write_sf('z',z)
  
#  mutate(.,x_from = case_when(row_number(unlist(.$from))%%2 == 0 ~ unlist(.$from)[row_number(unlist(.$from))]))



