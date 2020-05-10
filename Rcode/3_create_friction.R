library(tidyverse)
library(sf)
library(raster)
library(stars)

#EU HYDRO
f <- function(x){

  if(x == 16){x=1.6}#inland rock
  if(x == 1){x=27700}#seawater
  if(x == 2){x=1.5}#broadleaved forest
  if(x == 3){x=1}#improved grassland
  if(x == 4){x=1}#acid grassland
  if(x == 5){x=1}#saltmarsh should be 1.8 but replaced with 1 due to lots of acid mid-ID
  if(x == 6){x=1.2}#arable and horticulture
  if(x == 7){x=1.2}#heather
  if(x == 8){x=1.8}#bog
  if(x == 9){x=1}#supralittoral sediment
  if(x == 10){x=1}#littoral sediment
  if(x == 11){x=1.2}#heather grassland
  if(x == 12){x=1.5}#coniferous woodland
  if(x == 13){x=1}#calc grassland
  if(x == 14){x=27700}#water
  if(x == 15){x=1.6}#urban should be 1 but replaced with 1.6 due to lots of inland rock mis-ID
  x}





#read in land vector map and create lake map from it####
lake <- read_sf("C:\\Users\\username\\OneDrive\\Masters_project_second_semester\\maps\\extras_outer_2\\land_vector_map.gpkg")%>%
  st_transform(.,32630)%>%
  dplyr::select(bhab)%>%
  filter(bhab == 'Freshwater'|bhab == 'Saltwater')%>%
  transmute(.,cost = 100)

#b)convert land map to cost####
land_raster <- raster("C:\\Users\\username\\OneDrive\\Masters_project_second_semester\\maps\\extras_outer_2\\machine_learned_map.tif")%>%
  calc(.,f)

#c)read in highways and cost them####
highways <- read_sf("C:\\Users\\username\\OneDrive\\Masters_project_second_semester\\maps\\extras_outer_2\\footpath_map_outer.gpkg")%>%
  st_transform(.,32630)%>%
  dplyr::select(.,uri=osm_id)%>%
  mutate(.,
         cost = 0)%>%
  dplyr::select(.,cost)




#d)read in river and cost it####
OS_river <- read_sf("C:\\Users\\username\\OneDrive\\Masters_project_second_semester\\maps\\extras_outer_2\\river_map_outer.gpkg")%>%
  st_transform(.,32630)%>%
  dplyr::select(.,uri=gml_id)%>%
  mutate(.,
         cost = 15)%>%
  dplyr::select(.,cost)






#e) read in building map and cost it####

buildings<-read_sf("C:\\Users\\username\\OneDrive\\Masters_project_second_semester\\maps\\extras_outer_2\\banana.gpkg")%>%
  st_transform(.,32630)%>%
  dplyr::select(.)%>%
  mutate(.,
         cost = 99)%>%
  dplyr::select(.,cost)


#overlay####
land_raster %>%
  disaggregate(.,fact=2)%>%
  raster::writeRaster(.,"C:\\Users\\username\\OneDrive\\Masters_project_second_semester\\maps\\extras_outer_2\\land_temp.tif",overwrite=TRUE)



land_raster_stars <- read_stars("C:\\Users\\username\\OneDrive\\Masters_project_second_semester\\maps\\extras_outer_2\\land_temp.tif")



cost_map1 <- land_raster_stars %>% 
  st_rasterize(OS_river,template=.)


cost_map2<-cost_map1%>%
  st_rasterize(lake,template=.)

cost_map3 <- cost_map2%>%
  st_rasterize(buildings,template=.)

cost_map4 <- cost_map3 %>%
  st_rasterize(highways,template=.)

  

#write out####
write_stars(cost_map4,dsn="C:\\Users\\username\\OneDrive\\Masters_project_second_semester\\maps\\extras_outer_2\\cost_map_outer_with_buildings.tif",overwrite=TRUE)






