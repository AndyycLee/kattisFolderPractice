import sys

numOfNodes, numOfQueries = map(int, sys.stdin.readline().split())
# in union find, you need a array for ranks
# and a array for parents

rank = [0 for _ in range(numOfNodes)]
parent = [i for i in range(numOfNodes)]
def find(node):
    # base case if the parent is itself
    if parent[node] == node:
        return node
    
    # else
    # path compression, setting this node's parent, to the find of itself
    parent[node] = find(parent[node])

    return parent[node]

def union(node1, node2):

    node1Parent = find(node1)
    node2Parent = find(node2)

    if rank[node1Parent] > rank[node2Parent]:
        # set node2's parent to node1's parent


        parent[node2Parent] = node1Parent
        rank[node1Parent] += 1

        """
        my question is:
        if node2's parent was not itself, but a different node

        and we try to set node2's parent to node1's parent

        what happens about al other node's who previously had ndoe2 as a parent?
        should they be connecteed to node1's parent now? since they'er unioned?

        and it feels like im not handling that


        BUT!!!!! in reality

        instead of setting the parent of a node directly, ur setting the parent of a node, to be parent of the parent of the other node

        then in the find step, that node's parent, will have changed to have node's parent parent
        and it'll be compressed to be just node's parent

        """
    else:

        parent[node1Parent] = node2Parent
        rank[node2Parent] += 1
    # so if I try to union anything with node2, once it's parent has changed
    # what I'll get is node2's parent, and set the target node's parent to node2's parent

for _ in range(numOfQueries):
    typeOfQuery, node1, node2 = sys.stdin.readline().split()
    node1, node2 = int(node1), int(node2)

    if typeOfQuery == "=":
        union(node1, node2)
    else:
        node1Parent, node2Parent = find(node1), find(node2)
        if node1Parent == node2Parent:
            print('yes')
        else:
            print("no")


"""
BUGS?

NONE!

good news is no bugs, just minor stuff, such as, if I try ot union two nodes'
who already are unioned, meaning they have the same aprent, I could handel that with

if node1Parent == node2Parent:
    return  # already in same set, do nothing
but it's unnecessary, I guess a consequnce is rank increment


i guess a consequence is rank increment? since AI says
The bug: you increment rank unconditionally, but rank should only increase when both trees have equal rank (i.e., in the else branch only when ranks are equal). When one tree is strictly taller, attaching the shorter one doesn't increase the taller tree's rank.


nowto understand rank corruption
So rank is really an optimization on top of an optimization. Path compression does the heavy lifting, rank just makes the worst case theoretical bound tighter.

VERSION w/out rank optimization
parent = [i for i in range(numOfNodes)]

def find(node):
    if parent[node] == node:
        return node
    parent[node] = find(parent[node])
    return parent[node]

def union(node1, node2):
    node1Parent = find(node1)
    node2Parent = find(node2)
    parent[node1Parent] = node2Parent  # just always attach node1's root to node2's root


Version w/ dictionary

parent = {i: i for i in range(numOfNodes)}

def find(node):
    if parent[node] == node:
        return node
    parent[node] = find(parent[node])
    return parent[node]

def union(node1, node2):
    parent[find(node1)] = find(node2)
"""



"""
[0, 1, 2, 3, 4, 5]


[5, 1, 2, 3, 4, 5]

running find(0)

returns 5


now lets say we have
[5, 1, 2, 3, 4, 5]

but turn index 5's parent to 2

[5, 1, 2, 3, 4, 2]

trying to run find(0), gives us 0's parent is equal to 5's parent, which is 2
eventually
setting parent[0] to 2

return parent[node]
to return 0's parent is 2

so intuitively meaning in the worst case, union find's find operation will take O(n)

"""
