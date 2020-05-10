#similariy of routes
library(sp)
library(tidyverse)
library(dplyr)
library(sf)
library(raster)
library(stars)
library(ggplot2)
library(directlabels)
library(tcltk)



read_route <- function(dir , FILENAME ){
  route5<-read_sf(paste0(dir,FILENAME))%>%
  st_transform(.,32630)%>%
 # st_reverse(geom)%>%
  st_cast("POINT")%>%
  group_by(. , order)%>%
  mutate(.,ID = row_number())%>%
  ungroup(.)%>%
  arrange(. , order, ID)
  }

height_profiles <- function(dir , route , height_map , chain_limit ){

  #extract along route
  height_route <- route %>% 
                 mutate(distance = as.numeric(st_distance(geom, lead(geom, default = EMPTY), by_element = TRUE)))%>%
                 mutate(height = raster_extract(x = height_map, y = geom))
  
  height_route2 <- height_route%>%
                 filter(. , distance < 12) %>%
                 group_by(.,order)%>%
                 mutate(., distance_travelled = cumsum(distance))

  
 
  # create progress bar
  max_progress =  length(running_variable$from)
  pb <- tkProgressBar(title = "progress bar", min = 0,
                      max = max_progress, width = 300)
  
  #create folder
  folder =  paste0(dir,"height_profiles_",deparse(substitute(route)))
  dir.create(folder)
  
  number_of_peaks = max(distinct(dplyr::select(as_data_frame(height_route),order)))
  total_ascent = 0
  for (i in 1:number_of_peaks){
    
    temp <- filter(height_route2 , order == i)%>%
            filter(. , ID <= dim(.)[1]/2)%>%
            mutate(. , height = rev(height))%>%
            mutate(. , gain = lead(height)-height)%>%
            mutate(., slope = atan(gain/distance)*180/pi)
     #   %>%            mutate(. , step_change = ID-lag(ID))%>%
     #               mutate(. , include = as.numeric(step_change >1))
     #temp$include[1] = 0 # need to get rid of NA from lag
    
#    temp2 <- temp%>%
#      mutate(. , chain_number = cumsum(include))%>%
#      group_by(. , chain_number)%>%
#      mutate(. , chain_gain = sum(gain))%>%
#      filter(. , chain_gain > chain_limit)%>%
#      dplyr::select(.,chain_gain)%>%
#      distinct(.)
#     ascent = round( sum(height_gain2$chain_gain) , digits = 2)
    temp2<- temp%>%
             filter(. , gain>0)
    ascent = round(sum(temp2$gain),0)
    
    
    ggplot(temp, aes(x = distance_travelled, y= height))+
      geom_smooth()+
      geom_dl(label=ascent, method="smart.grid", inherit.aes=T)
    theme(axis.text.x = element_text(angle = 45, hjust = 1))
    ggsave(file = paste0(folder,"\\height_profile",as.character(temp$from[1]),"_",as.character(temp$to[1]),".png"))
    
    
    ggplot(temp, aes(x = distance_travelled, y=slope))+
      geom_smooth()+
      theme(axis.text.x = element_text(angle = 0, hjust = 1))     
    ggsave(file = paste0(folder,"\\","slope_profile",as.character(temp$from[1]),"_",as.character(temp$to[1]) , ".png"))


    
    print(ascent)
    print(paste0(folder,as.character(temp$from[1]),"_",as.character(temp$to[1]),".png"))
    total_ascent = total_ascent + ascent
    
    
    Sys.sleep(0.1)
    setTkProgressBar(pb, i, label=paste( round(i/number_of_peaks*100, 0),"% done"))
    
    
  }#end of loop
  close(pb)
  print(total_ascent)
  
  
  info <- data_frame(total_ascent,chain_limit)
  write_csv(info , path = paste0(folder,"\\","info.csv"))
  
  write_csv(height_route , path = paste0(folder,"\\","height_route.csv"))
  
}#end of function

land_distribution <- function(dir, route, land_map){
      
  
                    land_route <- route %>% 
                                  mutate(distance = as.numeric(st_distance(geom, lead(geom, default = EMPTY), by_element = TRUE)))%>%
                                  mutate(land = raster_extract(x = land_map, y = geom))
  

                      
                    frequency <- land_route%>%
                                   as_tibble(.)%>%
                                   dplyr::select(. , land )%>%
                                   as_data_frame(.)%>%
                                   add_count(.$land)%>%
                                   distinct()%>%
                                   dplyr::select(. , land , n)%>%
                                   mutate(. , fraction = 100* n/sum(n))%>%
                                   left_join(. , land_type_look_up , by = c("land" = "class_number"))
                      
                      
                      ggplot(frequency, aes(x=land_type, y=fraction))+
                             geom_point()+
                             geom_text(aes(label=n),size=2.5,hjust=-0.1, vjust=0)+
                             theme(axis.text.x = element_text(angle = 45, hjust = 1))
                        
                      
                      folder =  paste0(dir,"land_distribution_",deparse(substitute(route)))
                      dir.create(folder)
                      
                      ggsave(file = paste0(folder,"\\","land_distribution.png"))
                      write_csv(frequency , path = paste0(folder,"\\","info.csv"))
                      
     
                      }#end of function

