import graph as G
import random
def deleteRandomEdges(graph, resizeRatio=0.7):
	sampleGraph = graph.copy()
	sampleEdges = G.getEdges(sampleGraph)
	edges = len(sampleEdges)
	sampleEdgeCount = edges
	while True:
		#print sampleEdgeCount, edges
		if 1.0*sampleEdgeCount/edges <= resizeRatio:
			break
		sampleEdgeCount -= 1
		randomEdge = random.choice(sampleEdges)
		sampleEdges.remove(randomEdge)
		G.removeEdge(sampleGraph, randomEdge[0], randomEdge[1])
	return sampleGraph

if __name__ == "__main__":
	print "fetching data"
	data = G.readGraph("../data/5000x25000.data")
	d = G.readGraph("../data/5000x25000.data")
	l = len(G.getEdges(data))
	print "running deleteRandomEdges"
	sample = deleteRandomEdges(d.copy(), resizeRatio=0.7)
	print "variables available globally: data, sample"
	print l, len(G.getEdges(sample)), len(G.getEdges(data))
