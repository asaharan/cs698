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
	for src in nodesSample:
		if src in graph.keys():
			for dest, weight in graph[src]:
				if dest in nodesSample:
					G.addEdge(sampleGraph, src, dest, weight)
	return sampleGraph
