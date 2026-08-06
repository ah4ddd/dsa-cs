# Challenge 21 — Product of Array Except Self (Brute Force Version)

nums = [1, 2, 3, 4]

def product_except_self(nums):
    n = len(nums)

    product = [1]*n

    left = 1
    for i in range(n):
        product[i] = left
        left *= nums[i]

    right = 1
    for i in range(n -1, -1, -1): # range(start, stop, step)
        product[i] *= right
        right *= nums[i]

    return product

result = product_except_self(nums)

print(result)
