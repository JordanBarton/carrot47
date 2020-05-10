library(tidyverse)
library(sf)
library(raster)
library(stars)
library(rgrass7)
library(ggplot2)


#####################################################
#format sample into a raster
land <- read_sf("C:/Users/username/OneDrive/Masters_project_second_semester/maps/machine_maps/sampling_current.gpkg")%>%
  st_transform(.,32630)
  
land_class <- land%>%
  st_drop_geometry(.)%>%
  mutate(.,land_type = tolower(land_type))%>%
  distinct(.)%>%
  mutate(.,class_number = row_number())

write_csv(land_class , "C:\\Users\\username\\OneDrive\\Masters_project_second_semester\\csvs\\land_type_lookup_table.csv")


land <- land%>%
  left_join(.,land_class)%>%
  dplyr::select(.,-land_type)
   
 

land_raster <-st_rasterize(land,template=st_as_stars(st_bbox(land),dx=10,dy=10 ,values=NA_real_))
write_sf(land,"C:\\Users\\username\\OneDrive\\Masters_project_second_semester\\maps\\integer_class_vector.gpkg")
write_stars(land_raster,"C:\\Users\\username\\OneDrive\\Masters_project_second_semester\\maps\\integer_class_raster.tif")



#####################################################
#initialise GRASS
rgrass7::initGRASS(gisBase = "C:/Program Files/GRASS GIS 7.6",
          gisDbase = getwd(),
          location = 'grassdata',
          mapset= 'PERMANENT',
          override = TRUE,
          remove_GISRC = TRUE)



#set projection
rgrass7::execGRASS('g.proj',
                   georef = "C:\\Users\\username\\OneDrive\\Masters_project_second_semester\\maps\\sen2r_maps\\S2A2A_20190627_080_lakeDistrict_BOA_10.tif",
                   flags = c('t', 'c'))


rgrass7::execGRASS('r.in.gdal',
                   input = "C:\\Users\\username\\OneDrive\\Masters_project_second_semester\\maps\\sen2r_maps\\S2A2A_20190627_080_lakeDistrict_BOA_10.tif",                   
                   output = 'land_sentinel',
                   flags = c('o','overwrite'))




rgrass7::execGRASS("i.group",
                   group = "vis_bands",
                   subgroup = "vis_bands",
                   input = "land_sentinel.1,land_sentinel.2,land_sentinel.3,land_sentinel.4,land_sentinel.5,land_sentinel.6,land_sentinel.7,land_sentinel.8,land_sentinel.9,land_sentinel.10,land_sentinel.11",
                   flags = "r")

rgrass7::execGRASS("i.group",
                   group = "vis_bands",
                   subgroup = "vis_bands",
                   input = "land_sentinel.1,land_sentinel.2,land_sentinel.3,land_sentinel.4,land_sentinel.5,land_sentinel.6,land_sentinel.7,land_sentinel.8")


rgrass7::execGRASS('g.region', raster = 'land_sentinel.11')


#####################################################
#run machine learning

rgrass7::execGRASS('r.in.gdal',
                   input = "C:\\Users\\username\\OneDrive\\Masters_project_second_semester\\maps\\integer_class_raster.tif",                   
                   output = 'land_sample',
                   flags = c('o','overwrite'))


rgrass7::execGRASS("i.gensigset",
                   trainingmap = "land_sample" ,
                   group = "vis_bands" ,
                   subgroup = "vis_bands",
                   signaturefile = "lands_signature",
                   flags = "overwrite")

rgrass7::execGRASS("i.smap",
                   group = "vis_bands",
                   subgroup = "vis_bands",
                   signaturefile = "lands_signature",
                   output = "machine_learned_map",
                   goodness = "machine_learned_goodness",
                   blocksize = 7680,
                   flags = "overwrite")


#####################################################
#extract maps
rgrass7::execGRASS("r.out.gdal",
                   input = "machine_learned_map",
                   output = "C:\\Users\\username\\OneDrive\\Masters_project_second_semester\\maps\\machine_learned_map_20.tif",
                   format = "GTiff",
                   flags = "overwrite")


rgrass7::execGRASS("r.out.gdal",
                   input = "machine_learned_goodness",
                   output = "C:\\Users\\username\\OneDrive\\Masters_project_second_semester\\maps\\machine_learned_goodness20.tif",
                   format = "GTiff",
                   flags = "overwrite")




#####################################################
#calculate land percentages



df_machine <- raster("C:\\Users\\username\\OneDrive\\Masters_project_second_semester\\maps\\machine_learned_map_20.tif")

freq_machine <- freq(df_machine, digits=0, value=NULL, useNA='ifany', progress='text')%>%
                as.tibble(.)

freq_machine <- freq_machine %>% 
                mutate(., percentage = 100 * count/sum(freq_machine$count) )%>%
                left_join(.,land_class,by=c("value" = "class_number"))%>%
                dplyr::select(.,-value,-count)


land_original <- read_sf("C:\\Users\\username\\OneDrive\\Masters_project_second_semester\\maps\\extras\\land_vector_cut.gpkg")%>%
  st_transform(.,32630)%>%
  dplyr::select(land_type = bhab)%>%
  transmute(land_type=tolower(land_type))

land_original_class <- land_original%>%
  st_drop_geometry(.)%>%
  mutate(.,land_type = tolower(land_type))%>%
  dplyr::select(land_type)%>%
  distinct(.)%>%
  mutate(.,class_number = row_number())
  


land_original2 <- land_original%>%
  left_join(.,land_original_class, by='land_type')%>%
  dplyr::select(.,-land_type)



land_original_raster <-st_rasterize(land_original2,template=st_as_stars(st_bbox(land_original2),dx=10,dy=10 ,values=NA_real_))
write_stars(land_original_raster,"C:\\Users\\username\\OneDrive\\Masters_project_second_semester\\maps\\land_original.tif")


df_original <- raster("C:\\Users\\username\\OneDrive\\Masters_project_second_semester\\maps\\land_original.tif")
  

freq_original <- freq(df_original, digits=0, value=NULL, useNA='no', progress='text')%>%
  as.tibble(.)

freq_original <- freq_original %>% 
  mutate( percentage = 100 * count/sum(freq_original$count) )%>%
  left_join(.,land_original_class,by=c("value" = "class_number"))%>%
  dplyr::select(.,-value,-count)
freq_original$land_type[20] = "bog"
freq_original$land_type[13] = "seawater"
freq_original$land_type[4] = "urban"
freq_original$land_type[9] = "inland rock"
freq_original$land_type[17] = "water"
freq_original$land_type[8] = "littoral sediment"
freq_original$land_type[18] = "acid grassland"

freq_original2 <- aggregate(freq_original$percentage, by=list(land_type=freq_original$land_type), FUN=sum)%>%
  as.tibble()

freq_original <-dplyr::select(freq_original2,percentage = x , land_type)





beforeDataset <- freq_original %>%
  mutate(dataset = 'before') 

newDataset <- freq_machine %>%
  mutate(dataset = 'new')

fullDataset <- newDataset %>%
  rbind(beforeDataset) %>%
  filter(.,land_type != 'seawater')%>%
  group_by(.,dataset) %>%
  mutate(percentage = 100*percentage/sum(percentage))


plot <- ggplot(fullDataset, aes(x=land_type, y=percentage, colour = dataset))+
  geom_point()
plot + theme(axis.text.x = element_text(angle = 90, hjust = 1))
