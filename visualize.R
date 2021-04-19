library(readr)
library(igraph)
library(netbiov)
networkOfFollowers <- read_csv("networkOfFollowers.csv")

links <- data.frame(
  source=networkOfFollowers$source,
  target=networkOfFollowers$target
)

user1 <- ''
user2 <- ''

g <- graph_from_data_frame(d=links, directed=F) 
path <- get.shortest.paths(g, from=user1, to=user2, mode = "all")


#Visualización network usando igraph
#Representación extraía de https://stackoverflow.com/questions/22453273/how-to-visualize-a-large-network-in-r
plot(simplify(g), vertex.size= 0.01,edge.arrow.size=0.001,
     vertex.label.cex = 0.75,vertex.label.color = "black",
     vertex.frame.color = adjustcolor("white", alpha.f = 0),
     vertex.color = adjustcolor("white", alpha.f = 0),
     edge.color=adjustcolor(1, alpha.f = 0.15),
     display.isolates=FALSE,vertex.label=ifelse(page_rank(g)$vector > 0.1 , "", NA))

plot(g, vertex.size=10, vertex.label=NA)

plot(g, vertex.color="lightblue", vertex.size=10, vertex.label=NA)

#Usando librería para visualización redes biológicas complejas
gparm <- mst.plot(g, v.size=1.5,e.size=.25,
                      colors=c("red", "orange", "yellow", "green"),
                      mst.edge.col="white", layout.function=layout.fruchterman.reingold)

