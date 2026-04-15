"""

I'm reading the problem on my other screen right now



you have a recipeBook

with 1 - N recipes

you want one recipe with the valid potion ur seeking

the recipes share ingredients, but you only have one of each ingredient

for each recipe, if you can't concot : skip
else: concoct this potion



so pretty obviously, since we can make a mixture

like

[bats, cats, rats] = One Recipe

and if [bats, cats, rats, ginger] = another recipe

you can make both

so the output is two

however, if you then see 
[bats, cats]
or
[bats, cats, rats, toads]

you can't form those


some intial thoguhts, are it's hard for meto thnk of this as a union find problem

seems more like a simulation problem, where each ingredient I add to a set, and then for each future ingredient I add it to the set, however, if
i encounter a recipe, and its not a subset or superset then its not able to be included

unionFind excels when I want to see if a group of nodes belongs to each other

so im guessing in this case if i think of each ingredient in a recipe as a node, I would union all ingredients in a recipe together

in a new recipe being encountered, I would then find(ingredient), see if it belongs to my current main cauldron

OK I"VE GOT IT I THINK

each recipe is a cauldron, meaning I union everything in the recipe together

but before that, I run a find on all ingredients, seeing if they all belong to eachother

if they all belong to eachother, that actuaally means that a previous cauldron was brewed with those same ingredients
the only issue is, union might be a superset, meaning the cauldron might contain additional ingredients I don't want

rather than just being a cauldorn of ingredients or less than ingredients, or ingredients exactly!!!!!!!!!!!

so that means for each unionedGroup I want to keep a count of how many ingredients it has

if I find on all of my ingredients in a given recipe - FIRST: THEY MUST ALL MATCH, meaning they all share the same parent AND
see that the count exactly matches, that means I have an identical potion!

if I find on all my ingredients, but it has les ingredients than the countOfThatUnion group, thatmeans that group has additional ingredients so I have to skip this potion

if I find on all my ingredients, but if has more ingredients than the countOfThatUnion group

[bats, cats, rats] = One Recipe

[bats, cats, rats, ginger] = my second recipe, # notice ginger is a different group, but our matchingCount is 3, and the list of ingredients is 3 (aka: Count of that parentGroup), so ITS OKAY!

another recipe with:  [bats, cats, toads, biscuits , ginger]  # notice toads, biscuits, toads are a different group, this would be okay, but the matchingCount is 3, but the listOfIngredients in the cauldron is 4
so we must SKIP!

I like my appraoch, so lets code up a unionFind

I need to modify the union portion to union the count of ingredients in a map as well
"""


numOfRecipes = int(input())


# we're given the number of recipes beforehand, but the thing we're actually unioning, is the ingredients

"""
what really hung me up, was creating the parent map

since in unionFind normally, each node is initally it's own parent, and we union wiht other nodes

in ladice, each drwaer is a like a node, and is it's own parent initially, and each item (can really not be considered as a node, 
but rather jsut an edge to a prentGroup, as it only communicates by decrementing the capacityMap[parentDrawerGroup])
 connects to a parentGroup (meaning a item connects to it's drawer) 


in this one, the number of recipes is fixed, but that's not super useful, what Im actually interested in is the parent of each recipe
as each ingredient is a node, seems kinda wasteful, but it appears as thoguh I'm creating a parent for each ingredient off the bat, but I could do it on the fly i guess?
on the fly, probably means using a dictioanry for lookups to see if it doesn't exist yet, and just creating it if not


i guess it does tell us that: The sum of M over all recipes will be no greater than 500 000, so even if wasteful, it'll pass? but i still want to try being efficient just for practice

the problem: i have issues since I need to
have a count of the ingredients with a parentGroup(recipe)
so intially I can map each ingredient to 1, representing the number of ingredients it takes, is just 1 represented fro this group of size 1

i could pre-initialize this at the start, but im not giving the number, or even if the ingredients are integers are within some consecutive sequence, only they're sum is within 500 000

so creating them in the find, in a dictionary seems smarter
"""

import collections

currentlySeenIngredientsAndTheirIngredientCount = {}
count = 0
parent = {}

rank = collections.defaultdict(int)

def find(node):

    if node not in parent:
        rank[node] = 0
        currentlySeenIngredientsAndTheirIngredientCount[node] = 1
        
        parent[node] = node
    
    if parent[node] == node: return node

    # path compression
    parent[node] = find(parent[node])
    return parent[node]

# the thing Im struggling w/ is the fact that ingredients can be length of 1, meaning I need to handle that fact that a RECIPE only has ONE INGREDIENT, so SPECIFICALLY CHECK for length of 1 recipes, since running a union is 
# unnecessary, a FIND is sufficient to get the parent
def union(ingredientA, ingredientB):

    ingredientAParent, ingredientBParent = find(ingredientA), find(ingredientB)

    if ingredientAParent == ingredientBParent: return 


    if rank[ingredientAParent] > rank[ingredientBParent]:
        parent[ingredientBParent] = ingredientAParent
        currentlySeenIngredientsAndTheirIngredientCount[ingredientAParent] += currentlySeenIngredientsAndTheirIngredientCount[ingredientBParent]
    
    elif rank[ingredientBParent] > rank[ingredientAParent]:
        parent[ingredientAParent] = ingredientBParent
        currentlySeenIngredientsAndTheirIngredientCount[ingredientBParent] += currentlySeenIngredientsAndTheirIngredientCount[ingredientAParent]
    
    else:
        # tied union
        parent[ingredientBParent] = ingredientAParent
        currentlySeenIngredientsAndTheirIngredientCount[ingredientAParent] += currentlySeenIngredientsAndTheirIngredientCount[ingredientBParent]
        rank[ingredientAParent] += 1
    
