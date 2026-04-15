import sys, collections, heapq

n = int( sys.stdin.readline() )


"""
5
1
1
2
2
7

that node is the neighbour, of the chopped off LEAF
which means, we can have an leaf-degree map, holding how many leaves each node has

if a node has 0 leaves, it means its a leaf, and we can chop it off

when you chop off a a leaf, you decrement that node's neighbour's leaf-ddegree by 1

HOW do you know the neighbour?

5
1
1
2
2
7

Leaf-degrees:
1: 2
2: 2
3: 0
4: 0
5: 1
6: 0
7: 1

popping order  (-> neighbour, neighbours leaf-degree):
3  -> 5  (5:0)
4  -> 1   (1:1)
5   -> 1   (1: 0)
1   -> 2   (2: 1)
6   -> 2  (2: 0)
2    -> 7   (7:0)

# see, we got 7 as our last popped, and [3,4,5,1,6,2] length == 7



"""
leafDegreeMap = { i:0 for i in range(1, n+ 2) }

leafNeighbours = []
for _ in range(n):
    neighbourOfTheLeaf = int(sys.stdin.readline())
    leafNeighbours.append( neighbourOfTheLeaf )

    leafDegreeMap[neighbourOfTheLeaf] += 1

heap = []

for node, leafDegree in leafDegreeMap.items():
    if leafDegree == 0:
        heap.append( node )

# heap has: 3,4,6

res = []
idx = 0  # it's for our leafNeighbours
while heap:
    node = heapq.heappop( heap )

    # could do the finalizing check here
    if node == n + 1:
        if len(res) != n:
            print("error")
        else:
            for node in res:
                print(node)
        break # necessary, so when I pop next, the idx is incremented to be 6, for the leaf-neighbour node 7
    # in [511227], for leafNeighbours
    # if we run our next idx, indexing after without the break, its outside the valid limit
    neighbourOfNode = leafNeighbours[idx]

    # print(neighbourOfNode)

    leafDegreeMap[neighbourOfNode] -= 1
    if leafDegreeMap[neighbourOfNode] == 0:
        heapq.heappush(heap, neighbourOfNode)

    res.append( node )
    idx += 1


"""
bugs encountered:
issues with keyError, since range is not inclusive of endPoint

dictionary.values is the values, items is both

forgot import heapq

"""
