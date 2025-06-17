'''Given an array of integers nums and an integer k. A continuous subarray is called nice if there are k odd numbers on it.

Return the number of nice sub-arrays.

 

Example 1:

Input: nums = [1,1,2,1,1], k = 3
Output: 2
Explanation: The only sub-arrays with 3 odd numbers are [1,1,2,1] and [1,2,1,1].

Example 2:

Input: nums = [2,4,6], k = 1
Output: 0
Explanation: There are no odd numbers in the array.

Example 3:

Input: nums = [2,2,2,1,2,2,1,2,2,2], k = 2
Output: 16
'''
def nice_array(nums, k):
    count = 0
    left = 0
    odd_count = 0
    for right in range(len(nums)):
        if nums[right] %2 == 1 :
            odd_count +=1 
            while odd_count > k : 
                if nums[left] % 2 == 1 :
                    odd_count -= 1
                left += 1
        if odd_count == k:
            temp_left = left
            while temp_left < right and nums[temp_left] % 2 == 0 :
                tem_left += 1
            count += temp_left - left + 1
    return count
result = nice_array([1,1,2,1,1], 3)  # Output: 2
print(result)  # Output: 2