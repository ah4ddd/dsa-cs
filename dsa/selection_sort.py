nums = [5, 3, 8, 4]

n = len(nums)

for i in range(n):

    smallest = i
    # start at index i+1 and stop before n
    for j in range(i + 1, n):

        if nums[j] < nums[smallest]:

            smallest = j

    nums[i], nums[smallest] = nums[smallest], nums[i]

print(nums)
