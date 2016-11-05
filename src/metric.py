from collections import defaultdict
import graph as G

#	In and Out Degree distribution
def degreeDist(graph, sample):
	originalDictIn = defaultdict(int)
	originalDictOut = defaultdict(int)
	sampleDictIn = defaultdict(int)
	sampleDictOut = defaultdict(int)
	for src, dest in G.getEdges(graph, weight=False):
		originalDictIn[dest] += 1
		originalDictOut[src] += 1
	for src, dest in G.getEdges(sample, weight=False):
		sampleDictIn[dest] += 1
		sampleDictOut[src] += 1
	originalIn = defaultdict(int)
	originalOut = defaultdict(int)
	sampleIn = defaultdict(int)
	sampleOut = defaultdict(int)
	for node in G.getNodes(graph):
		originalIn[originalDictIn[node]] += 1
		originalOut[originalDictOut[node]] += 1
	for node in G.getNodes(sample):
		sampleIn[sampleDictIn[node]] += 1
		sampleOut[sampleDictOut[node]] += 1
	return originalIn, originalOut, sampleIn, sampleOut
