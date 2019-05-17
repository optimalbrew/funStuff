"""
Dijkstra's shortest path

Two ways to think about it.

1: original
Start from init node and breadth first traversal (like a wavefront) keeping track of steps taken from source and updating distances 
to nodes seen multiple times (via different paths) as we go along. Must traverse the entire graph. 

2: faster version with (need to implement) a priority queue.
* create a set of unvisited nodes called unhandled.
* These ndoes are stored in a binary tree (or a heap) where the value represents current best distance from source.
* Node with the lowest distance (from source) is on top of the tree/ queue.
* Initially, the source node has a distance 0, while all other nodes are infty
* While set(unhandled nodes) != empty
    * pick the node on top
    * find distances to all its UNvisited/unhandled children (or nighbors)
    * update these distance (from infty or previously known value)
    * After all chidren/neighbors updated, move the parent node to the visited set.     
    * Reorg the queue/tree to put lowest total distance on top again

"""


