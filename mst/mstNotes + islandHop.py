import sys, math, collections, heapq

"""
this is notes for islandHop MST

islandHop is MST, using 
either Prims with either the minMapping optimization

or deciding to not build an adjList and just calculate the distance on the fly (since it's just a sqrt, it might be faster than building an adjList and doing dictionary lookups)


minDistances[startNode] = 0 # so the minMapping only prevents enquuing slower nodes, but for nodes already enqueued, the visited set handles that we dont process duplicates?


but technically, because of the heap property, only a visited set is necessary. as in if we didnt have it , but only kept the minMapping dictionary, we would fail due to processing
 duplicate nodes thereby adding redundant nodes to our MST

so in our minMapping dictionary, it seems in Prims it represents the minimum
cost to reach that node from any of our processed nodes
, but in dijstras its the minimum cost to reach it from a given starting node

"""

def euclideanDistance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

line = sys.stdin.readline()
if line:
    numOfCases = int(line.strip())
    for _ in range(numOfCases):
        # We still build the adjList here
        adjList = collections.defaultdict(list)
        points = []

        line = sys.stdin.readline().strip()
        while not line: line = sys.stdin.readline().strip()
        numOfCoordinates = int(line)

        for _ in range(numOfCoordinates):
            x, y = map(float, sys.stdin.readline().split())
            points.append((x, y))

        # Pre-calculating N^2 edges (The potential TLE bottleneck)
        for i in range(len(points)):
            for j in range(i + 1, len(points)):
                p1, p2 = points[i], points[j]
                d = euclideanDistance(p1, p2)
                adjList[p1].append((d, p2))
                adjList[p2].append((d, p1))

        # MST with Dictionary Optimization
        visited = set()
        minDistances = {point: float('inf') for point in points}
        
        startNode = points[0]
        minDistances[startNode] = 0 # so the minMapping only prevents enquuing slower nodes, but for nodes already enqueued, the visited set handles that we dont process duplicates?
        minHeap = [(0.0, startNode)]
        mstWeight = 0.0

        while minHeap:
            w, curr = heapq.heappop(minHeap)
            if curr in visited: continue

            visited.add(curr)
            mstWeight += w

            for d, neighbor in adjList[curr]:
                if neighbor not in visited and d < minDistances[neighbor]:
                    minDistances[neighbor] = d
                    heapq.heappush(minHeap, (d, neighbor))
        
        print(f"{mstWeight:.2f}")



import sys, math, heapq

def euclideanDistance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

line = sys.stdin.readline()
if line:
    numOfCases = int(line.strip())
    for _ in range(numOfCases):
        points = []
        line = sys.stdin.readline().strip()
        while not line: line = sys.stdin.readline().strip()
        numOfCoordinates = int(line)

        for _ in range(numOfCoordinates):
            x, y = map(float, sys.stdin.readline().split())
            points.append((x, y))

        # MST with On-the-fly distance calculation
        visited = set()
        minDistances = {point: float('inf') for point in points}
        
        startNode = points[0]
        minDistances[startNode] = 0
        minHeap = [(0.0, startNode)]
        mstWeight = 0.0

        while minHeap:
            w, curr = heapq.heappop(minHeap)
            if curr in visited: continue

            visited.add(curr)
            mstWeight += w

            # Instead of looking at a pre-built list, we check all points.
            # Python's math.sqrt is faster than Python's dictionary lookups!
            for neighbor in points:
                if neighbor not in visited:
                    d = euclideanDistance(curr, neighbor)
                    if d < minDistances[neighbor]:
                        minDistances[neighbor] = d
                        heapq.heappush(minHeap, (d, neighbor))
        
        print(f"{mstWeight:.2f}")