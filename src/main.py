import graph as G
import metric as M
import randomEdge as RE
import randomNode as RN
import randomNodeNeighbor as RNN
import randomWalk as RW

path = "../data/smallGraph.data"
numNodes = 10

fid = open("../out/inDegreeDist.out", "w")
fod = open("../out/outDegreeDist.out", "w")
fwcc = open("../out/wccDist.out", "w")
fscc = open("../out/sccDist.out", "w")
fhop = open("../out/hopDist.out", "w")
fclust = open("../out/clustDist.out", "w")


print "Reading graph..."
graph = G.readGraph(path)
print "Generating samples..."
print "\t* using random edge"
sampleRE = RE.randomEdge(graph, nodes=numNodes)
print "\t* using random node"
sampleRN = RN.sampleRN(graph, nodes=numNodes)
print "\t* using random node neighbour"
sampleRNN = RNN.randomNodeNeighbor(graph, nodes=numNodes)
print "\t* using random walk"
rw = RW.RandomWalk(graph, nodes=numNodes)
sampleRW = rw.getGraph()

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
for sample, num in zip([sampleRE, sampleRN, sampleRNN, sampleRW],range(1,5)):
	algo = getAlgo(num)
	ans = {}
	print "\t* In and Out degree distribution for " + algo
	dd = M.degreeDist(sample)
	ans[algo] = dd[0]
	fid.write(str(ans) + "\n\n")
	ans[algo] = dd[1]
	fod.write(str(ans) + "\n\n")
	print "\t* WCC distribution for " + algo
	ans[algo] = M.wccDist(sample)
	fwcc.write(str(ans) + "\n\n")
	print "\t* SCC distribution for " + algo
	ans[algo] = M.sccDist(sample)
	fscc.write(str(ans) + "\n\n")
	print "\t* Hop distribution for " + algo
	ans[algo] = M.hopDist(sample)
	fhop.write(str(ans) + "\n\n")
	print "\t* Clustering coefficient distribution for " + algo
	ans[algo] = M.clustCoff(sample)
	fclust.write(str(ans) + "\n\n")

fid.close()
fod.close()
fwcc.close()
fscc.close()
fhop.close()
fclust.close()
