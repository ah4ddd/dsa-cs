# 3702. Longest Subsequence With Non-Zero Bitwise XOR

# 3702. Longest Subsequence With Non-Zero Bitwise XOR

def longestSubsequence(nums):

    # We will calculate the XOR of ALL numbers in the array.
    #
    # Example:
    # nums = [1, 2, 3]
    #
    # total starts at 0:
    #
    # 0 XOR 1 = 1
    # 1 XOR 2 = 3
    # 3 XOR 3 = 0
    #
    # So total eventually becomes the XOR of the entire array.
    total = 0

    # This keeps track of whether the array contains
    # at least ONE non-zero number.
    #
    # Why do we care?
    #
    # If every number is 0, then every possible subsequence
    # has XOR = 0.
    #
    # Therefore, there is no valid subsequence at all.
    has_non_zero = False

    # Go through every number once.
    for n in nums:

        # Since the problem gives us non-negative numbers,
        # n > 0 means that n is non-zero.
        #
        # Once we find one non-zero number, this stays True.
        if n > 0:
            has_non_zero = True

        # XOR the current number into total.
        #
        # ^= is shorthand for:
        #
        # total = total ^ n
        #
        # So we continuously build:
        #
        # total = nums[0] XOR nums[1] XOR nums[2] ...
        total ^= n

    # CASE 1:
    #
    # The XOR of the ENTIRE array is already non-zero.
    #
    # Then we can simply take the entire array as our
    # subsequence.
    #
    # Its XOR is non-zero, so the longest possible
    # subsequence has length len(nums).
    if total != 0:
        return len(nums)

    # CASE 2:
    #
    # The XOR of the entire array is 0.
    #
    # But we know there is at least one non-zero number.
    #
    # If we remove ONE carefully chosen element, the XOR
    # of the remaining elements becomes non-zero.
    #
    # Therefore we can take n - 1 elements.
    elif has_non_zero:
        return len(nums) - 1

    # CASE 3:
    #
    # The entire XOR is 0 AND there isn't even a
    # non-zero number.
    #
    # Since all numbers are 0, the array looks like:
    #
    # [0, 0, 0, ...]
    #
    # XOR of any subsequence is still 0.
    #
    # Therefore, no valid subsequence exists.
    else:
        return 0

"""
             XOR the entire array
                     │
          ┌──────────┴──────────┐
          │                     │
      XOR ≠ 0                XOR = 0
          │                     │
          ↓                Is there a
     Take everything       non-zero number?
          │                 /       \
          ↓               YES        NO
        n                  │          │
                           ↓          ↓
                         n - 1        0
"""



nums = [1,2,3]

r = longestSubsequence(nums)

print(r)




# Brainfuck solution
def longestsubsequence(nums):
    total = 0
    non_zero = 0

    for n in nums:
        non_zero = non_zero | (n > 0)
        total ^= n

    return non_zero * (len(nums) - (not total))

nums = [1,2,3]

r = longestsubsequence(nums)

print(r)
