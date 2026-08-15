"""
What Type Of Sliding Window Is This?

This is a variable-length sliding window (also called a shrinking window).

Variable-length: The window size changes as we go
Why shrinking?: When we violate the condition (more than 2 occurrences of a character), we shrink from the left until we're valid again

There's also a fixed-length version (where window size is always k), but this isn't that.
"""

# 3090. Maximum Length Substring With Two Occurrences

s = "bcbbbcba"

def maximumlengthSubstring(s):
    left = 0 # Left pointer of window
    max_length = 0 # Track the longest valid window we've seen
    char_counts = {} # # Dictionary stores count of each char in current window
    # The sliding is caused by the for loop and
    # the while loop working together as a team.
    for right in range(len(s)):
        incoming_char = s[right]
        # create the key if new or throw the old and overwrite it
        char_counts[incoming_char] = char_counts.get(incoming_char, 0) + 1

        # Shrink from the back
        while char_counts[incoming_char] > 2:
            # kicking out of the back of the box (remove from left)
            outgoing_char = s[left]
            char_counts[outgoing_char] -= 1
            left += 1
        # Calculate the current window's length,
        # then compare it with the biggest window I've seen so far.

        # Current window length = right - left + 1
        # +1 because BOTH left and right indexes are included.
        # right - left gives the distance between them, not the number of elements.
        max_length = max(max_length, right - left + 1)

    return max_length


r = maximumlengthSubstring(s)
print(r)


"""
Iteration | right | char | Window    | char_counts        |max_length | Status
----------|-------|------|-----------|--------------------|-----------|-----------
Start     | -     | -    | ""        | {}                 | 0         | -
1         | 0     | 'b'  | "b"       | {'b': 1}           | 1         | ✓
2         | 1     | 'c'  | "bc"      | {'b': 1, 'c': 1}   | 2         | ✓
3         | 2     | 'b'  | "bcb"     | {'b': 2, 'c': 1}   | 3         | ✓
4         | 3     | 'b'  | "cbb"*    | {'b': 2, 'c': 1}   | 3         | 🔄 Shrink
5         | 4     | 'b'  | "bb"*     | {'b': 2, 'c': 0}   | 3         | 🔄 Shrink
6         | 5     | 'c'  | "bbc"     | {'b': 2, 'c': 1}   | 3         | ✓
7         | 6     | 'b'  | "bcb"*    | {'b': 2, 'c': 1}   | 3         | 🔄 Shrink
8         | 7     | 'a'  | "bcba"    | {'b': 2, 'c': 1, 'a': 1} | 4   | ✅ MAX!

*Asterisk means the window shrunk due to violation

If I'm tracking the longest variable-length window,
right-left+1 tells me the current window's length,
and I compare it with the best length I've seen.
"""
