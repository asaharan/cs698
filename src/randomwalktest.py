import graph as G
import randomWalk as r
g = G.readGraph("../data/smallGraph.data")
walk = r.RandomWalk(g,nodes=10)
