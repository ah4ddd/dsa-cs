# Challenge 16 — Is the List a Palindrome?

numbers = [1, 2, 3, 2, 1]

numbers2 = [1, 2, 3, 4, 5]

def is_palindrome(nums):
    for i in range(len(nums)//2):
        if nums[i] != nums[-(i+1)]:
            return False
    return True

result = is_palindrome(numbers)
result2 = is_palindrome(numbers2)

print(result)
print(result2)
