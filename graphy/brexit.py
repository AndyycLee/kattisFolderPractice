import collections, sys
"""

idea is this?

every country maps to it's neighbours as a set

so for 

4 3 4 1
2 3
2 4
1 2

2: [1, 3, 4]
1: [2]
3: [2]
4: [2]

q = [ 1 ]

look at 1's neighbours: that's 2

exitMap[2] -= 1
and that's the end of our q, since it's now empty, and didn't pop our homeCountry/enqueue it to be popped, so print"stay"


tricky to understand, since countries with no trading neighbours, they will never leave
meaning that our exitMap for every country with no trading partners should be INF, since no matter how many countries try to leave, this country will never enter
our queue to be popped from

initally we maintain this exitMap as len(neighbourCountries) // 2. whenver we pop from our queue, see that
it's actually a bidrectional relationship between country-country for trading partners

so that now that we popped, we see it's list of enighbours, and can decrement those countries indegrees by 1, comapre with out exitMap to see if you
should neque that to leavingCountry queue
if it hasnt been visited before, then enqueue it and mark as visited

"""

numOfCountries, edges, homeCountry, firstLeavingCountry = map(int, input().split())

if homeCountry == firstLeavingCountry:
    print("leave")
    sys.exit()

exitMap = { i: float("inf") for i in range(1, numOfCountries + 1)  }

indegreeMap = collections.defaultdict(int)

adjList = {i:set() for i in range(1, numOfCountries + 1) }

for _ in range(edges):
    node1, node2 = map(int, input().split())
    adjList[node1].add(node2)
    adjList[node2].add(node1)

    indegreeMap[node1] += 1
    indegreeMap[node2] += 1


# now going to construct the exitMap, to set the number of neighbours must leave, for this country to be enqueued in our popping queue
for i in range(1, numOfCountries + 1):
    numOfNeighbours = len(adjList[i])
    if numOfNeighbours > 0:
        exitMap[i] = numOfNeighbours // 2
    
q = collections.deque([firstLeavingCountry])

# visited = set(firstLeavingCountry)

# I don't think a visited set is necessary, as we're removing from the set of neighbours, so we don't risk removing the same country twice, thereby decrementing a countries indegree twice
# and since we never remove the same country twice, we'll never decremetn a countries in-degree by duplitituos accidentaly


# print(adjList)

while q:
    leavingCountry = q.popleft()
    # print(leavingCountry)

    # if leavingCountry in visited: continue
    # if leavingCountry == homeCountry:
    #     print("leave")

    # look at it's neighbours, to determine who we have to remove, and potentially decrement the exitMap if this node hasn't been visited

    for neighbour in adjList[leavingCountry]:
        # it's unnecesary to remove neighbour, from adjList[leavingCountry], since we won't be looking at this leavingCountry again, so we won't be trying to remove it ever again, and it'll never be re-enqueued because , because the edges it was conected to are removeed, so it can never see itself indegree decrement and enqueeud

        # these neighbours, are having their exitMap decremented

        # if leavingCountry not in visited:
        if leavingCountry in adjList[neighbour]:

            adjList[neighbour].remove( leavingCountry )
            indegreeMap[neighbour] -= 1
            
            # I could technically do a visit set here, marking the neighbour as added to our queue
            # therefore no longer add him to the queue
            # but because the indegree check is ==, and not <=, we only enqueue him once, although our indegreeMap will decrement those values
            # a bit extra, kinda unnecessarily
            if indegreeMap[neighbour] == exitMap[neighbour]:
                # visited.add(neighbour)
                q.append( neighbour )
                # print(neighbour)
                if neighbour == homeCountry:
                    print("leave")
                    sys.exit()

# print(exitMap)
# print(indegreeMap)
# print(adjList)

print("stay")


"""
reflections on bugs

missed edge case where homeCountry == firstLeaving

I think good catch? on the unnecessary aspect of a visited set

forgot to set the indegrees, for nodes in my indegree map

"""

"""
analyzing failure:

10 14 1 10
1 2
1 3
1 4
2 5
3 5
4 5
5 6
5 7
5 8
5 9
6 10
7 10
8 10
9 10


1: [2,3,4]
2: [1 , 5]
3: [1, 5]
4: [ 1, 5]
5: [2,3,4, 6,7,8,9]
6: [5, 10]
7: [5, 10]
8: [5, 10]
9: [5, 10]
10: [6,7,8,9]

1 is home, 10 is leaving

look at 10's neighbours

6,7,8,9

6: [5]
7: [5]
8: [5]
9: [5]

indegrees all become 1, so it's equal to it's exit map
so they all get enqueued

5, has exitMap of 8
4 nodes being removed means, it gets enqueued eventually
5: [2,3,4,5]


"""