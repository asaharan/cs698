import graph as G
import random
import itertools

class RandomWalk:
	
	def __init__(self,graph, nodes=1000, minP=0.0,weights=True):
		self.sampleGraph = {}
		self.graph = graph
		self.weights=weights
		self.nodesOriginal = G.getNodes(self.graph)
		self.edgesOriginal = G.getEdges(self.graph, weight = True)
		self.nodes = min(nodes, len(self.nodesOriginal))
		self.nodesSample = set()
		self.minP = minP #min probability required to select a edge
		self.startNode = random.choice(self.nodesOriginal)
		self.currentNode = self.startNode
		while True:
			if len(self.nodesSample) == self.nodes:
				#print 'processing done'
				#print self.sampleGraph
				break
			self.neighbours=G.getNeighbours(self.graph, self.currentNode)
			self.chooseRandomNeighbour()
			#self.step()
	
	def getGraph(self):
		return self.sampleGraph
	
	def step(self):
		#self.currentNode = self.startNode
		#print self.currentNode
		#print self.nodesSample
		self.neighbours=G.getNeighbours(self.graph, self.currentNode)
		self.chooseRandomNeighbour()

	def chooseRandomNeighbour(self):
		weights=[0.0]*len(self.neighbours)
		if self.weights == False:
			weights=[1.0]*len(self.neighbours)
			pass	
		sumv = 0
		n = len(self.neighbours)
		if self.weights == True:
			for i in range(n):
				toNode = self.neighbours[i]
				weights[i]=G.getEdgeWeight(self.graph, self.currentNode, toNode)
				sumv+=weights[i]

		#print weights
		r = random.uniform(0,1)
		for i in range(n):
			#print weights[i],'/',sumv,'='
			weights[i]/=sumv*1.0
			#print weights[i],' sa'
		s = 0
		stra = ''
		called = False
		for i in range(n):
			s+=weights[i]
			stra += str(r)+','+str(s)+','+str(weights[i])+';'
			if r < s :
				called = True
				self.cross(self.currentNode, self.neighbours[i], weights[i]*sumv)
				break
		if called:
			#print "called"
			pass
		else:
			#now we need to update start or retry start
			self.updateStartAndCurrent()
			#print "not called",stra

	def updateStartAndCurrent(self):
		self.startNode = random.choice(self.nodesOriginal)
		self.currentNode = self.startNode

	def cross(self,src,dest, weight):
		self.currentNode = dest
		self.nodesSample.add(dest)
		self.nodesSample.add(src)
		if not G.addEdge(self.sampleGraph, src, dest, weight ):
			#print 'not G.addEdge'
			self.updateStartAndCurrent()
			#self.startNode = random.choice(self.nodesOriginal)
			#self.currentNode = startNode
		else:
			#print src, dest,"added to G"
			#print self.sampleGraph
			pass
