
import collections, heapq, sys

"""

basic MST, with visited set, adjList

"""
def solve():
    numOfNodes, numOfEdges = map(int, input().split())

    if (0, 0) == (numOfNodes, numOfEdges):
        sys.exit()
        return False
    
    # not acutally necessary
    # if numOfEdges == 0:
    #     print("Impossible")
    #     return False

    adjList = collections.defaultdict(list)

    visited = set()

    for _ in range(numOfEdges):

        u, v, weight = map(int, input().split())

        adjList[u].append( (v, weight) )

        adjList[v].append( (u, weight) )


    # now run a MST (Prim's)

    heap = [(0, 0, 0)] # wieght, node, neighbouringNode
    mstWeight = 0
    edgeResult = []
    edgesCount = -1 # not set to 0, to account for the first Node being counted as a "edge"


    while heap and edgesCount != numOfNodes - 1:
        weight, currentNode, originalSourceNeighbour = heapq.heappop(heap)


        if currentNode in visited: continue

        # process this node
        mstWeight += weight
        visited.add(currentNode)

#         edgeResult.append( ( originalSourceNeighbour, currentNode if currentNode > originalSourceNeighbour else originalSourceNeighbour, currentNode) )
# this is a 3 tuple, lol, look at it's
        """
        edgeResult.append( ( 
            originalSourceNeighbour,   # Element 1: The source
            currentNode if currentNode > originalSourceNeighbour else originalSourceNeighbour, # Element 2: The result of this if/else logic
            currentNode                # Element 3: The current node again
        ) )

        """

        edgeResult.append( ( originalSourceNeighbour, currentNode) if currentNode > originalSourceNeighbour else (currentNode, originalSourceNeighbour) )
        edgesCount += 1  # this is a bug, because remember the first node shouldnt contribute to the edgeCount


        for neighbour, neighbourWeight in adjList[currentNode]:
            if neighbour not in visited:
                heapq.heappush(heap, ( neighbourWeight, neighbour, currentNode ) ) # weight, my neighbour, sourceNode, 

    if edgesCount != numOfNodes -1:
        print("Impossible")
        
    else:
        print(mstWeight)
        for e in sorted(edgeResult[1:]):   # might need to sort this, remember we start at 1 t oaccount for dummy edge 0,0 we start with
            print(e[0], e[1])


while True:
    solve()




"""

BUGS: 

Starting node, so dummy first edge needs to have edge count = -1
or find a way to skip incrementing edgesCoutn for the first node

for the heappush, be clear on pushing neighbour, source
and when popping, know that the new currentNode is now hte neighbour, and the other curreentNode is now the originalSourceNeighbour


Need to do prims, but when I look at my neighbours to enqueue in the adjList, I also add to the heap
(weight, neighbourNode, originalNode)

so that when I pop to process a node
I also add it's MST Weight
but additionally the path I took to get there
which is stored in edgeResult

as [neighbourNode, originalNode] depending on whichever node is larger

remember to skip edgeResult[0] as I initiallized it with a "dummy 0" to itself, just to kickstart Prims



"""