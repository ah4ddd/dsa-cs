# MAIN PROBLEM (Dynamic-Size Window (Stretchy Box))
# The box size changes.
# It expands to add items and only shrinks when a rule is broken.
# In this problem, we want to find the shortest part of
# the array that adds up to a sum of 7 or more.
def shortest_part_with_sum_seven(nums, target_sum):
    left = 0
    current_sum = 0
    min_length = float('inf')  # Proper mathematical infinity (no hardcoded 999)

    print(f"Searching in array: {nums} for target sum >= {target_sum}\n")

    for right in range(len(nums)):
        current_sum += nums[right]

        # While the current slice meets our goal, try to shrink it from the left
        while current_sum >= target_sum:
            current_window_size = right - left + 1
            min_length = min(min_length, current_window_size)

            # Print the actual real-time slice that successfully hit the target sum
            print(f"Found match! Slice: {nums[left : right + 1]} | Size: {current_window_size} | Sum: {current_sum}")

            # Shrink from the back edge
            current_sum -= nums[left]
            left += 1

    # If min_length never changed from infinity, it means no slice ever hit the target sum
    final_ans = min_length if min_length != float('inf') else 0
    print(f"\n--> Shortest part length found: {final_ans}")
    return final_ans


# =======================================================
# Test Inputs are now properly OUTSIDE the function
# =======================================================
nums = [2, 3, 1, 2, 4, 3]
target_sum = 7

shortest_part_with_sum_seven(nums, target_sum)



