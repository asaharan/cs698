import graph as G
import randomWalk
import metric as m
filename = "../data/10000x320000.data"
nodes = 2000
graph = G.readGraph(filename)
t = randomWalk.RandomWalk(graph,nodes=nodes)
w=t.getGraph()
print "degreeDist ",m.degreeDist(w)
print "wcc ", m.wccDist(w)
