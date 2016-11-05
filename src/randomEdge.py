import graph as G
import random
def randomEdge(graph, nodes=1000):
	edges = G.getEdges(graph, weight=True)
	nodes = min(nodes, G.getNodes(graph))
	sampleGraph = {}
	sampleEdges = set()
	while True:
		edge=random.choice(edges)
		if not edge in sampleEdges:		
			G.addEdge(sampleGraph,edge[0],edge[1],edge[2])
			sampleEdges.add(edge)
		if len(G.getNodes(sampleGraph)) == nodes:
			break
	return sampleGraph
