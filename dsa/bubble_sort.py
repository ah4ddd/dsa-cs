nums = [5, 3, 8, 4] # > 3 4 5 8

n = len(nums)

for i in range(n):

    for j in range(n - 1 - i):

        if nums[j] > nums[j + 1]:

            nums[j], nums[j + 1] = nums[j + 1], nums[j] # swap

print(nums)
