# Challenge 23 — Valid Anagram

s = "astronomer"
t = "moonstarer"

def is_anagram(s, t):

    if len(s) != len(t):
        return False

    count = {}
    compare = {}

    for i in s:
        if i in count:
            count[i] += 1
        else:
            count[i] = 1
    for j in t:
        if j in compare:
            compare[j] += 1
        else:
            compare[j] = 1

    if count == compare:
        return True
    return False

r = is_anagram(s, t)

print(r)



# another wierd one idk
def anagram(s, t):

    if len(s) != len(t):
        return False

    count = {}

    for i in range(len(s)):

        if s[i] in count:
            count[s[i]] += 1
        else:
            count[s[i]] = 1

        if t[i] in count:
            count[t[i]] -= 1
        else:
            count[t[i]] = -1

    for key in count:
        if count[key] != 0:
            return False

    return True
