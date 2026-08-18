# 27. Remove Element

nums = [0,1,2,2,3,0,4,2]

val = 2

def removeElements(nums, val):
    new = [n for n in nums if n!=val]
    return new

r = removeElements(nums, val)

print(r)
