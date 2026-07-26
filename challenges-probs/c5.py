def get_largest(nums):
    if not nums:
        return None

    largest = nums[0]
  # largest = float("-inf") < works too

    for n in nums[1:]:
        if n > largest:
            largest = n

    print(f"Largest: {largest}")

numbers = [-12, -7, -3, -25]

get_largest(numbers)


"""
Pattern #1 — Counting
count = 0

for item in items:
    if condition:
        count += 1


Pattern #2 — Categorizing
evens = []
odds = []

for item in items:
    ...


Pattern #3 — Best-so-far ⭐
best = items[0]

for item in items[1:]:
    if item is better:
        best = item
"""
