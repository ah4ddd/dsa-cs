# Challenge 14 — Find the Second Largest Number

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
START

largest = 12
second  = 12

        │
        ▼

65 arrives

🥇 65
🥈 12

        │
        ▼

70 arrives

🥇 70
🥈 65

        │
        ▼

7 arrives

Too small

🥇 70
🥈 65

        │
        ▼

40 arrives

Too small

🥇 70
🥈 65

        │
        ▼

75 arrives

🥇 75
🥈 70

        │
        ▼

42 arrives

Too small

🥇 75
🥈 70

        │
        ▼

8 arrives

Too small

🥇 75
🥈 70

        │
        ▼

90 arrives

🥇 90
🥈 75

        │
        ▼

98 arrives

🥇 98
🥈 90
"""
