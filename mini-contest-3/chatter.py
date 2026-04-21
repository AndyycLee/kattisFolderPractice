"""

for n ranges, we are gonna run union find on the set of problems

I had 
"""
import collections, sys

def solve():
    try:
        n, r, a, b, c = map(int, input().split())

        def helper(prevRValue):
            newRValue = ( (prevRValue * a) + b  ) % c
            return newRValue 


        rank = [0 for _ in range(n)]
        parent = [i for i in range(n)]

        parentGroupSize = [1 for _ in range(n)]

        def find(node):
            if parent[node] == node:
                return node
            
            parent[node] = find(parent[node])
            return parent[node]

        def union(node1, node2):
            node1Parent, node2Parent = find(node1), find(node2)

            if node1Parent == node2Parent: return # False

            if rank[node1Parent] > rank[node2Parent]:
                parent[node2Parent] = node1Parent
                parentGroupSize[node1Parent] += parentGroupSize[node2Parent]
            
            elif rank[node2Parent] > rank[node1Parent]:
                parent[node1Parent] = node2Parent
                parentGroupSize[node2Parent] += parentGroupSize[node1Parent]

            else:
                parent[node2Parent] = node1Parent
                rank[node1Parent] += 1
                parentGroupSize[node1Parent] += parentGroupSize[node2Parent]

            # return True I explain why I dojnt need this in down below comments

        numOfSuccessfulConnectionAttempts = 0

        currentRValue = [r]

        while numOfSuccessfulConnectionAttempts < n:

            xbeforeMod = helper(currentRValue[0])

            currentRValue[0] = xbeforeMod

            ybeforeMod = helper(currentRValue[0])

            currentRValue[0] = ybeforeMod

            x, y = xbeforeMod % n, ybeforeMod % n

            if x == y:
                continue

            union(x, y)
            numOfSuccessfulConnectionAttempts += 1

            """
            after I calculate the new R value, I need to set it globally

            I also do return False/True in union, because if a group was already chatting together, I think that means that's not a unique group

            for example
            1 <-> 2

            and if I union 2 <-> 3

            there is now 1 unique chat Group of size 3
            if I tried to union
            1 < -> 3

            that wouldn't change the size of the chat group nor the unique count of chats

            ABOVE ^ I realized I had a bug in my understanding, and that's bceause union will automatically handle merging groups with the same parent to do double counting of parentGroupSize

            but it still counts as a successfulConnectionAttempt as it joins new people

            """

        """
        now need to handle the printing

        for each group of chat connections

        I run a find, seeing the parent, I can add that parent to a dict, which maps taht groupsSize : howManyGroups have that size

        for unvisited parent's - I can find the group size, and run the above mapping

        otherwise skip

        """
        out = []
        res = collections.defaultdict(int)
        uniqueGroups = set()

        for i in range(n):

            iParent = find(i)

            if iParent not in uniqueGroups:

                uniqueGroups.add(iParent)

                iParentGroupSize = parentGroupSize[iParent]
                res[ iParentGroupSize ] += 1

        numOfUniqueGroups = len(uniqueGroups)

        for groupSize, howManyGroupsHaveThatSize in res.items():
            out.append( (groupSize, howManyGroupsHaveThatSize) )

        out.sort(reverse=True)

        test = []
        # the reason I'm using a testDictionary and joining in the end, is because if I used a raw string and repeeatedly concatened, that's n^2 in python

        for groupSize, howManyGroupsHaveThatSize in out:

            if howManyGroupsHaveThatSize == 1:
                test.append( str(groupSize) )
            
            else:
                test.append( str(f"{groupSize}x{howManyGroupsHaveThatSize}") )

        test = " ".join(test)

        print(f"{numOfUniqueGroups} {test}")
    
    except:
        sys.exit()



# if f strings don't work, im just gonna ask AI to convert it

while True:
    solve()


"""

I had a bug in my randomizationHelper

I don't reset r % n

I do that outside to calcualte x and y

final notes:

I probably deserve a bit less grade in both technical and other aspects

I have really slow coding speed

I'm pretty proud of the fact I was able to solve this in less than a hour, with no AI debugging, and I could manually debug it on my own
! probably a testament to my learning unionFind I can solve it decently fast, implement the patterns (i kinda glanced at my old union find code tho)
and also got better at manual debugging and inspecting for errors, which is a skill I really need to work on

some bugs I noticced were:

typos, using resetinng the prevRValue to xbeforeMod, rather than ybeforeMod

helper was using r, not prevRValue

goodjob on weird f string avoiding concatenation formatting

"""