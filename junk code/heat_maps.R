library(tidyverse)
library(ggplot2)
library(igraph)
library(rgrass7)
library(TSP)
library(tidyr)
library(tidygraph)
library(dplyr)
library(gplots)
library(pheatmap)


#heat maps


multmerge = function(path){
  filenames=list.files(path=path, full.names=TRUE)
  rbind_list(lapply(filenames, function(x){read.csv(x, stringsAsFactors = F, sep=',')}))
}


create_cost <- function(path){

df <- multmerge(path)


places<-dplyr::select(df,Origin,hillNumber)



edges <- merge(df,places, by=c("Origin","hillNumber"),all=TRUE) %>%
  filter(.,Origin!=hillNumber)%>%
  transmute(.,from=as.character(Origin),to=as.character(hillNumber),weight=as.integer(cost))

nodes<-dplyr::select(edges,"from")%>%
  distinct(.)


graph <- tbl_graph(nodes = nodes , edges = edges,directed=TRUE)


full_graph <- shortest.paths(graph,mode='out')


costs_tibble <- as_tibble(full_graph) }




nn14 <-create_cost("C:\\Users\\username\\OneDrive\\factory_reset_6_feb\\Project\\path_finding_data\\14nn")

nn14k <-create_cost("C:\\Users\\username\\OneDrive\\factory_reset_6_feb\\Project\\path_finding_data\\14nnk")

nn14k_cal <-create_cost("C:\\Users\\username\\OneDrive\\factory_reset_6_feb\\Project\\path_finding_data\\nn14k_cal")

nn30k_cal <-create_cost("C:\\Users\\username\\OneDrive\\factory_reset_6_feb\\Project\\path_finding_data\\nn30k_cal")

nn214k_cal <-create_cost("C:\\Users\\username\\OneDrive\\factory_reset_6_feb\\Project\\path_finding_data\\214nnk_cal")


nn14 <- nn14%>%
  as.matrix(.)
colnames(nn14) <- c(as.numeric(1:length(nn14[,1])))


pheatmap(nn14)

#heatmap(as.matrix(nn14k))


#heatmap(as.matrix(nn214k_cal))



cut<-read_csv("matrix_cut.csv")



cut<-read_csv("")





cut1<-  nn214k_cal %>%
  
  # Data wrangling
  rowid_to_column(var="X") %>%
  gather(key="Y", value="Z", -1) %>%
  
  # Change Y to numeric
  mutate(Y=as.numeric(gsub("V","",Y))) %>%
  mutate(X = factor(X),
         Y = factor(Y)) %>%
  
  # Viz
  ggplot(aes(X, Y, fill= Z)) + 
  geom_tile()









