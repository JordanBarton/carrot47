library(tidyverse)
library(ggplot2)
library(igraph)
library(rgrass7)
library(TSP)
library(tidyr)
library(tidygraph)
library(dplyr)

#create full tidy cost matrix####

multmerge = function(path){
  filenames=list.files(path=path, full.names=TRUE)
  rbind_list(lapply(filenames, function(x){read.csv(x, stringsAsFactors = F, sep=',')}))
}

df <- multmerge("C:\\Users\\username\\OneDrive\\Masters_project_second_semester\\processed_costs\\outer_costs")



places<-dplyr::select(df,Origin,hillnumber)



edges <- merge(df,places, by=c("Origin","hillnumber"),all=TRUE) %>%
  filter(.,Origin!=hillnumber)%>%
  transmute(.,from=as.character(Origin),to=as.character(hillnumber),weight=as.integer(cost))
  


nodes<-dplyr::select(edges,"from")%>%
  distinct(.)

  
graph <- tbl_graph(nodes = nodes , edges = edges,directed=TRUE)


full_graph <- shortest.paths(graph,mode='out')


costs_tibble <- as_tibble(full_graph)


#solve salesman####

costs<- as.matrix(costs_tibble) %>%
  as.ATSP(.) %>%
  reformulate_ATSP_as_TSP(.) %>%
  TSP(.) %>%
  TSP::solve_TSP(.)





places_full <- dplyr::select(df,Origin)%>%
  distinct(.)%>%
  mutate(.,i=1)%>%
  left_join(.,., by="i")%>%
  dplyr::select(Origin = Origin.x,hillNumber = Origin.y)%>%
  mutate(.,row=row_number())



costs_tidy <- pivot_longer(costs_tibble,cols = starts_with("V"), names_to = "to", values_to = "time")%>%
  mutate(.,row=row_number())%>%
  left_join(.,places_full,by = "row")%>%
  dplyr::select("from"=Origin,to=hillNumber,time=time)

write_csv(costs_tidy,"C:\\Users\\username\\OneDrive\\Masters_project_second_semester\\processed_costs\\outer_costs\\tidy.csv")


#####
tour_order <- costs %>%
  as.integer() %>%
  enframe(name=NULL)%>%
  filter(value<=214)

nodes<-mutate(nodes,row=row_number())



hill_order <- left_join(tour_order,nodes, by = c('value' = 'row'))%>%
  mutate(., to=lead(from))%>%
  transmute(from=as.numeric(from),to=as.numeric(to))%>%
  left_join(.,costs_tidy,by = c("to"="to","from"="from"))

print(sum(hill_order$time,na.rm=TRUE))
#try to calculate using TSP::tour_length  





TSP::concorde_path("C:/Users/username/Desktop/concorde")
costs<-as.matrix(costs_tibble)
colnames(costs) <- c(as.numeric(1:length(costs[,1])))
costs <-costs %>%
  as.ATSP(.) %>%
  reformulate_ATSP_as_TSP(.) %>%
  TSP(.) %>%
  solve_TSP(.,method="concorde", precision = 0)
######




