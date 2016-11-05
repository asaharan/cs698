import random

def getNeighbours(graph, src):
	if src not in graph.keys():
		return []
	else:
		return [dest for dest, weight in graph[src]]

def isNeighbour(graph, src, dest):
	if dest in getNeighbours(graph, src):
		return True
	else:
		return False

def getEdgeWeight(graph, src, dest):
	if not isNeighbour(graph, src, dest):
		return None
	else:
		for nei, wt in graph[src]:
			if nei == dest:
				return wt

def addEdge(graph, src, dest, weight):
	flag = True
	if src in graph.keys():
		if not isNeighbour(graph, src, dest):
			graph[src].append((dest, weight))
		else:
			flag = False
	else:
		graph[src] = [(dest, weight)]
	return flag

def getNodes(graph):
	nodes = set()
	for src in graph.keys():
		nodes.add(src)
		for neighbour in getNeighbours(graph, src):
			nodes.add(neighbour)
	return list(nodes)

def getEdges(graph, weight=True):
	edges = set()
	if weight:
		for src in graph.keys():
			for dest, wt in graph[src]:
				edges.add((src, dest, wt))
	else:
		for src in graph.keys():
			for dest, wt in graph[src]:
				edges.add((src, dest))
	return list(edges)

def saveToFile(graph, path):
	fp = open(path, 'w')
	for src in graph.keys():
		for dest, weight in graph[src]:
			fp.write(str(src) + " " + str(dest) + " " + str(weight) + "\n")
	fp.close()

def generateGraph(nodes=100, edges=300, weights=50, path=None):
	graph = {}
	i = 0
	while i < edges:
		src = random.randint(1, nodes)
		dest = random.randint(1, nodes)
		weight = random.randint(1, weights)
		if addEdge(graph, src, dest, weight):
			i += 1
	if path:
		saveToFile(graph, path)
	return graph


def readGraph(path):
	graph = {}
	fp = open(path, 'r')
	for line in fp.readlines():
		data = line.split()
		start = int(data[0])
		dest = int(data[1])
		weight = int(data[2])
		if start in graph.keys():
			graph[start].append((dest, weight))
		else:
			graph[start] = [(dest, weight)]
	fp.close()
	return graph