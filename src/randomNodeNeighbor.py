import graph as G
import random
def randomNodeNeighbor(graph, nodes=1000):
	nodes = min(nodes, len(G.getEdges(graph)))
	#dataNodes = G.getNodes(getEdges)
	sampleGraph = {}
	sampleNodes = {}
	while True:
		if len(G.getNodes(sampleGraph)) >= nodes:
			break
		randomNode = random.choice(graph.keys())
		sampleGraph[randomNode] = graph[randomNode]
	
	return sampleGraph

if __name__ == "__main__":
	print "fetching data"
	data = G.readGraph("../data/5000x25000.data")
	print "running randomNodeNeighbor"
	sample = randomNodeNeighbor(data)
	print "vars: data, sample "

