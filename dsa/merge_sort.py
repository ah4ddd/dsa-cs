def merge_sort(arr):

    # -------------------------------
    # BASE CASE
    # -------------------------------
    # If the list has 0 or 1 element,
    # it is already sorted.
    # Stop the recursion and return it.
    if len(arr) <= 1:
        return arr

    # Find the middle index of the list.
    mid = len(arr) // 2

    # Split the list into two halves.
    # Left gets everything BEFORE mid.
    left = arr[:mid]

    # Right gets everything FROM mid onward.
    right = arr[mid:]

    # --------------------------------
    # RECURSION
    # --------------------------------
    # Sort the left half.
    # This pauses the current function,
    # creates a NEW merge_sort() call,
    # and waits until it returns
    # a sorted left half.
    left = merge_sort(left)

    # Sort the right half.
    # Again, pause this function,
    # recursively sort the right side,
    # and wait for the sorted result.
    right = merge_sort(right)

    # At this point:
    # left is sorted.
    # right is sorted.
    #
    # Now combine both sorted halves
    # into one fully sorted list.
    return merge(left, right)


def merge(left, right):

    # This will store the final merged list.
    result = []

    # i walks through the left list.
    i = 0

    # j walks through the right list.
    j = 0

    # Compare both lists until one is exhausted.
    while i < len(left) and j < len(right):

        # If the current element in the left
        # list is smaller...
        if left[i] < right[j]:

            # ...put it into the result.
            result.append(left[i])

            # Move to the next element
            # in the left list.
            i += 1

        else:
            # Otherwise the right element
            # is smaller (or equal),
            # so add it.
            result.append(right[j])

            # Move to the next element
            # in the right list.
            j += 1

    # One list may still have elements left.
    # Add ALL remaining elements
    # from the left list.
    result.extend(left[i:])

    # Add ALL remaining elements
    # from the right list.
    result.extend(right[j:])

    # Return one fully merged,
    # fully sorted list.
    return result


# Original unsorted list.
nums = [8, 3, 5, 4, 9, 15, 18, 20]

# Start Merge Sort.
# The function will recursively split,
# recursively sort,
# then recursively merge.
answer = merge_sort(nums)

# Print the final sorted list.
print(answer)
