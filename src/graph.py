import random

def generateGraph(nodes=100, edges=300, path=None):
	graph = {}
	i = 0
	while i < edges:
		src = random.randint(1, nodes)
		dest = random.randint(1, nodes)
		if src in graph.keys():
			if dest not in graph[src]:
				graph[src].add(dest)
				i += 1
		else:
			graph[src] = set([dest])
			i += 1
	if path:
		fp = open(path, 'w')
		for src in graph.keys():
			for dest in graph[src]:
				fp.write(str(src) + " " + str(dest) + "\n")
		fp.close()
	return graph


def readGraph(path):
	graph = {}
	fp = open(path, 'r')
	for line in fp.readlines():
		data = line.split()
		start = int(data[0])
		dest = int(data[1])
		if start in graph.keys():
			graph[start].add(dest)
		else:
			graph[start] = set([dest])
	fp.close()
	return graph
