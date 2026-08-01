# Challenge 25 — Longest Consecutive Sequence

nums = [100, 101, 5, 6, 7, 8, 50]


def longest_consecutive(nums):
    num_set = set(nums)

    longest = 0

    for num in num_set:
        # We check n-1 because we want to know if this is the beginning of the sequence
        if num - 1 not in num_set:

            length = 1

            while num + length in num_set:
                length += 1

            if length > longest:
                longest = length
              # longest = max(longest, length) <<< works too

    return longest


result = longest_consecutive(nums)
print(result)


"""
Walk through every number.

↓

Is this the beginning of a sequence?

↓

No?

Ignore it.

↓

Yes?

Walk forward until the sequence ends.

↓

Remember the length if it's the biggest one so far.

↓

Continue.
"""


# depreciated one
"""
def longest_consecutive(nums):
    lc = set(nums)
    count = 0

    for c in lc:
        if c - 1 in lc:
            count += 1
        elif c + 1 in lc:
            count += 1

    if count > 0:
        return count

    elif len(lc) == 1:
        return 1

    return 0


result = longest_consecutive(nums)
print(result)
"""
