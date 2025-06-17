from collections import defaultdict

def numberOfSubarrays(nums, k):
    count = defaultdict(int)
    count[0] = 1
    odd = 0
    res = 0

    for num in nums:
        if num % 2 != 0:
            odd += 1
        res += count[odd - k]
        count[odd] += 1

    return res

# ✅ Example test
print(numberOfSubarrays([1, 1, 2, 1, 1], 3))  # Output: 2
