letters = ['a', 'b', 'c', 'd', 'e', 'f']
# indices:   0    1    2    3    4    5

letters[1:4]  # Output: ['b', 'c', 'd'] # don't include last

letters[:3]   # From start up to index 3 -> ['a', 'b', 'c']
letters[3:]   # From index 3 to the very end -> ['d', 'e', 'f']

print(letters[1:4])


# Negative Indices in Slicing
letters = ['a', 'b', 'c', 'd', 'e', 'f']
# neg idx:  -6   -5   -4   -3   -2   -1

letters[-1] # is 'f' (the last item)
letters[-3:] # means "start at 3rd from the end, go to the very end" = ['d', 'e', 'f']
letters[:-3] # means "start at the beginning, go up to 3rd from the end" = ['a', 'b', 'c']

# Colon on the left ([:x]) -> "Start at the beginning" and go up until x.
# Colon on the right ([x:]) -> "Start at x" and go all the way to the end.

"""
inclusive
↓

start

exclusive
↓

end
"""
