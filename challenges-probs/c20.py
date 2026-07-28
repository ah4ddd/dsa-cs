# Challenge 20 — Rotate List

numbers = [1, 2, 3, 4, 5]
k = 2

def rotate_right(nums, k):
    n = len(nums)
    if n == 0:
        return nums

    k = k % n
    rotated = [0] * n

    for i in range(k):
            rotated[i] = nums[n - k + i]

    for j in range(n-k):
        rotated[j+k] = nums[j]

    return rotated

result = rotate_right(numbers, k)

print(result)



# solution 2 (slicing)
def rotate_with_slice(nums, k):
  if not nums:
      return None
  k = k % len(nums)

  return nums[-k:] + nums[:-k]

result2 = rotate_right(numbers, k)

print(result)
