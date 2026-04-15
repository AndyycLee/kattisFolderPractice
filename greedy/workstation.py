import sys, heapq

n, m = map(int, sys.stdin.readline().split())


inter = []
heap = []
# 1 for arrive, -1 for depart
for _ in range(n):
    researcherArriveTime, duration = map(int, sys.stdin.readline().split())

    researchers.append( (researcherArriveTime, duration, 1) )
    researchers.append( (researcherArriveTime + duration, duration, -1) )
    # heapq.heappush( (researcherArriveTime + researcherEndTime, researcherArriveTime + researcherEndTime + m) )
    # I was gonna do a approach where I also add the endTimes, like a tuple (start, 1) (end, -1), and when we encounters an endTime we push
    # to the heap, but that isnt necesary, it would be valid though
    # since we consider endTimes before startTimes, meaning we can push to our heap, and thime to pop from our heap to use the free computer
inter.sort()
count = 0
# now we explore our startTimes
for researcherStart, duration, typ in inter:
    if typ == -1:
        # we push the free computer time to the heap
        heapq.heappush(heap, (researcherStart, researcherStart + m) )
    else:
        if heap:
            # evict from the heap computer times that have already locked
            while  heap and heap[0][1] < researcherStart:
                heapq.heappop()
            
            if heap and (researchStart <= heap[0][1]):
                heapq.heappop() # use the free computer
                # push the new occupied computer time
                
                heapq.heappush(heap, (researcherStart + researchEnd, researcherStart + researchEnd + m ) )
        else:
            # means we don't have any free computer, so we unlock one
            count += 1

print(count - n) # we only care about the saved unlocks, not the total unlocks
def solve_penelope(researchers, m):
    # Sort by arrival time
    researchers.sort()
    
    # Heap stores "Free Times" of machines currently unlocked
    # (The time the researcher left)
    unlocked_machines = []
    saved_unlocks = 0
    
    for start, duration in researchers:
        # 1. Clean up: Remove machines that have already locked
        while unlocked_machines and unlocked_machines[0] + m < start:
            heapq.heappop(unlocked_machines)
            
        # 2. Check if any machine is free (and not locked)
        # unlocked_machines[0] is the EARLIEST a machine became free
        if unlocked_machines and unlocked_machines[0] <= start:
            # We found a match! 
            saved_unlocks += 1
            heapq.heappop(unlocked_machines) # Use this machine
            
        # 3. Add the machine's NEW free time after this researcher leaves
        heapq.heappush(unlocked_machines, start + duration)
        
    return saved_unlocks