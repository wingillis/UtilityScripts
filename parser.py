# This is a simple script that checks to see if
# the GephiWriter works.
# The output of this is a square with one node in the middle,
# that is connected to all other nodes

from GephiWriter import GephiWriter

graphwriter = GephiWriter('WinIsAwesome')

graphwriter.addNode(0, 'First node')

graphwriter.addNode(1, 'Second Node')

graphwriter.addNode(2, 'Third node')

graphwriter.addNode(3, 'Fourth node')

graphwriter.addNode(4, 'Fifth node')

graphwriter.addEdge(0, 0, 1)
graphwriter.addEdge(1, 0, 3)
graphwriter.addEdge(2, 0, 4)
graphwriter.addEdge(3, 1, 4)
graphwriter.addEdge(4, 1, 2)
graphwriter.addEdge(5, 2, 4)
graphwriter.addEdge(6, 2, 3)
graphwriter.addEdge(7, 3, 4)

graphwriter.save()