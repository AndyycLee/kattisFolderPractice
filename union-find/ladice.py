"""
some initial thoughts

knowing it's a union find is a big service

essentially, what im going to do is

you can imagine each drawer L, as a parent Node

and each item N, as a the structure, I need to union to the drawer

each Drawer can only have one item, meaning the "Rank" of the drawer should be incremented when unioning it
and decrementing, when unioned away??

im not sure, ive never dis-unioned before

### looking at the rules:
Mirko stores the items in order from 
 to 
 using the first rule he can apply:

If the drawer 
 is empty, he stores the item 
 in that drawer.

If the drawer 
 is empty, he stores the item 
 in that drawer.

Try to move the item from 
 to its other drawer; if that ones filled too, try moving that item to its other drawer, and so on until you either succeed or get back to a previously seen drawer. In case of success, store the item 
 in the drawer 
. In case of failure, continue to next rule.

Try moving the item from 
 to its other drawer; if that ones filled too, try moving that item to its other drawer, and so on until you either succeed or get back to a previously seen drawer. In case of success, store the item 
 in the drawer 
. In case of failure, continue to next rule.

Give up and throw away the item 


So each item N, corresponds to one of 2 drawers
but a drawer can only have 1 item

we can pretty easily map each item: [drawerA, drawerB]


"""




"""
working through a basic test case

1: 1 2
2: 1 3
3: 1 2
4: 1 3
5: 1 2

items -> drawers


initially,



ASKED AI

pretty fascinating union-find problem

i never considered that unioning drwawers would be a thing, and so 3 diferent drawers each unioned together, means a capacity of 3 for any item we can insert


basicaly:

the idea is this:
run a union on each of the drawers that woudl be connected toa item!

working through a basic test case

1: 1 2
2: 1 3
3: 1 2
4: 1 3
5: 1 2

items -> drawers

this means, [1,2,3] are all a drawerSet, which I can define a drawerParent based on some rank

so let's say drawer1, is the parent

iterate from items 1,2,3,4,5

1 -> find(1) - i could also run a find on find(2), but theese are unionedDrwaers anyways so they'll return the same parent so it doesnt matter

see's drawerParent1, has a capacity of 3, so insert

2 -> find(1)

see's drawerParent1, has capcity of 2 so insert

3 -> find(1)
see's drawerParent1 has capacity of 1 so insert


remaining find's see drawerParent1 has no capacityk, so unable to isnert, print(SMECE)
4 -> find(1)

5 -> find(1)


in the unioning of drawers, so 
"""
# I need to strat from 1 index, since drwaesr and items begin from 1, to N inclusive. So standard aray indexing of 0 -> n-1 won't work

numOfItems, numOfDrawers = map(int, input().split()   )

drawerParentCapacity = {i:1 for i in range(1, numOfDrawers + 1)} # every drawer parent initially starts with one capacity - represnesting itself

rank = [-1] + [1 for _ in range(numOfDrawers) ]
parent = [-1] + [ i for i in range(1, numOfDrawers + 1)]

# i also need to consider, when unioning two drawers, I must also union their capacities

def find(node):

    if parent[node] == node:
        return node
    
    # path compression   -- could also do     parent[node] = find(parent[node])

    MainParentNode = find(parent[node] )
    parent[node] = MainParentNode
    return parent[node]

def union(drawerA, drawerB):

    # this is going to be the tryicky part
    # essentially I ned to union two drawers based on the rank, and set one of the drawers as the parentDrawer, with him having the greatest rank
    # I also need to union the total caapcity of both drawers, and set that value as the new capacity of the parentDrawer

    drawerAParent = find(drawerA)
    drawerBParent = find(drawerB)

    # in this case, because of the capacity unioning - not because of rank adding, I think i need to add a early return if they 
    # share the same parent to avoid duplicate capacity adding
    if drawerAParent == drawerBParent: return 
    # yup this was necessary ^^

    if rank[drawerAParent] > rank[drawerBParent]:

        # union drawerB's parent to drawerA
        parent[drawerBParent] = drawerAParent

        drawerParentCapacity[drawerAParent] += drawerParentCapacity[drawerBParent]

    elif rank[drawerBParent] > rank[drawerAParent]:
        parent[drawerAParent] = drawerBParent
        drawerParentCapacity[ drawerBParent] += drawerParentCapacity[drawerAParent]

    else: # equal ranks
                # union drawerB's parent to drawerA
        parent[drawerBParent] = drawerAParent
        rank[drawerAParent] += 1
        drawerParentCapacity[drawerAParent] += drawerParentCapacity[drawerBParent]

itemToItsDrawer = []

for i in range(numOfItems):

    drawerA, drawerB = map(int, input().split())
    
    # the i'th item 
    itemToItsDrawer.append( (i, (drawerA, drawerB)))

for item, drawerPair in itemToItsDrawer:
    drawerA, drawerB = drawerPair
    union(drawerA, drawerB)


    drawerGroupParent = find(drawerA)

    if drawerParentCapacity[drawerGroupParent] > 0:
        drawerParentCapacity[drawerGroupParent] -= 1
        print("LADICA")
    else:
        print("SMECE")

"""
one of my oncerns wiht this appraoch
is that im technically not doing it as the simulation intends

for example

1: 1 2
2: 1 2
3: 1 2
4: 1 3

should be:
LADICA
LADICA
SMECE
LADICA

but my algorithim merges [1,2,3]

so wouldnt I end up with:
LADICA
LADICA
LADICA
SMECE

indeed, the reason I fail testCase3 is because of this example above, so I'll rectificy this
by unioning as I see items, and then seeing to find and insert into it's ParentGroup
"""