# 3702. Longest Subsequence With Non-Zero Bitwise XOR

# 3702. Longest Subsequence With Non-Zero Bitwise XOR

def longestSubsequence(nums):

    # XOR of the entire array
    total = 0

    # True if at least one non-zero number exists
    has_non_zero = False

    for n in nums:

        # Needed for the case where total XOR is 0
        # but we can still remove one element
        if n > 0:
            has_non_zero = True

        # Build the XOR of all numbers
        total ^= n

    # Whole array already has non-zero XOR
    if total != 0:
        return len(nums)

    # Whole XOR is 0, but a non-zero number exists
    # → remove one element
    elif has_non_zero:
        return len(nums) - 1

    # All numbers are 0 → every subsequence has XOR 0
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
