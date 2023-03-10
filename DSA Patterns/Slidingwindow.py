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
        #slide the window, we dont need to slide if we have not hit the required window size of 'k'
        if windowEnd >= k - 1:
            result.append(windowSum / k) # calculate the average
            windowSum -= arr[windowStart] # subtract the element going out
            windowStart += 1 # slide the window ahead
    return result


def max_sub_array_of_size_k(k, arr):
    windowsum, windowstart,  maxsum = 0, 0, 0
    for windowend in range(len(arr)):
        windowsum += arr[windowend] #add the next element
    
        if windowend >= k - 1:
            maxsum = max(maxsum, windowsum)
            windowsum -= arr[windowstart]
            windowstart += 1
        return maxsum
    
import math
def smallest_subarray_with_given_sum(s, arr):
    window_sum = 0
    min_length  = math.inf
    window_start = 0
    for window_end in range(len(arr)):
        window_sum += arr[window_end]
        while window_sum >= s:
            min_length = min(min_length, window_end - window_start + 1)
            window_sum - arr[window_start]
            window_start += 1
        if min_length == math.inf:
            return 0
        return min_length

def longest_substring_with_k_distinct(str, k):
    window_start = 0
    max_length  = 0
    char_frequency = {}

    for window_end in range(len(str)):
        right_char = str[window_end]
        if right_char not in char_frequency:
            char_frequency[right_char] = 0
        char_frequency[right_char] += 1

        while len(char_frequency) > k:
            left_char = str[window_start]
            char_frequency[left_char] -= 1
            if char_frequency[left_char] == 0:
                del char_frequency[left_char]
            window_start += 1
        max_length  = max(max_length, window_end  - window_start + 1)
    return max_length

def pair_with_targetsum(arr, target_sum):
    start_point = 0
    end_point =  len(arr) - 1
    while start_point < end_point:
        arr[start_point] + arr[end_point] == sum
        if sum < target_sum:
            start_point +=1
        if sum > target_sum:
            end_point -= 1
        if sum  == target_sum:
            return  [start_point, end_point]
    return [-1, -1]

def remove_duplicates(arr):
    next_non_duplicate = 1
    i = 1
    while(i < len(arr)):
        if arr[next_non_duplicate - 1] != arr[i]:
            arr[next_non_duplicate] = arr[i]
            next_non_duplicate += 1
        i += 1
    return next_non_duplicate

def remove_element(arr, key):
    nextElement = 0
    for i in range(len(arr)):
        if arr[i] != key:
            arr[nextElement] == arr[i]
            nextElement += 1
    return nextElement





