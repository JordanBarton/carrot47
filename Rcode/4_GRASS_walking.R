library(raster)
library(sf)
library(tidyverse)
library(rgrass7)
library(link2GI)
library(glue)
library(lubridate)
library(dplyr)

walk_path <- function(originHill, destinationHill){
 
   execGRASS('v.extract',
            input = 'coordinates',
            output = 'Origin',
            where =  paste('hillnumber == ',originHill),
            flags  = c('overwrite', 'quiet'))

  
 place = paste0(destinationHill,collapse=",")
 execGRASS('v.extract',
            input = 'coordinates',
            output = 'Destination',
            where = paste0("hillnumber IN (",place,")",sep=""),
            flags  = c('overwrite', 'quiet'))

  
  rgrass7:: execGRASS('r.walk',
                      elevation = 'elevation',
                      friction = 'friction',
                      output = 'cost_surface',
                      outdir = 'direction',
                      start_points = 'Origin',
                      stop_points =  'Destination',
                      lambda = 1, 
                      memory = 7000,
                      flags  = c('overwrite', 'quiet','k')) #insert 'k' for more accurate but slower

  
#costs#### 
  rgrass7::execGRASS('v.what.rast',
                     map = 'Destination',
                     raster = 'cost_surface',
                     column = 'cost',
                     flags  = 'quiet')

  

  
  rgrass7::execGRASS('v.db.addcolumn',
                     map = 'Destination',
                     columns = 'Origin',
                     flags  = 'quiet')
  
  
  rgrass7::execGRASS('v.db.update',
                     map = 'Destination',
                     column = 'Origin',
                     value = as.character(originHill),
                     flags  = 'quiet')
  
  print(originHill)
  print(destinationHill)
  rgrass7::execGRASS('v.db.select',
                     map = 'Destination',
                     columns = 'Origin,hillNumber,cost',
                     separator = 'comma',
                     file = paste("C:\\Users\\username\\OneDrive\\Masters_project_second_semester\\current_costs\\cost",originHill,'.csv'),
                     flags  = c('overwrite', 'quiet'))
  
  
  
  
#paths####  
  execGRASS('g.remove',
            type = 'vector',
            name = 'pathMap',
            flags = c('f','quiet'))
  
  execGRASS('r.path',
            input = 'direction',
            vector_path = 'pathMap',
            start_points = 'Destination',
            flags  = c('overwrite', 'quiet'))
  
  execGRASS('v.db.addtable',
            map = "pathMap",
            flags = 'quiet')
  execGRASS('v.db.addcolumn',
            map = "pathMap",
            columns = 'origin',
            flags = 'quiet')
  execGRASS('v.db.update',
            map = 'pathMap',
            column = 'origin',
            value = 'originHill',
            flags = 'quiet')
  
  execGRASS('v.out.ogr',
            input = 'pathMap',
            output =  paste("C:\\Users\\username\\OneDrive\\Masters_project_second_semester\\current_paths\\path",originHill,'.gpkg'),
            format = 'GPKG',
            flags  = c('overwrite', 'quiet')) 
##### 
 

  
  
  
  
  
  
#  rgrass7::execGRASS('r.out.gdal',
#                     input = 'cost_surface',
#                     output = 'cost_surface.tif',
#                     format = 'GTiff',
#                     flags  = c('overwrite', 'quiet'))
#  print('cost surface rasterised')
  
}



#initialise grass####
coordinates <-"C:\\Users\\username\\OneDrive\\Masters_project_second_semester\\maps\\extras_outer_2\\summit_positions_outer_27700.gpkg"
 
initGRASS(gisBase = "C:/Program Files/GRASS GIS 7.6",
          gisDbase = getwd(),
          location = 'grassdata',
          mapset= 'PERMANENT',
          override = TRUE,
          remove_GISRC = TRUE)



#set projection
rgrass7::execGRASS('g.proj',
                    georef = "C:\\Users\\username\\OneDrive\\Masters_project_second_semester\\maps\\extras_outer_2\\height_map_27700.tif",
                    flags = c('t', 'c'))


#load in elevation raster
rgrass7::execGRASS('r.in.gdal',
                   input = "C:\\Users\\username\\OneDrive\\Masters_project_second_semester\\maps\\extras_outer_2\\height_map_27700.tif",
                   output = 'elevation',
                   flags = c('o','overwrite'))

#"C:/Users/username/OneDrive/factory_reset_6_feb/Project/friction_3.tif"

#load in friction raster
rgrass7::execGRASS('r.in.gdal',
                   input = "C:\\Users\\username\\OneDrive\\Masters_project_second_semester\\maps\\extras_outer_2\\cost_map_outer_27700.tif",
                   output = 'friction',
                   flags = c('o','overwrite'))

#load in coordinates -> need coordinates.gpkj
rgrass7::execGRASS('v.in.ogr',
                   input = coordinates,
                   output='coordinates',
                   flags  = c('overwrite','o'))


#create the region bounded by maps
rgrass7::execGRASS('g.region', raster = 'elevation')

#walk####
#load in nearest neighbours  -> /need to enforce symmetry of matrix/
nearest_neighbours <-read_csv("C:\\Users\\username\\OneDrive\\Masters_project_second_semester\\csvs\\nearest_neighbours.csv")



#loop over all nodes up to number_of_calculations
      #taverse map (r.walk if nn )
      #export path
      #export costs
originHill <- distinct(nearest_neighbours,from)%>%
  dplyr::select(.,from)%>%
  pull(.,from)





start<-Sys.time()
for (i in 1:length(distinct(nearest_neighbours,from)$from)){


destinationHill <-  nearest_neighbours%>%
  filter(., nearest_neighbours$from == originHill[i])%>%
  dplyr::select(.,to)%>%
  pull(.,to)




walk_path(originHill[i],destinationHill)


end<-Sys.time()
print((start-end)*(length(distinct(nearest_neighbours,from)$from)-i)/i)

}
  




#merge paths
#merge costs










  