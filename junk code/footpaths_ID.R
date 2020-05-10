library(tidyverse)
library(sf)
library(raster)
library(stars)


highways <- read_sf("C:\\Users\\username\\OneDrive\\Masters_project_second_semester\\maps\\extras_outer_2\\footpath_map_outer.gpkg")%>%
  st_transform(.,27700)%>%
  dplyr::select(.,uri=osm_id,sac_scale,tracktype,highway,surface)%>%
  mutate(.,ID1 = case_when(sac_scale == "hiking" ~ "A",
                           sac_scale == "mountain_hiking" ~ "B",
                           sac_scale == "demanding_mountain_hiking" ~ "C",
                           sac_scale == "hiking; mountain_hiking" ~ "D",
                           sac_scale == "mountain_hiking;hiking" ~ "F",
                           sac_scale == "undefined" ~ "0",
                           sac_scale == "mountain_hiking; hiking" ~ "G",
                           sac_scale == "demanding_alpine_hiking" ~ "H",
                           sac_scale == "alpine_hiking" ~ "I",
                           sac_scale == "difficult_alpine_hiking" ~ "J",
                           TRUE ~ "0"))%>%
  mutate(.,ID2 = case_when(tracktype == "grade1" ~ "A",
                           tracktype == "grade2" ~ "B",
                           tracktype == "grade3;grade2" ~ "C",
                           tracktype == "grade3" ~ "D",
                           tracktype == "grade4" ~ "F",
                           tracktype == "grade5" ~ "G",
                           tracktype == "grade6" ~ "H",
                           tracktype == "" ~ "I",
                           TRUE ~ "0"))%>%
  mutate(.,ID3 = case_when(highway == "trunk" ~ "A",
                           highway == "secondary" ~ "B",
                           highway == "path" ~ "C",
                           highway == "footway" ~ "D",
                           highway == "bridleway" ~ "F",
                           highway == "residential" ~ "G",
                           highway == "motorway_link" ~ "H",
                           highway == "motorway" ~ "I",
                           highway == "track" ~ "J",
                           highway == "tertiary" ~ "K",
                           highway == "service" ~ "L",
                           highway == "primary" ~ "M",
                           highway == "cycleway" ~ "N",
                           highway == "steps" ~ "O",
                           highway == "trunk_link" ~ "P",
                           highway == "primary_link" ~ "Q",
                           highway == "pedestrian" ~ "R",
                           highway == "secondary_link" ~ "S",
                           highway == "byway" ~ "T",
                           highway == "tertiary_link" ~ "U",
                           highway == "construction" ~ "V",
                           highway == "proposed" ~ "W",
                           highway == "raceway" ~ "X",
                           highway == "road" ~ "Y",
                           highway == "corridor" ~ "Z",
                           highway == "living_street" ~ "1",
                           highway == "unclassified" ~ "0",
                           TRUE ~ "0"))%>%
  mutate(.,ID4 = case_when(surface == "" ~ "0",
                           surface == "asphalt" ~ "A",
                           surface == "compacted" ~ "B",
                           surface == "gravel" ~ "C",
                           surface == "unpaved" ~ "D",
                           surface == "paved" ~ "F",
                           surface == "grass" ~ "G",
                           surface == "rock" ~ "H",
                           surface == "sett" ~ "I",
                           surface == "ground" ~ "J",
                           surface == "mud" ~ "K",
                           surface == "wood" ~ "L",
                           surface == "concrete" ~ "M",
                           surface == "stone" ~ "N",
                           surface == "dirt" ~ "O",
                           surface == "cobblestone" ~ "P",
                           surface == "paved;gravel" ~ "Q",
                           surface == "paving_stones" ~ "R",
                           surface == "pebblestone" ~ "S",
                           surface == "earth" ~ "T",
                           surface == "boggy" ~ "U",
                           surface == "metal" ~ "V",
                           surface == "sand" ~ "W",
                           surface == "Degrading_from_asphalt_to_overgrown_track" ~ "X",
                           surface == "river bed" ~ "Y",
                           surface == "stepping stone" ~ "Z",
                           surface == "Variable," ~ "1",
                           surface == "Soft_grass" ~ "2",
                           surface == "Rough_but_hard" ~ "3",
                           surface == "soft_grass" ~ "4",
                           surface == "slate" ~ "5",
                           surface == "grass_paver" ~ "6",
                           surface == "fine_gravel" ~ "7",
                           surface == "stone_slabs" ~ "8",
                           surface == "scree" ~ "9",
                           TRUE ~ "0"))%>%
  mutate(., ID = paste0(ID1,ID2,ID3,ID4))
  

highways_reduced <- highways%>%
  dplyr::select(.,uri,ID)




lookup_table <- highways %>%
  st_drop_geometry(.)%>%
  dplyr::select(.,ID,ID1,ID2,ID3,ID4,sac_scale,tracktype,highway,surface)%>%
  distinct()

write_csv(lookup_table,"C:\\Users\\username\\OneDrive\\Masters_project_second_semester\\path_lookup_table.csv")

cost_table <- read_csv("C:\\Users\\username\\OneDrive\\Masters_project_second_semester\\path_costs.csv")



sac_scale_cost <- highways%>%
  dplyr::select(.,uri,sac_scale)%>%
  left_join(.,cost_table,by = "sac_scale")%>%
  dplyr::select(.,uri,score)%>%
  st_drop_geometry()

highway_cost <- highways%>%
  dplyr::select(.,uri,highway)%>%
  left_join(.,cost_table,by = "highway")%>%
  dplyr::select(.,uri,score)%>%
  st_drop_geometry()


tracktype_cost <- highways%>%
  dplyr::select(.,uri,tracktype)%>%
  left_join(.,cost_table,by = "tracktype")%>%
  dplyr::select(.,uri,score)%>%
  st_drop_geometry()


surface_cost <- highways%>%
  dplyr::select(.,uri,surface)%>%
  left_join(.,cost_table,by = "surface")%>%
  dplyr::select(.,uri,score)%>%
  st_drop_geometry()


df <- left_join(sac_scale_cost,highway_cost , by = "uri")%>%
      left_join(.,tracktype_cost , by = "uri")%>%
      left_join(.,surface_cost , by = "uri")

DF<- df%>%
  mutate_all(~replace(., is.na(.), 0))%>%
  mutate(., score_total = 1*score.x + 1*score.y + 1*score.x.x + 1*score.y.y)%>%
  dplyr::select(.,uri,score_total)


df_undefined <- filter(DF, score_total == 0 )

df_defined <- filter(DF, score_total != 0 )

df_redefined <- df_undefined %>%
  mutate(.,score_total = mean(df_defined$score_total))

total_df <-  left_join(highways,rbind(df_defined,df_redefined),by = "uri")%>%
  dplyr::select(.,uri,ID,score_total,geom)
  

write_sf(total_df,"C:\\Users\\username\\OneDrive\\Masters_project_second_semester\\reduced_paths.gpkg")



      
  

