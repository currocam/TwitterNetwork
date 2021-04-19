# TwitterNetwork

Build a Twitter’s social network from followers until it finds a connection to a specified user. It was created with educational purposes.

## General info
Given a user 1 and a user 2, the script collects all the followers of user 1, the followers of his followers and so on until a match occurs with user 2.

Then, using R we characterize that connection between user 1 and user 2; and visualize the data obtained using the igraph and netbiov libraries.  

## Technologies
- Python 3.8.5
- R 4.0.4

## Network's visualization examples
- Network visualization using igraph

![igraph network visualization](igraph_network.svg)

- Network visualization using netbiov (n R package for visualizing large network data in biology and medicine)

![netbiov network visualization](netbiov_network.svg)
