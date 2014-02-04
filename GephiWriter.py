import xml.etree.ElementTree as et

class GephiWriter(object):

	def __init__(self, filename):
		# You must create the writer object with a filename
		# parameter.

		# Setting up the basic elements of the tree to
		# build a graph
		self.gexf = et.Element('gexf')
		self.graph = et.SubElement(self.gexf, 'graph')
		self.nodes = et.SubElement(self.graph, 'nodes')
		self.edges = et.SubElement(self.graph, 'edges')
		self.nodeDict = {}
		self.edgeDict = {}

		self.filename = filename

	def addEdge(self, eyeD, source, target, weight=None):
		# Every parameter is allowed to be a number.
		# The below code will make the necessary transformations
		self.edgeDict[eyeD] = [source, target]
		if weight:
			self.edgeDict[eyeD].append(weight)

	def addNode(self, eyeD, label):
		# You can make the id a number and the below code
		# will convert it to the necessary string

		self.nodeDict[eyeD] = label

	def processNodes(self):
		#goes through every entry for nodes and adds them
		#to nodes as the parent
		for eyeD, label in self.nodeDict.items():
			self.node = et.SubElement(self.nodes, 'node')
			self.node.set('id', str(eyeD))
			self.node.set('label', label)

	def processEdges(self):
		# Makes edges the parent and adds every edge
		# to that parent. Weight is optional, as before
		for eyeD, attrs in self.edgeDict.items():
			self.edge = et.SubElement(self.edges, 'edge')
			self.edge.set('id', str(eyeD))
			self.edge.set('source', str(attrs[0]))
			self.edge.set('target', str(attrs[1]))
			if len(attrs)==3:
				self.edge.set('weight', str(attrs[2]))


	def save(self):
		# Saves the file
		self.processNodes()
		self.processEdges()

		self.nodes.set('count', str(len(self.nodeDict)))
		self.edges.set('count', str(len(self.edgeDict)))

		self.tree = et.ElementTree(self.gexf)

		self.tree.write(self.filename + '.gexf', encoding='UTF-8', 
			xml_declaration=True)