import graph as G
import random
import itertools

class RandomWalk:
	
	def __init__(self,graph, nodes=1000, minP=0.0):
		self.sampleGraph = {}
		self.graph = graph
		self.nodesOriginal = G.getNodes(self.graph)
		self.edgesOriginal = G.getEdges(self.graph, weight = True)
		self.nodes = min(nodes, len(self.nodesOriginal))
		self.nodesSample = set()
		self.minP = minP #min probability required to select a edge
		self.startNode = random.choice(self.nodesOriginal)
		self.currentNode = self.startNode
		while True:
			if len(self.nodesSample) == self.nodes:
				print 'processing done'
				print self.sampleGraph
				break
			self.step()

	def step(self):
		#self.currentNode = self.startNode
		print self.currentNode
		print self.nodesSample
		self.neighbours=G.getNeighbours(self.graph, self.currentNode)
		self.chooseRandomNeighbour()

	def chooseRandomNeighbour(self):
		weights=[0]*len(self.neighbours)
		sumv = 0
		n = len(self.neighbours)
		for i in range(n):
			toNode = self.neighbours[i]
			weights[i]=G.getEdgeWeight(self.graph, self.currentNode, toNode)
			sumv+=weights[i]

		r = random.uniform(0,1)
		for i in range(n):
			weights[i]/=sumv
		s = 0
		for i in range(n):
			s+=weights[i]
			if r < s :
				self.cross(self.currentNode, self.neighbours[i], weights[i]*sumv)
				break

	def cross(self,src,dest, weight):
		self.currentNode = dest
		self.nodesSample.add(dest)
		self.nodesSample.add(src)
		if not G.addEdge(self.sampleGraph, src, dest, weight ):
			print 'not G.addEdge'
			self.startNode = random.choice(self.nodesOriginal)
		
	def sampleRW(graph, nodes=1000):
		sampleGraph = {}
		nodesOriginal = G.getNodes(graph)
		edgesOriginal = G.getEdges(graph, weight = False)
		nodesSample = set()
		startNode = random.choice(nodesOriginal)
