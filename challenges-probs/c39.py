# 1386. Cinema Seat Allocation

class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: list[list[int]]) -> int:

        # Store reserved seats for each row
        reserved = {}

        for row, seat in reservedSeats:
            if row not in reserved:
                reserved[row] = set()

            reserved[row].add(seat)

        # Every completely empty row can fit 2 groups
        answer = (n - len(reserved)) * 2

        # Check only rows that have reservations
        for row in reserved:
            seats = reserved[row]

            left_free = all(seat not in seats for seat in [2, 3, 4, 5])
            middle_free = all(seat not in seats for seat in [4, 5, 6, 7])
            right_free = all(seat not in seats for seat in [6, 7, 8, 9])

            if left_free and right_free:
                answer += 2

            elif left_free or middle_free or right_free:
                answer += 1

        return answer

obj = Solution()

r = obj.maxNumberOfFamilies(
    n=2, reservedSeats = [[2,1],[1,8],[2,6]]
    )

print(r)
