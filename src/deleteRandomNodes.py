import graph as G
import random
def deleteRandomNodes(graph, resizeRatio=0.7):
	sampleNodes = G.getNodes(graph)
	sampleNodeCount = len(sampleNodes)
	sampleGraph = graph.copy()
	nodes = sampleNodeCount
	while True:
		print sampleNodeCount, nodes
		if 1.0*sampleNodeCount/nodes <= resizeRatio:
			break
		sampleNodeCount -= 1
		randomNode=random.choice(sampleNodes)
		sampleNodes.remove(randomNode)
		G.removeNode(sampleGraph, randomNode)
	return sampleGraph

if __name__=="__main__":
	print "fetching data"
	data = G.readGraph("../data/5000x25000.data")
	print "running deleteRandomNodes"
	sample = deleteRandomNodes(data, resizeRatio=0.7)
	print "variables available globally: data, sample"
