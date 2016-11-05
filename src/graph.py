import random

def getNeighbours(graph, src):
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

def generateGraph(nodes=100, edges=300, weights=50, path=None):
	graph = {}
	i = 0
	while i < edges:
		src = random.randint(1, nodes)
		dest = random.randint(1, nodes)
		weight = random.randint(1, weights)
		if src in graph.keys():
			if not isNeighbour(graph, src, dest):
				graph[src].append((dest, weight))
				i += 1
		else:
			graph[src] = [(dest, weight)]
			i += 1
	if path:
		fp = open(path, 'w')
		for src in graph.keys():
			for dest, weight in graph[src]:
				fp.write(str(src) + " " + str(dest) + " " + str(weight) + "\n")
		fp.close()
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
