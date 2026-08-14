# Variable-Size Window (The Box Stretches and Shrinks)
# The box size changes.
# It expands to add items and only shrinks when a rule is broken.
# In this problem, we want to find the shortest part of
# the array that adds up to a sum of 7 or more.

# Our array of ordered numbers
# jargon code
nums = [2, 3, 1, 4]
target_sum = 7

print("--- VISUALIZING EVERY SINGLE STEP ---")

left = 0
current_sum = 0

for right in range(len(nums)):
    # 1. EXPAND STEP
    current_sum += nums[right] # M
    current_box_slice = nums[left : right + 1]
    current_window_size = right - left + 1

    print(f"EXPAND  | Window: {str(current_box_slice):<12} | Size: {current_window_size} | Sum: {current_sum}")

    # 2. SHRINK STEP (Triggers only when sum is 7 or more)
    while current_sum >= target_sum:
        print(f"  ↳ MATCH HIT! (Sum {current_sum} >= {target_sum}). Shrinking from left...")

        # Subtract the item we are leaving behind
        current_sum -= nums[left]
        left += 1  # Pull the back edge forward

        # Calculate and print the newly shrunken window
        current_box_slice = nums[left : right + 1]
        current_window_size = right - left + 1
        print(f"  SHRINK  | Window: {str(current_box_slice):<12} | Size: {current_window_size} | Sum: {current_sum}")


# Because a sliding window cannot skip numbers,
# your box cannot just magically grab the 3 and
# the 4 while ignoring the 1.
# It is forced to take the whole continuous chain: [3, 1, 4].


# Clean Code
nums = [2, 3, 1, 4]
target_sum = 6

left = 0
current_sum = 0
min_length = float('inf')

for right in range(len(nums)):
    current_sum += nums[right]

    while current_sum >= target_sum:
        min_length = min(min_length, right - left + 1)
        current_sum -= nums[left]
        left += 1

print(f"Shortest Window Size Found: {min_length}")

