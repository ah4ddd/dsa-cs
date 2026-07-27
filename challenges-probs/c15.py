# Challenge 15 — Move All Zeros to the End

numbers = [0, 1, 0, 3, 12, 0, 9 ,8, 0]

def move_zeros(nums):
    plain = []
    rearrange = []
    for n in nums:
        if n == 0:
            rearrange.append(n)
        else:
            plain.append(n)

    return plain + rearrange


result = move_zeros(numbers)

print(result)
