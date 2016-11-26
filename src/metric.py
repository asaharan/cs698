from collections import defaultdict
import graph as G
import sys
#	for doing DFS both times while computing SCC
def dfs(graph, start, visited, stack=None, scc=None):
	visited[start] = True
	for neighbour in G.getNeighbours(graph, start):
		if not visited[neighbour]:
			dfs(graph, neighbour, visited, stack, scc)
			if scc != None:
				scc.add(neighbour)
	if stack != None:
		stack.append(start)

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

#	Weakly Connected Component distribution
def wccDist(graph):
	tempGraph = graph.copy()
	dist = defaultdict(int)
	while tempGraph:
		size = G.getWccSize(tempGraph)
		dist[size] += 1
	return dist

#	Strongly Connected Component distribution
def sccDist(graph):
	sys.setrecursionlimit(5000)
	transpose = G.computeTranspose(graph)
	nodes = G.getNodes(graph)
	visited = [False]*(sorted(nodes)[-1] + 1)
	st = []
	dist = defaultdict(int)
	for node in nodes:
		if not visited[node]:
			dfs(graph, node, visited, stack=st)
	visited = [False]*(sorted(nodes)[-1] + 1)
	while len(st) > 0:
		node = st.pop()
		newScc = set([node])
		dfs(transpose, node, visited, scc=newScc)
		dist[len(newScc)] += 1
		while len(newScc) > 0:
			val = newScc.pop()
			if val != node:
				st.remove(val)
	return dist

#	Hop-plot distribution
def hopDist(graph):
	nodes = sorted(G.getNodes(graph))
	dist = {}
	for node in nodes:
		dist[node] = {}
		for n in nodes:
			dist[node][n] = sys.maxint
	for src, dest, weight in G.getEdges(graph):
		dist[src][dest] = weight
	for node in nodes:
		dist[node][node] = 0
	for k in nodes:
		for i in nodes:
			for j in nodes:
				dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
	hop = defaultdict(int)
	for i in nodes:
		for j in nodes:
				hop[dist[i][j]] += 1
	hop.pop(sys.maxint, None)
	return hop

#	Clustering Coefficient Distribution
def clustCoff(graph):
	nodes = sorted(G.getNodes(graph))
	clustDist = dict()
	for node in nodes:
		neighbors = G.getNeighbours(graph, node)
		n_neighbors = len(neighbors)
		if n_neighbors not in clustDist.keys():
			clustDist[n_neighbors] = set()
		total = 0
		for neighbor in neighbors:
			for neighborPair in neighbors:
				if G.isNeighbour(graph, neighbor, neighborPair):
					total += 1
		if n_neighbors == 0 or n_neighbors == 1:
			clustDist[n_neighbors].add(1)
		else:
			clustDist[n_neighbors].add(total/(n_neighbors * (n_neighbors-1) * 1.0))
	return clustDist

#average in and out weight distribution
def weightDist(graph):
	inDict = defaultdict(int)
	outDict = defaultdict(int)
	inWeightDict = defaultdict(int)
	outWeightDict = defaultdict(int)
	inAvgWeightDict = defaultdict(int) #should use float
	outAvgWeightDict = defaultdict(int) #should use float
	for src, dest, weight in G.getEdges(graph, weight=True):
		inDict[dest] += 1
		inWeightDict[dest] += weight
		outDict[src] += 1
		outDict[src] += weight
	inDist = defaultdict(int)
	outDist = defaultdict(int)
	#calculating average now
	for node in inDict:
		inAvgWeightDict[node] = inWeightDict[node]/inDict[node]
	
	for node in outDict:
		outAvgWeightDict[node] = outWeightDict[node]/outDict[node]

	for node in G.getNodes(graph):
		inDist[inAvgWeightDict[node]] += 1
		outDist[outAvgWeightDict[node]] += 1
	return inDist, outDist

