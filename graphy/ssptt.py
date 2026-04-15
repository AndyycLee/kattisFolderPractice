import math

"""
walking thru this test case

4 4 4 0
0 1 15 10 5
1 2 15 10 5
0 2 5 5 30
3 0 0 1 1
0
1
2
3
2 1 1 0
0 1 100 0 5
1
0 0 0 0



to reach Node1, theres a cost of 5 to traverse
but it can only be traversed at t=15

so I reach it in t=20

to get to Node2, theres a cost of 5, so after getting to Node1
the path from node1 to node2 is opened at every 15 + (10*p) intervals
 if I wait until t=25, I can traverse it
it to reach Node2 which is then reached at t=30

I need to create a dijkstra map
with the shortest time to reach every singel node

like in FullTank
The goal was to minimize the cost
And at each step, you could traverse an edge wiht no cost, or add cost but stay at hte same edge, and adding hte cost was based on the current
Edge you're at

In this problem, you


In standard dijkstra's
You pop edges with the minEdgeWeight
and traverse in that order, so that you relax edges to rfind he shortest path

In this variation, you traverse edges in the shortest time span

I have a feeling of solving thsi using dijkstras, where we keep a globalTimer counter. and upon exploration of the heappop, we pop the lowestNetTimeTaken node, look at it's edges and relaxthem if the new edges could be traversed in that globalTimeCount



the issue is with a globalTimeCounter, its wasted inefficeincy increemnting T by 1, for the P*T value, so I was thinking there mightbe some math to effectively calculate the minimumTiming to reach the edges neighbours given the current timing im at?



I got this feeling that its



heap = (currentTime, currentNode)

pop from heap

check it's neighbours, the edges to add is



when currentTime <= (P *T) + d



thats the new (nextCurrentTime, nextNode)



we can add

but effectively calculating that nextCurentTime means

(currentTime - d )/ P

which I didn't find any merit in the number?



in example one fro reaching node2, that yields

1/2 =< T



so I dont even know what that means
THIS IS WHERE I ASKED AI

itd be at time=25. the k value is 6/10

but im a bit confused on what the k value represents, is it the full time that must tick? meaning we also keep this tickCycle value to keep track of in our heap, so that future edges know the tickCycle and we find the maxTime based on the next interval whoses tickCycle is valid?

The Math to find the Departure Time

Instead of looping, we can find the departure time (t) mathematically.

If we arrive at currentTime:

If currentTime ≤ t₀:
We just wait until t₀. Departure is at t₀.

If currentTime > t₀:
If P = 0, we missed the only chance! The edge is "Impossible."

If P > 0, we need the smallest k such that:
t₀ + k · P ≥ currentTime

Using ceiling logic, the next pulse t after t₀ is:

t = t₀ + ceil((currentTime - t₀) / P) · P


those pulses that we round up, then represents the next time we can depart in order to find the next timing to reach the next node

that makes sense then, is there a resaon we decide to choose a ceil or how does that make work out? i understand the equation is like

current time =< (k*P + initial time)

since that means that we have reached a interval that we can achieve, but the k must be ceiled so thats not a prtial value for the thingy of big that lets our time exceed the current time?

meaning the new currentTime is = currentTime + pulseCeiler*P
in the case that initialTime < currentTime


"""
"""
its a dijkstras on crack

our heap = (currentTime, currentNode)

when we pop, minimizing for currentTime

we'll end up looking at the nodes neighbours, mapping like

adjList[node1] = [ (node2, openingTime, P, dTIme) , (node3, openingTime, P, dTIme) ]

and relaxing it's edge's, and adding them to the queue if the calcultedTime to reach that node, is less than what we've ever seen so far

so we'll have a minMapping = [float("inf") for _ in range(numOfNodes)]

and then you can have a heap = [ (0, startingNodeIndex )]

pop from the heap, check the node's neighbours,
and there will be two conditions then 

"""
import collections, heapq, sys
# Single source shortest path, time table

def modifiedDijkstrasOnCrack():
    numOfNodes , numOfEdges, numOfQueries, startingNodeIndex = map(int, ( sys.stdin.readline().split() ))

    if (0, 0, 0, 0) == (numOfNodes, numOfEdges, numOfQueries, startingNodeIndex): sys.exit()

    # edges are pretty unique, they take
    # timeInit + t*P to traverse
    # and cost d timeUnits to traverse


    # and remember, you need to find the current time it takes where
    # currentTime =< initTime + (P* somePulseTiming)

    minMapping = [float("inf") for _ in range(numOfNodes)]
    minMapping[startingNodeIndex] = 0
    adjList = collections.defaultdict(list)
    heap = [ (0, startingNodeIndex ) ]

    for _ in range(numOfEdges):
        source, destination, initTime, P, dTimeCost = map(int, sys.stdin.readline().split() )

        adjList[source].append( (destination, initTime, P, dTimeCost) )

    while heap:
        currentTime, currentNode = heapq.heappop(heap)

        for neighbour, initTime, P, dTimeCost in adjList[currentNode]:

            # now we calculate the time it takes to get to that node at a minimum

            # two cases:
            # one is where our initTime is greater than our current tiem, so we just wait until that initTime

            if initTime >= currentTime:

                if minMapping[neighbour] > (initTime + dTimeCost):

                    heapq.heappush( heap, (initTime + dTimeCost, neighbour))

                    minMapping[neighbour] = (initTime + dTimeCost)

            else:
                # mean's either we have to find the next avalaible pulse timing
                # to fidnthe opening window where currentTime =< initTime + (P* somePulseTiming)

                # or that the P, is 0, meaning no pulse timing will be open for us to ever access this path

                if P == 0:
                    continue

                else:
                    pulseTiming = math.ceil( (currentTime - initTime) / P)
                
                    nextGreaterTiming = (P * pulseTiming) + initTime

                    if minMapping[neighbour] > (nextGreaterTiming + dTimeCost):
                        heapq.heappush( heap, (nextGreaterTiming + dTimeCost, neighbour) )

                        minMapping[neighbour] =  (nextGreaterTiming + dTimeCost)


    for _ in range(numOfQueries):
        targetNode = int(input())
        if minMapping[targetNode] != float("inf"):
            print(minMapping[targetNode])
        
        else:
            print("Impossible")

while True:
    modifiedDijkstrasOnCrack()