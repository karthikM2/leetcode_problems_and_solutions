'''You are given an array of integers nums, there is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position.

Return the max sliding window.

 

Example 1:

Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
Output: [3,3,5,5,6,7]
Explanation: 
Window position                Max
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7

Example 2:

Input: nums = [1], k = 1
Output: [1]

 '''
# solution 1 which is taking o(n*k) time complexity
'''    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        right, start, max_ele = k,0,[]
        for left in range(len(nums)):
            sub_array = nums[left:right]
            max_ele.append(max(sub_array))
            left += 1
            right += 1
            if left == len(nums)-2:
                break
        return max_ele'''

# solution 2 which is taking o(n) time complexity
from collections import deque
def maxSlidingWindow(nums, k):
    if not nums or k == 0:
        return []
    if k == 1:
        return nums
    result = []
    deq = deque()  # Store indices of elements in the current window
    for i in range(len(nums)):
        if deq and deq[0] < i-k+1:
            deq.popleft()
        while deq and nums[deq[-1]] < nums[i]:
            deq.pop()
        deq.append(i)
        if i >= k - 1:
            result.append(nums[deq[0]])
    return result

# Example usage
result = maxSlidingWindow([1, 3, -1, -3, 5, 3, 6, 7], 3)
print(result)  # Output: [3, 3, 5, 5, 6, 7]