# Challenge 14 — Find the Second Largest distinct Number

numbers = [12, 65, 70, 7, 40, 40, 75, 42, 8, 90, 98, 98]

def get_second_largest(nums):
    largest = nums[0]
    second_largest = nums[0]

    for n in nums:
        if n > largest:
            second_largest = largest
            largest = n
        elif second_largest < n and n < largest:
            second_largest = n

    if second_largest < largest:
        return second_largest
    return None

result = get_second_largest(numbers)
print(result)


"""
# Become second largest only if you're:
# bigger than the current second largest
# and smaller than the current largest.

Start

🥇12
🥈12

      │
      ▼
65 arrives

🥇65
🥈12

      │
      ▼
70 arrives

🥇70
🥈65

      │
      ▼
7

❌ Too small

      │
      ▼
40

❌ Too small

      │
      ▼
40

❌ Too small

      │
      ▼
75

🥇75
🥈70

      │
      ▼
42

❌ Too small

      │
      ▼
8

❌ Too small

      │
      ▼
90

🥇90
🥈75

      │
      ▼
98

🥇98
🥈90

      │
      ▼
98 (duplicate)

98 > 98 ?     ❌

90 < 98 ?     ✅

98 < 98 ?     ❌

Update cancelled.

      │
      ▼

FINAL

🥇98
🥈90
"""
