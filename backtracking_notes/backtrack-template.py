def backtrack(params):
    # base case
    if base_case_condition:
        results.append(currentSolution.copy())
    
    for choice in choices:
        if choice is invalid:
            continue

        make_choice
        backtrack(updated_params)
        undo_choice




# EXAMPLE WITH PERMS
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.res = []
        self.backtrack([], nums, set())
        return self.res

    def backtrack(self, perm: List[int], nums: List[int], chosen: set):
        if len(perm) == len(nums):
            self.res.append(perm.copy())  
            return
        for i in range(len(nums)):
            if i in chosen:
                continue
        
            perm.append(nums[i])
            chosen.add(i)
            self.backtrack(perm, nums, chosen)
            perm.pop()
            chosen.remove(i)

"""
https://claude.ai/share/5f1c4796-c3c1-4bf4-83f8-0a53bac40790

and for loop is just the loop that i have choices and i automatically handle the skip case in the next iteration once i undo

Mar 22
Exactly! You nailed it.

The for loop never makes an explicit "skip this element" decision — the skip is just implicitly baked into the next iteration of the loop:

python
for i in range(start, len(nums)):
    current.append(nums[i])
    backtrack(i + 1, current)
    current.pop()          # undo
                           # next iteration naturally moves to next element
                           # which IS the skip

"""


"""

for somereason, i get the feeling this is different than standard backtrackign problems, where the choice of a skip is encoded seems kinda unique to subsets as we want the undo choice, to then be the fresh information for the next choice of the index loop. WHICH MAKES SENSE! SINCE we want each choice of our next index loop  after we undoed,

to be a fresh state, aside from the current path it took to reach there 

so even draughts is similar, in the sense that after we jump to capture, and undo, the next choice to jump is a fresh state
"""

def subsets(nums):
    result = []
    
    def backtrack(start, current):
        result.append(current[:])  # add at every node
        
        for i in range(start, len(nums)):
            current.append(nums[i])
            backtrack(i + 1, current)
            current.pop()
    
    backtrack(0, [])
    return result

def subsets(nums):
    result = []
    
    def backtrack(index, current):
        if index == len(nums):   # <-- explicit base case required
            result.append(current[:])
            return
        
        # exclude nums[index]
        backtrack(index + 1, current)
        
        # include nums[index]
        current.append(nums[index])
        backtrack(index + 1, current)
        current.pop()
    
    backtrack(0, [])
    return result