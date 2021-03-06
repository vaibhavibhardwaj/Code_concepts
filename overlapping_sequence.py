import heapq

def gotMostVisited(n , sprints)-> int:
    
    time_counts = [0]*(n+2)
    i = 0
    while(i<n-1):
        # 1-5 or 5-1  needed platform counts will be same 
        # Hence, min and max is taken 
        start = min(sprints[i],sprints[i+1])
        end = max(sprints[i],sprints[i+1])
        time_counts[start] = time_counts[start]+1
        time_counts[end+1] = time_counts[end+1]-1
        i = i + 1
                
    trainCountIth = [0] # trains at 0th time
    
    for i in range(1,n+2):
        trainCountIth.append(trainCountIth[i-1] + time_counts[i])
        
    # presents top 3 values  and it's index
    time_p = heapq.nlargest(3, range(len(trainCountIth)), trainCountIth.__getitem__)
    
    return time_p
