def findSubsetsThatSumToK(arr, n, k) :
    result = []
    
    #arr.sort()
    def backtrack(start, current_subset, current_sum):
        # If the current sum is equal to K, add the subset to the result
        if current_sum == k:
            result.append(list(current_subset))
            # We continue after finding a subset to explore other possibilities
        
        # Explore all further elements starting from 'start' index
        for i in range(start, n):
            # Include the element
            current_subset.append(arr[i])
            # Recurse with the next elements
            backtrack(i + 1, current_subset, current_sum + arr[i])
            # Backtrack: Exclude the element
            current_subset.pop()
    
    backtrack(0, [], 0)
    #result.sort(key = lambda x: (len(x), x))
    return result