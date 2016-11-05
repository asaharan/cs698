from collections import defaultdict
import graph as G

#	In and Out Degree distribution
def degreeDist(graph):
	inDict = defaultdict(int)
	outDict = defaultdict(int)
	for src, dest in G.getEdges(graph, weight=False):
		inDict[dest] += 1
		outDict[src] += 1
	inDist = defaultdict(int)
	outDist = defaultdict(int)
	for node in G.getNodes(graph):
		inDist[inDict[node]] += 1
		outDist[outDict[node]] += 1
	return inDist, outDist
