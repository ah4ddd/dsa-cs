# Challenge 21 — Product of Array Except Self (Brute Force Version)

nums = [1, 2, 3, 4]

def product_except_self(nums):
    product = []

    for i in range(len(nums)):
        current = 1
        for j in range(len(nums)):
            if i != j:
                current *= nums[j]

        product.append(current)

    return product

result = product_except_self(nums)

print(result)
