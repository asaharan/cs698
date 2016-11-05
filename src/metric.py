import graph as G

#	Out-degree distribution
def s2(graph, sample):
	originalDist = {}
	sampleDist = {}
	for src in graph.keys():
		degree = len(graph[src])
		if degree in originalDist.keys():
			originalDist[degree] += 1
		else:
			originalDist[degree] = 1
	for src in sample.keys():
		degree = len(sample[src])
		if degree in sampleDist.keys():
			sampleDist[degree] += 1
		else:
			sampleDist[degree] = 1
	return originalDist, sampleDist
