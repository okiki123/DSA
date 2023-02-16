#Brute force approach is to calculate the sum of every 5 elements contiguous subarray of the given array and divide the su, by '5' to find the average
def find_average_of_subarays(k, arr):
    result = []
    for i in range(len(arr) - k + 1):
    #find sum of next 'K' elements
        _sum = 0.0
        for j in range(i, i+k):
            _sum += arr[j]
        result.append(_sum/k) #Calculate average
    return result

#Optimal Solution
def find_averages_of_subarrays(k, arr):
    result = []
    windowSum, windowStart = 0.0, 0
    for windowEnd in range(len(arr)):
        windowSum += arr[windowEnd] #add the next element
        #slide the window, we dont need to slide if we have not hit the required window aize of 'k'
        if windowEnd >= k - 1:
            result.append(windowSum / k) # calculate the average
            windowSum -= arr[windowStart] # subtract the element going out
            windowStart += 1 # slide the window ahead
    return result



