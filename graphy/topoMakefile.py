import collections

n = int(input())
prereqToCourse = collections.defaultdict(list) # Forward: If A changes, B is affected
courseToPrereqs = collections.defaultdict(list) # Backward: B needs A to run

# --- Step 1: Parse Input ---
for _ in range(n):
    line = input().split(":")
    target = line[0].strip()
    # .split() handles multiple spaces and empty strings automatically!
    preReqList = line[1].split() 
    
    for p in preReqList:
        prereqToCourse[p].append(target)
        courseToPrereqs[target].append(p)

changed_file = input().strip()

# --- Step 2: Find Affected Files (Discovery) ---
affected = set()
stack = [changed_file]
while stack:
    curr = stack.pop()
    if curr not in affected:
        affected.add(curr)
        for neighbor in prereqToCourse[curr]:
            stack.append(neighbor)

# --- Step 3: Local Indegree Calculation ---
# Only count dependencies that are ALSO in the affected set
indegreeMap = {course: 0 for course in affected}
for course in affected:
    for p in courseToPrereqs[course]:
        if p in affected:
            indegreeMap[course] += 1

# --- Step 4: Kahn's Algorithm ---
res = []
# Start only with affected nodes that have 0 internal dependencies
# q = collections.deque([c for c in affected if indegreeMap[c] == 0])
# but logically speaking, the only course that's affected with an indegree of 0, is the changed file
q = collections.deque([changed_file])


while q:
    curr = q.popleft()
    res.append(curr)
    
    for neighbor in prereqToCourse[curr]:
        if neighbor in affected:
            indegreeMap[neighbor] -= 1
            if indegreeMap[neighbor] == 0:
                q.append(neighbor)

# Print results line by line as requested by the problem
for file in res:
    print(file)

# unfortunate I couldn't get this, the modified toposort really broke my brain since we need a two pass
# and so courseToPrereq is necesary for step 3- and step 2 doesnt need it