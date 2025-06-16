#Problem: Find the maximum sum of a subarray of size k.
#Input: arr = [2, 1, 5, 1, 3, 2], k = 3
#Output: 9 (from subarray [5, 1, 3])

'''This is a fixed size sliding window problem. '''
arr = [2, 1, 5, 1, 3, 2]
k = 3
def max_sum_subarray(arr, k):
    max_sum = window_sum = sum(arr[:k])
    for i in range(k,len(arr)):
        window_sum += arr[i] - arr[i-k]
        max_sum = max(max_sum, window_sum)
    print(max_sum)
    #return max_sum

max_sum_subarray(arr, k)