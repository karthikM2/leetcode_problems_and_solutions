'''Given an array of positive integers nums and a positive integer target, return the minimal length of a

whose sum is greater than or equal to target. If there is no such subarray, return 0 instead.

 

Example 1:

Input: target = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: The subarray [4,3] has the minimal length under the problem constraint.

Example 2:

Input: target = 4, nums = [1,4,4]
Output: 1

Example 3:

Input: target = 11, nums = [1,1,1,1,1,1,1,1]
Output: 0
'''

def minSubArrayLen(target,nums):
        if target in nums : 
            return 1
               
        else:
            if sum(nums) < target:
                return 0
            if sum(nums) == target:
                return len(nums)
            # Sliding window approach
            left,start,min_len,k = 0,0,float('inf'),2
            for right in range(len(nums)):
                 start += nums[right]
                 while start >= target:
                      min_len = min(min_len,right-left+1)
                      start -= nums[left]
                      left += 1
        return min_len if min_len > 0 else 0                 
                

result = minSubArrayLen( 7, [2,3,1,2,4,3])
print(result)