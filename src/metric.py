from collections import defaultdict
import graph as G

#	In and Out Degree distribution
def degreeDist(graph, sample):
	originalDistIn = defaultdict(int)
	originalDistOut = defaultdict(int)
	sampleDistIn = defaultdict(int)
	sampleDistOut = defaultdict(int)
	for src, dest in G.getEdges(graph, weight=False):
		originalDistIn[dest] += 1
		originalDistOut[src] += 1
	for src, dest in G.getEdges(sample, weight=False):
		sampleDistIn[dest] += 1
		sampleDistOut[src] += 1
	return originalDistIn, originalDistOut, sampleDistIn, sampleDistOut
