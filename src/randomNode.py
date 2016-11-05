import graph as G
import random
import itertools

def sampleRN(graph, nodes=1000):
	sampleGraph = {}
	nodesOriginal = G.getNodes(graph)
	edgesOriginal = G.getEdges(graph, weight=False)
	nodesSample = set()
	size = min(nodes, len(nodesOriginal))
	while(len(nodesSample) < size):
		nodesSample.add(random.choice(nodesOriginal))
	nodesSample = list(nodesSample)
	edges = 0
	for pair in itertools.product(nodesSample, repeat=2):
		edge = (pair[0], pair[1])
		if edge in edgesOriginal:
			G.addEdge(sampleGraph, pair[0], pair[1], G.getEdgeWeight(graph, pair[0], pair[1]))
	return sampleGraph
