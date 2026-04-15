"""
First thought is:

we're looking for a MST, given coordinate points

and so we could first create N^2 edges

by taking for each coordinate point, finding it's euclidean distance to another point

making that the edgeWeight

so adjList[ (x1, x2)] = [ (euclidDistance, (x2, y2) ),  (euclidDistance, (x3, y3) ) ]

and then what we do is run a MST like prims, or kruskals on this

"""

import sys, math, collections, heapq

numOfCases = int(sys.stdin.readline())


def euclideanDistance(coordinatePair1, coordinatePair2):
    x1, y1 = coordinatePair1
    x2, y2 = coordinatePair2

    return math.sqrt( (x1 - x2)**2 + (y1 - y2)**2  )

for _ in range(numOfCases):
    adjList = collections.defaultdict(list)

    points = []

    numOfCoordinates = int(input())

    for _ in range(numOfCoordinates):
        x, y = map(float, sys.stdin.readline().split() )

        points.append( (x, y) )

    # now we create an adjList, mapping each coordinate and it's euclid distance to every other point

    for i in range(len(points)):
        for j in range(i + 1, len(points)):

            coordinatePair1 = points[i]
            coordinatePair2 = points[j]
            
            euclidDistance = euclideanDistance(coordinatePair1, coordinatePair2)

            adjList[coordinatePair1].append( (euclidDistance, coordinatePair2) )
            adjList[coordinatePair2].append( (euclidDistance, coordinatePair1) )


    # now just run a MST on this

    visited = set()
    # visited.add(points[0])
    minHeap = [ (0, points[0]) ] # cost, startCoordinatePair

    mstWeight = 0

    while minHeap:

        w, coordinatePair = heapq.heappop(minHeap)

        if coordinatePair in visited: continue

        visited.add(coordinatePair)
        mstWeight += w

        for weight, coordinateNeighbour in adjList[coordinatePair]:

            if coordinateNeighbour not in visited:
                heapq.heappush( minHeap, (weight, coordinateNeighbour) )
    
    print(mstWeight)


"""
some potential BUGS:
    visited.add(points[0])
works perfectly

but fear set( point[i] )
or just putting in any raw tuple as initializing, since set operator normally unpacks values, rather than considers them as a tuple

make sure not to initalize with     # visited.add(points[0])

remember input parsing correctly for cases where using floats, dont just map(int, etc..)


got first test case, unfort

"""
