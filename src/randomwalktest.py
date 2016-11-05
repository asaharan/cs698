import graph as G
import randomWalk as r
filename = "../data/10000x320000.data"
nodes = 100
g = G.readGraph(filename)
w = r.RandomWalk(g,nodes=nodes)
