nums = [2, 1, 5, 1, 3, 2]
k = 3

def maxSum(nums, k):
    window_sum = sum(nums[:k])
    maximum = window_sum

    for i in range(k, len(nums)):
        window_sum += nums[i]       # add new element
        window_sum -= nums[i - k]   # remove old element

        maximum = max(maximum, window_sum)

    return maximum

r = maxSum(nums, k)
print(r)

# 2 leaves ❌
# 1 enters ➕
