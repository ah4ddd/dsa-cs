def merge_sort(arr):
    # Base case
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2

    left = arr[:mid] # Everything before index 2
    right = arr[mid:] # Everything from index 2 onward

    # Recursion
    left = merge_sort(left)
    right = merge_sort(right)

    return merge(left, right)


def merge(left, right):

    result = []

    i = 0
    j = 0

    while i < len(left) and j < len(right):

        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])

    return result


nums = [8, 3, 5, 4]

answer = merge_sort(nums)

print(answer)
