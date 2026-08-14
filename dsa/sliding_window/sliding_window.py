def max_sum_subarray(nums, k):
    # 1. Get the sum of the very first window [1, 2, 3]
    window_sum = sum(nums[:k])
    max_sum = window_sum

    # 2. Slide the window across the rest of the array
    for i in range(k, len(nums)):
        incoming_element = nums[i]
        outgoing_element = nums[i - k]

        # Slide the window: Add the new, drop the old
        window_sum = window_sum + incoming_element - outgoing_element

        # Keep track of the highest sum we've seen so far
        max_sum = max(max_sum, window_sum)

    return max_sum

# Test it
numbers = [1, 2, 3, 4, 5, 6]
result = max_sum_subarray(numbers, k=3)
print(f"Max Sum: {result}")  # Outputs: 15



# STUPID EXAMPLE (Fixed-Size)
# Our array of ordered numbers
nums = [10, 20, 30, 40]

# --- WINDOW 1 (Looks at indices 0, 1, 2 ->) ---
# We calculate the first sum manually
window_sum = 10 + 20 + 30  # Sum is 60
print(f"Window 1 Sum: {window_sum}")


# --- WINDOW 2 (Slides right -> Looks at) ---
# Instead of doing 20 + 30 + 40, we use the shortcut:
outgoing = nums[0]  # The number 10 leaves the back
incoming = nums[3]  # The number 40 enters the front

# Update the math directly
window_sum = window_sum - outgoing + incoming  # 60 - 10 + 40 = 90
print(f"Window 2 Sum: {window_sum}")
