# Challenge 26 — Group Anagrams
"""
Expected output:

[
    ["eat", "tea", "ate"],
    ["tan", "nat"],
    ["bat"]
]
"""


words = ["eat", "tea", "tan", "ate", "nat", "bat"]

# O(k log k)  /  O(n × k log k)
def group_anagrams(words):
    groups = {}

    for w in words:
        key = "".join(sorted(w))
        if key not in groups:
            groups[key] = []

        groups[key].append(w)

    return list(groups.values())

r = group_anagrams(words)
print(r)



## DEPRECIATED ##
# Whenever Python sees a brand-new key...
# If you access a missing key... it automatically creates : []
# An empty list
# That saves us from writing a bunch of checks ourselves
"""
from collections import defaultdict

words = ["eat", "tea", "tan", "ate", "nat", "bat"]

def group_anagram(words):
    groups = defaultdict(list)

    for w in words:
        key = "".join(sorted(w))
        groups[key].append(w)

    # groups.values() gives only the values
    return list(groups.values())

result = group_anagrams(words)
print(result)"""
