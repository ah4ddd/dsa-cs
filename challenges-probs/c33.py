# C33 -- Merge Sorted Array

# SOL !
def mergesort(nums1, m, nums2, n):
    nums1[:] = sorted(nums1[:m] + nums2)

    return nums1

r = mergesort(nums1=[1,2,3,4,0,0,0], m=4, nums2=[2,4,5,6,7,8], n=6)

print(r)
