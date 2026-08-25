# Challenge 20 — Rotate List

numbers = [1, 2, 3, 4, 5, 6, 7]
print(f"input: {numbers}")
k = 3
print(f"k: {k}")


# solution 2 (slicing)
def rotate_with_slice(nums, k):
  if not nums:
      return None
  k = k % len(nums)
  print(k)
# The element at the END index is NOT included.
  return nums[-k:] + nums[:-k]

result2 = rotate_with_slice(numbers, k)

print(f"output: {result2}")
