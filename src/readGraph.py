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
	return graph