for _ in range(numOfRecipes):
    # turns out, all of the below input parsing can be condensed into: ingredientList = list(map(int, input().split()))[1:]  ^^
    ingredientList = map(int, input().split())

    ingredientList = list(ingredientList)
    ingredientList = ingredientList[1:]


    if len(ingredientList) == 1:
        # no union needed
        ingredientParent = find(ingredientList[0])
        
        # recipes are not guaranteed to be distinct, so we might have seen this before, which handles the case of single ingredients, or single cauldrons
        if currentlySeenIngredientsAndTheirIngredientCount[ingredientParent] == 1:
            count += 1
        
        # and it's checking if that existing ingredient, has shown up in a cauldron before, and is only a cauldron of that one ingredient to brew a potion
        # since if that ingredient is part of a bigger union, the currentlySeenIngredientsAndTheirIngredientCount will be > 1
        
    else:
        # we need to run a find on all the ingredients first, see if they all share the same parent

        # if yes, mean's they're already unioned, now we just need to check if the parent's ingredients count matches exactly, or is less than my ingredients lsit <- Correction: I'll never have the scenario where a parent's ingredients count is less than one in my ingredients list,
        # since the size of a existing cauldron (parentGroup) can be at most the size of a found parentGroup (cauldron), thus any recipe introducing shared ingredients can only share ingredients of a cauldron at max of the size of that existing cauldron

        # theres definitely an aproach which runs a find on all the ingredients, comapres withthe recipe's ingredientCount, and handles it like that
        # the case I'm debating is

        # [1,2,3]
        # [1,2,3,4]
        # because this means that we have a temp dictionary, mapping parentGroup : 3, newGroup: 1
        # and you could compare this to the count of each of it's parentGroup's currentlySeenIngredientsAndTheirIngredientCount
        temp = collections.defaultdict(int)
        for ingredient in ingredientList:

            ingredientParent = find(ingredient)
            temp[ingredientParent] += 1
            
        valid = True
        for ingredientParent, ingredientCountInARecipe in temp.items():

            """
            so a case like [1,2,3] in a cauldron, 

            and our recipe is [1, 2]
            meaning our recipe is missing components of the cauldron
            """

            if currentlySeenIngredientsAndTheirIngredientCount[ingredientParent] > ingredientCountInARecipe:

                # this means recipe's dont match up cause the current recipe has 
                valid = False; break
            elif currentlySeenIngredientsAndTheirIngredientCount[ingredientParent] == ingredientCountInARecipe:

                """
                so a case like [1,2,3] in a cauldron, 

                and our recipe is [1, 2,3,4]
                meaning our recipe runs find(1), find(2), find(3), and thus finds parentGroup1: 3 == parentGroupOFCauldron

                and does this for every single ingredient, finding out that we are valid, we'll never run into the case where a recipe has >= ingredientCountInAReipe
                because after seeing if a group of new ingredients has the matching of a existin cauldron, the matching can only be at most size of the cauldron's group
                if we encounter new valid recipes, the size of our cauldron matches with that, meaning we will never achieve a new recipe that has more matching ingredients than whata cauldron would already have since we 
                union the new recipes together if they are valid, being the new max size
                """
        if valid:
            # I need to union the ingredients, with the parent of the group
            ingredientParent = find(ingredientList[0])

            for ingredient in ingredientList[1:]:
                union(ingredientParent, ingredient)
            
            # could also do the union like this:
            # if valid:
            #     for i in range(len(ingredientList) - 1):
            #          union(ingredientList[i], ingredientList[i + 1])
            count += 1

print(count)














"""

not sure waht's wrong, why I output 0

Im not even entering the loop
for ingredientParent, ingredientCountInARecipe in temp.items():

so a case like [1,2,3] in a cauldron, 

and our recipe is [1, 2]
meaning our recipe is missing components of the cauldron

if currentlySeenIngredientsAndTheirIngredientCount[ingredientParent] > ingredientCountInARecipe:
    print("FOUDN WRONG NON MATCHING COUNT!")

    # this means recipe's dont match up cause the current recipe has 
    valid = False; break
elif currentlySeenIngredientsAndTheirIngredientCount[ingredientParent] == ingredientCountInARecipe:

    print("FOUDN MATCHING COUNT!")


ok im glad I didnt need to walk through everything manually, just using print statements showed me I was never entering the
ELSE, where a ingredeintList has at least 2 ingredienst

portion of 

    if len(ingredientList) == 1:
        # no union needed
        ingredientParent = find(ingredientList[0])
        
        # recipes are not guaranteed to be distinct, so we might have seen this before, which handles the case of single ingredients, or single cauldrons
        if currentlySeenIngredientsAndTheirIngredientCount[ingredientParent] == 1:
            count += 1
        
    else:

AMAZING I SOLVED THIS WITHOUT AI, AND I DID IT WITHOUT AI HINTS EITHER, Union find patterns are so hard to identify, but
im proud I was able to do it, in a real contest because i take so long to walk through the code, i fear i wont be able to
either identify it within time constraints or pressure
or even if i do Ill take too long to solve, or get caught on details with implmeentation

AI FEEDBACK: 
My motivation for sepeating singel ingredients vs not single was to handle ujnioning, but ya my method wouldve handled that path for a single ingredient just find as well

ironically, I didn't even need The "Single Ingredient" Case:
You have a special if len(ingredientList) == 1 block. While that works, the beauty of the DSU logic is that it actually generalizes
 If a recipe has one ingredient [5], your temp dictionary would just be {find(5): 1}. If ingredient 5 hasn't been used, its size is 1. Since 1 == 1, it passes! You could actually delete that special case and the else logic would handle it perfectly.

"""