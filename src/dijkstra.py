"""
Dijkstra's shortest path using a priority queue (instead of original 'wavefront')

Pseudocode from wikipedia: https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm

1  function Dijkstra(Graph, source):
2      dist[source] ← 0                           // Initialization
3
4      create vertex set Q
5
6      for each vertex v in Graph:           
7          if v ≠ source
8              dist[v] ← INFINITY                 // Unknown distance from source to v
9          prev[v] ← UNDEFINED                    // Predecessor of v
10
11         Q.add_with_priority(v, dist[v])
12
13
14     while Q is not empty:                      // The main loop
15         u ← Q.extract_min()                    // Remove and return best vertex
16         for each neighbor v of u:              // only v that are still in Q
17             alt ← dist[u] + length(u, v) 
18             if alt < dist[v]
19                 dist[v] ← alt
20                 prev[v] ← u
21                 Q.decrease_priority(v, alt)
22
23     return dist, prev

"""
#Using heaps
import heapq

########## Class for nodes###################
# input graph as adjacency list (good for graphs that are sparse)
class graphNode:
    def __init__(self,x):
        self.label = str(x) #in case labels are not strings
        self.adj = {} #use dict
    """
    Example: 
    n1 = graphNode('n1')
    n1.adj = dict(n2=5,n3=10)
    print(n1)
    """
    #repr
    def __repr__(self):
        desc=''
        if self.adj:
            desc = 'Node ' + self.label + ' is connected to'
            for k,v in self.adj.items():
                desc += '\n* node ' + str(k) + ' at distance ' + str(v)
            return desc
        else:
            return 'Node '+ self.label + ' has no neighbors.'

######## Sample input #######################
#Input graph: same as in wikipedia example
n1 = graphNode('n1')
n1.adj = {'n2':7, 'n3':9, 'n6':14} #or dict(n2=7,n3=9,n6=14)

n2 = graphNode('n2')
n2.adj = dict(n1=7,n3=10,n4=15)

n3 = graphNode('n3')
n3.adj = dict(n1=9,n2=10,n4=11,n6=2)

n4 = graphNode('n4')
n4.adj = dict(n2=15,n3=11,n5=6)

n5 = graphNode('n5')
n5.adj = dict(n4=6,n6=9)

n6 = graphNode('n6')
n6.adj = dict(n1=14,n3=2,n5=9)

# distances between nodes
def nodeDist(node1,node2):
    return node1.adj[node2.label]

############## Main algorithm #################
# initialization
allNodes = set([n1,n2,n3,n4,n5,n6])
nodeDict = {node.label: node for node in allNodes} #can use label (string) to refer to node object instance 

source = n1 #start node
distance = {'n1':0}
inf = 10e2 #infinifty for this example

# vertexSet 
Q = [] #this will be used for the priority queue
prev={} #map of previous node to retrace path

# Initialize distance to all nodes from source as infty
for node in allNodes:
    if node != source:
        distance[node.label] = inf
    prev[node.label] = None 
    heapq.heappush(Q, (distance[node.label], node.label)) #add to priority queue (heap)

# The main search
while len(Q) != 0:
    top = heapq.heappop(Q) #pop top of queue
    u = nodeDict[top[1]] #extract the second element of the tuple, the node object, from its label (string)
    stillInQ = [n[1] for n in Q]
    for vStr in u.adj.keys():
        if vStr in stillInQ: #examine each neighbor that's still in the queue
            v = nodeDict[vStr] #get node from label
            alt  = distance[u.label] + nodeDist(u,v) # compute distance from source  to v through u
            if alt < distance[v.label]:
                distance[v.label] = alt
                prev[v.label] = u.label
                for i in range(0,len(Q)):
                    if Q[i][1] == v.label:
                        Q[i] = (alt, v.label) #update priority of node
                        heapq.heapify(Q)

print('\nDistance from source\n *',distance)
print('\n\nPrevious node on shortest path from source\n *',prev)

