# C31 — Stone Game IV

def winner_square_game(n):
    dp = [False]*(n+1)

    for stone in range(1, n+1):

        square = 1

        while square <= stone:

            remaining = stone - square * square

            if dp[remaining] == False:
                dp[stone] = True
                break

            square+=1

    return dp[n]

n = 8
result = winner_square_game(n)
print(result)
