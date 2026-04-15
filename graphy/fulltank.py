import heapq, collections

n, m = map(int, input().split())

gasPriceAtCity = list(map(int, input().split() ))

adjList = {i:[] for i in range(n)}

for _ in range(m):
    
    city, destination, distanceToTravelCost = map(int, input().split() )
    
    adjList[city].append( (destination, distanceToTravelCost) )

    adjList[destination].append( (city, distanceToTravelCost) )

numOfQueries = int(input())


for _ in range(numOfQueries):
    cityMinMapping = collections.defaultdict(lambda: float('inf') ) # maps my (city, fuel) to the minimum cost to get there with that fuel level
    # cityMinMapping = {i:float('inf') for i in range(n) }
    fuelCapacity, startingCity, goal = map(int, input().split()) 

    cityMinMapping[ (startingCity, 0) ] = 0 # maps my (city, fuel) to the minimum cost to get there with that fuel level

    heap = [ (0, startingCity, 0)  ] #stores:  ( totalCurrrentCost, currentCity, currentFuel)
    
    while heap:
        currentCost, currentCity, currentFuel = heapq.heappop(heap)

        if currentCity == goal:
            print(currentCost)
            break
        # option 1: buy fuel at current city
        if currentFuel < fuelCapacity:
            newCost = currentCost + gasPriceAtCity[currentCity]
            if newCost < cityMinMapping[ (currentCity, currentFuel + 1) ]:
                cityMinMapping[ (currentCity, currentFuel + 1) ] = newCost
                heapq.heappush(heap, (newCost, currentCity, currentFuel + 1) )
        
        # option 2: travel to neighboring cities
        for neighbor, distanceToTravelCost in adjList[currentCity]:
            if currentFuel >= distanceToTravelCost:
                if cityMinMapping[ (neighbor, currentFuel - distanceToTravelCost) ] > currentCost:
                    cityMinMapping[ (neighbor, currentFuel - distanceToTravelCost) ] = currentCost
                    heapq.heappush(heap, (currentCost, neighbor, currentFuel - distanceToTravelCost) )
    
    else:
        print("impossible")
    
    heap.clear()