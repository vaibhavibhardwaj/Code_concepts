from collections import defaultdict

def functio(A):
    tally = defaultdict(list)
    
    for i,item in enumerate(A):
        tally[item].append(i)
    return ((key,locs) for key,locs in tally.items() if len(locs)>1)

A = [3, 5,2,3,4,6,1,6,5,6]

for dup in sorted(functio(A),reverse =True):
    for i in range(len(dup[1])):
        print(dup[0],i)
