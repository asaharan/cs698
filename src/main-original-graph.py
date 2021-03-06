import graph as G
import metric as M
import randomEdge as RE
import randomNode as RN
import randomNodeNeighbor as RNN
import randomWalk as RW
import json

path = "../data/smallGraph.data"
#path = "../data/smallGraph.data"
numNodes = 1000

fid = open("../out-final/inDegreeDist-original-graph.out", "w")
fod = open("../out-final/outDegreeDist-original-graph.out", "w")
fwcc = open("../out-final/wccDist-original-graph.out", "w")
fscc = open("../out-final/sccDist-original-graph.out", "w")
fhop = open("../out-final/hopDist-original-graph.out", "w")
fclust = open("../out-final/clustDist-original-graph.out", "w")


print "Reading graph..."
graph = G.readGraph(path)
# print "Generating samples..."
# print "\t* using random edge"
# sampleRE = RE.randomEdge(graph, nodes=numNodes)
# print "\t* using random node"
# sampleRN = RN.sampleRN(graph, nodes=numNodes)
# print "\t* using random node neighbour"
# sampleRNN = RNN.randomNodeNeighbor(graph, nodes=numNodes)
# print "\t* using random walk"
# rw = RW.RandomWalk(graph, nodes=numNodes)
# sampleRW = rw.getGraph()

def getAlgo(num):
	if num == 1:
		return "random edge"
	elif num == 2:
		return "random node"
	elif num == 3:
		return "random node neighbour"
	elif num == 4:
		return "random walk"

print "Computing metrics..."
for sample, num in zip([graph],range(1,5)):
	algo = getAlgo(num)
	ans = {}
	print "\t* In and Out degree distribution for " + algo
	dd = M.degreeDist(sample)
	ans[algo] = dd[0]
	fid.write(json.dumps(ans) + "\n\n")
	ans[algo] = dd[1]
	fod.write(json.dumps(ans) + "\n\n")
	print "\t* WCC distribution for " + algo
	ans[algo] = M.wccDist(sample)
	fwcc.write(json.dumps(ans) + "\n\n")
	print "\t* SCC distribution for " + algo
	ans[algo] = M.sccDist(sample)
	fscc.write(json.dumps(ans) + "\n\n")
	print "\t* Hop distribution for " + algo
	ans[algo] = M.hopDist(sample)
	fhop.write(json.dumps(ans) + "\n\n")
	print "\t* Clustering coefficient distribution for " + algo
	ans[algo] = M.clustCoff(sample)
	fclust.write(str(ans) + "\n\n")

fid.close()
fod.close()
fwcc.close()
fscc.close()
fhop.close()
fclust.close()
