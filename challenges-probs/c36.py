# 2029. Stone Game IX
"""
What is the problem?
    Alice and Bob have a row of stones. Each stone has a number on it.
    They take turns removing one stone at a time, with Alice going first.
    After every move, we look at the sum of all stones removed so far.
    If the player makes that sum divisible by 3, that player loses immediately.

There is one more rule:
    If all stones are removed and it's Alice's turn, Bob wins automatically.
    Both players play optimally.
    What do I have to return?

Return:
    True  → Alice can force a win
    False → Bob can force a win
"""

def stoneGameIX(stones):
    type0 = type1 = type2 = 0

    for s in stones:
        if s % 3 == 0:
            type0 += 1
        elif s % 3 == 1:
            type1 += 1
        else:
            type2 += 1

    if type0 % 2 == 0:
        return type1 > 0 and type2 > 0
    else:
        return abs(type1 - type2) > 2

stones = [1,2,3]

r = stoneGameIX(stones)

print(r)