cost_distribution <- function(dir , route, cost_map){
  
  
    cost_route <- route %>% 
                  mutate(distance = as.numeric(st_distance(geom, lead(geom, default = EMPTY), by_element = TRUE)))%>%
                  mutate(cost = raster_extract(x = cost_map, y = geom))
  
   
   
 
    frequency_cost <- cost_route %>%
                      as_tibble(.)%>%
                      dplyr::select(.,-geom)%>%
                      add_count(.$cost)%>%
                      mutate(. , cost = round( cost, digits = 1 ))%>%
                      dplyr::select(. , cost , n)%>%
                      distinct()%>%
                      mutate(. , fraction = 100* n/sum(n))%>%
                      arrange(. , cost )
    

    folder =  paste0(dir,"cost_distribution_",deparse(substitute(route)))
    dir.create(folder)
    write_csv(frequency_cost , path = paste0(folder,"\\","info.csv"))
    
    ggplot(frequency_cost, aes(x = cost, y=fraction))+
          geom_point()+
          geom_text(aes(label=n),size=2.5,hjust=-0.1, vjust=0)+
          theme(axis.text.x = element_text(angle = 0, hjust = 1))+
          labs(x = "log(cost)", y = "percentage")+
          scale_x_continuous(trans = "log2")
    ggsave(file = paste0(folder,"\\","cost_distribution_logx.png"))
    
    ggplot(frequency_cost, aes(x = as.character(cost), y=fraction))+
          geom_point()+
          geom_text(aes(label=n),size=2.5,hjust=-0.1, vjust=0)+
          theme(axis.text.x = element_text(angle = 45, hjust = 1))+
          labs(x = "cost", y = "percentage")
    ggsave(file = paste0(folder,"\\","cost_distribution_charx.png"))
    
    
    ggplot(frequency_cost, aes(x = cost, y=fraction))+
           geom_point()+
           geom_text(aes(label=n),size=2.5,hjust=-0.1, vjust=0)+
           theme(axis.text.x = element_text(angle = 0, hjust = 1))+
           labs(x = "cost", y = "percentage") +      
           scale_x_continuous(limits = c(0,30))
    ggsave(file = paste0(folder,"\\","cost_distribution_cutx.png"))
    
    
}#end of function

similarity <- function(route_A,route_B){
  df <- left_join(as_data_frame(sapply(route_A, as.character)),
                  as_data_frame(sapply(route_B, as.character)),
                  by = c("from","to"))%>%
                  filter(!is.na(order.y))%>%
                  dplyr::select( . ,from , to , order = order.x)
  print(paste0("similarity = " , as.character(100 * dim(df)[1]/dim(route_A)[1]) , "%"))
  
  return(df)
}#end of function

raster_extract = function(x, y, fun = NULL, na.rm = FALSE , along = FALSE) {
  x = as(x, "Raster")
  y = as(y, "Spatial")
  raster::extract(x = x, y = y, fun = fun, na.rm = na.rm, along = along )
}



EMPTY <- st_as_sfc("POINT(EMPTY)")
dir = "C:\\Users\\username\\OneDrive\\Masters_project_second_semester\\routes\\"


route1 <- read_route(dir,"route_paul.gpkg")#paul

route2 <- read_route(dir,"route_old.gpkg")#sem1

route3 <- read_route(dir,"route_machine.gpkg")#old r.walk new friction

route4 <- read_route(dir,"route_old_outer.gpkg")#old r.walk new friction outer

route5 <- read_route(dir,"route_outer_0067.gpkg")#old r.walk lambda=0.067 new friction

route6 <- read_route(dir,"route_new_0067.gpkg")#new r.walk lambda = 0.067

route7 <- read_route(dir,"route_new_0133.gpkg")#new r.walk lambda = 0.133

route8 <- read_route(dir,"route_new_outer_0067.gpkg")#new r.walk lambda = 0.067 outer

route9 <- read_route(dir,"route_new_outer_0133.gpkg")#new r.walk lambda = 0.133 outer


land_map <- raster::raster("C:\\Users\\username\\OneDrive\\Masters_project_second_semester\\maps\\extras_outer_2\\machine_learned_map.tif")

height_map <- raster::raster("C:\\Users\\username\\OneDrive\\Masters_project_second_semester\\maps\\extras_outer_2\\height_map_27700.tif")

cost_map <- raster::raster("C:\\Users\\username\\OneDrive\\Masters_project_second_semester\\maps\\extras_outer_2\\cost_map_final.tif")

land_type_look_up <- read_csv("C:\\Users\\username\\OneDrive\\Masters_project_second_semester\\csvs\\land_type_lookup_table.csv")

costs_look_up <- read_csv("C:\\Users\\username\\OneDrive\\Masters_project_second_semester\\csvs\\costs_look_up_table.csv")



land_distribution(dir,route1,land_map)
cost_distribution(dir,route1,cost_map)
height_profiles(dir,route1,height_map,1)



land_distribution(dir,route2,land_map)
cost_distribution(dir,route2,cost_map)
height_profiles(dir,route2,height_map,1)


land_distribution(dir,route3,land_map)
cost_distribution(dir,route3,cost_map)
height_profiles(dir,route3,height_map,1)


land_distribution(dir,route4,land_map)
cost_distribution(dir,route4,cost_map)
height_profiles(dir,route4,height_map,1)


land_distribution(dir,route5,land_map)
cost_distribution(dir,route5,cost_map)
height_profiles(dir,route5,height_map,1)


land_distribution(dir,route6,land_map)
cost_distribution(dir,route6,cost_map)
height_profiles(dir,route6,height_map,1)


land_distribution(dir,route7,land_map)
cost_distribution(dir,route7,cost_map)
height_profiles(dir,route7,height_map,1)


land_distribution(dir,route8,land_map)
cost_distribution(dir,route8,cost_map)
height_profiles(dir,route8,height_map,1)



land_distribution(dir,route9,land_map)
cost_distribution(dir,route9,cost_map)
height_profiles(dir,route9,height_map,1)



total_cost1<-dplyr::select(route1,from,to,cost)%>%distinct()









fundamental_paths <- similarity(route2,route3)%>%
                     similarity(route4)%>%
                     similarity(route6)%>%
                     similarity(route7)%>%
                     similarity(route8)%>%
                     similarity(route9)




