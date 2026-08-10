# C31 -- Integer to Roman

def intToRoman(num: int):
    integers = {
            1000: "M",
            900: "CM",
            500: "D",
            400: "CD",
            100: "C",
            90: "XC",
            50: "L",
            40: "XL",
            10: "X",
            9: "IX",
            5: "V",
            4: "IV",
            1: "I"
            }

    roman = ""

    for v, s in integers.items():
        while num >= v:
            roman += s
            num -= v

    return roman


r = intToRoman(3450)

print(r)

