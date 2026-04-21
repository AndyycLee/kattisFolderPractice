"""

basically, we have two intervals we can try to fillup of length N

we always push to the interval with less size

!! we are guaranteed a solution exceeds so I don't need to worry about any interval overflowing

sort the musicians by duration

and kep choosing the less full interval

the approahc essentially works by divide muscians into two intervals, since atmost two msucians can go on break at one time
"""

lengthOfConcert, numOfMusicians = map(int, input().split())

musiciansBreakTime =  map(int, input().split())

musiciansBreakTimeAndIndex = []

for i, breakTime in enumerate(musiciansBreakTime):
    
    musiciansBreakTimeAndIndex.append( (breakTime, i) )
musiciansBreakTimeAndIndex.sort(reverse=True)

res = []
interval1, interval2 = 0, 0 # lengthOfConcert, lengthOfConcert
# if we were given possible failure cases, then itd be smart to add the check upon insertion if we exceed lengthOfConcert in either interval

i = 0
while i < numOfMusicians:


    if interval1 < interval2:
        res.append( ( interval1 ,musiciansBreakTimeAndIndex[i][1]) ) # instead of appending the (durationTime, index), we actually want the interval's startingTime since thats the next time we can insert a musicna 


        interval1 += musiciansBreakTimeAndIndex[i][0] # the muscians duration of their break, but in the actual result we need the index, because the result output should output each muscian sorted by index order
        # rather than our insertion (since we sort to use largest durations first)

    else:
        res.append( (  interval2 ,musiciansBreakTimeAndIndex[i][1] ) )
        interval2 += musiciansBreakTimeAndIndex[i][0]

    i += 1
def customKey(tupl):
    return tupl[1]

res.sort(key=customKey)

out = []
for t in res:
    out.append(  str(t[0]) )
    out.append(" ")

print("".join(out))



"""
my operatiosn are really ugly, since we have to strip away indexes at the end, in order to then join as a string, which I fel lik can definitely be cleaned up

"""