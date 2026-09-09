class Solution:
    def isPalindrome(self, x: int) -> bool:

        # Negative numbers can never be palindromes
        if x < 0:
            return False

        # One digit numbers are always palindromes
        if x >= 0 and x <= 9:
            return True

        # Two digit numbers
        if x >= 10 and x <= 99:

            digit1 = x // 10
            digit2 = x % 10

            if digit1 == digit2:
                return True
            else:
                return False

        # Three digit numbers
        if x >= 100 and x <= 999:

            digit1 = x // 100
            digit2 = (x // 10) % 10
            digit3 = x % 10

            if digit1 == digit3:
                return True
            else:
                return False

        # Four digit numbers
        if x >= 1000 and x <= 9999:

            digit1 = x // 1000
            digit2 = (x // 100) % 10
            digit3 = (x // 10) % 10
            digit4 = x % 10

            if digit1 == digit4 and digit2 == digit3:
                return True
            else:
                return False

        # Five digit numbers
        if x >= 10000 and x <= 99999:

            digit1 = x // 10000
            digit2 = (x // 1000) % 10
            digit3 = (x // 100) % 10
            digit4 = (x // 10) % 10
            digit5 = x % 10

            if digit1 == digit5 and digit2 == digit4:
                return True
            else:
                return False

        # Six digit numbers
        if x >= 100000 and x <= 999999:

            digit1 = x // 100000
            digit2 = (x // 10000) % 10
            digit3 = (x // 1000) % 10
            digit4 = (x // 100) % 10
            digit5 = (x // 10) % 10
            digit6 = x % 10

            if digit1 == digit6 and digit2 == digit5 and digit3 == digit4:
                return True
            else:
                return False

        # Seven digit numbers
        if x >= 1000000 and x <= 9999999:

            digit1 = x // 1000000
            digit2 = (x // 100000) % 10
            digit3 = (x // 10000) % 10
            digit4 = (x // 1000) % 10
            digit5 = (x // 100) % 10
            digit6 = (x // 10) % 10
            digit7 = x % 10

            if (
                digit1 == digit7
                and digit2 == digit6
                and digit3 == digit5
            ):
                return True
            else:
                return False

        # Eight digit numbers
        if x >= 10000000 and x <= 99999999:

            digit1 = x // 10000000
            digit2 = (x // 1000000) % 10
            digit3 = (x // 100000) % 10
            digit4 = (x // 10000) % 10
            digit5 = (x // 1000) % 10
            digit6 = (x // 100) % 10
            digit7 = (x // 10) % 10
            digit8 = x % 10

            if (
                digit1 == digit8
                and digit2 == digit7
                and digit3 == digit6
                and digit4 == digit5
            ):
                return True
            else:
                return False

        # Nine digit numbers
        if x >= 100000000 and x <= 999999999:

            digit1 = x // 100000000
            digit2 = (x // 10000000) % 10
            digit3 = (x // 1000000) % 10
            digit4 = (x // 100000) % 10
            digit5 = (x // 10000) % 10
            digit6 = (x // 1000) % 10
            digit7 = (x // 100) % 10
            digit8 = (x // 10) % 10
            digit9 = x % 10

            if (
                digit1 == digit9
                and digit2 == digit8
                and digit3 == digit7
                and digit4 == digit6
            ):
                return True
            else:
                return False

        # Ten digit numbers
        if x >= 1000000000 and x <= 2147483647:

            digit1 = x // 1000000000
            digit2 = (x // 100000000) % 10
            digit3 = (x // 10000000) % 10
            digit4 = (x // 1000000) % 10
            digit5 = (x // 100000) % 10
            digit6 = (x // 10000) % 10
            digit7 = (x // 1000) % 10
            digit8 = (x // 100) % 10
            digit9 = (x // 10) % 10
            digit10 = x % 10

            if (
                digit1 == digit10
                and digit2 == digit9
                and digit3 == digit8
                and digit4 == digit7
                and digit5 == digit6
            ):
                return True
            else:
                return False

        # Just in case something somehow reaches here
        return False