# Fixed Sliding Window
# You have a box locked at a size of 3.
# As you traverse (move forward), you step exactly one number ahead.
# You leave one number behind out the back of the box.
# You output the sum of the specific numbers currently trapped
# inside your box at that exact moment.


# Our array of ordered numbers
nums = [10, 20, 30, 40, 60, 70]
K = 3  # The fixed size of our window

print("--- RUNNING FIXED-SIZE WINDOW WITH A LOOP ---")

# 1. Position 1: Calculate the very first window slice dynamically
current_sum = sum(nums[:K])  # 10 + 20 + 30 = 60
print(f"Window: {nums[:K]} | Sum: {current_sum}")

# 2. Position 2 onwards: The loop automatically slides the window right
# 'right' starts at index 3 (the number 40) and goes to the end
for right in range(K, len(nums)):
    outgoing_item = nums[right - K]  # Dynamically finds the item leaving the back
    incoming_item = nums[right]      # Dynamically finds the item entering the front

    # The shortcut math updates the window total instantly
    current_sum = current_sum - outgoing_item + incoming_item

    # Dynamic slice calculation to print the current box
    current_box_slice = nums[right - K + 1 : right + 1]
    print(f"Window: {current_box_slice} | Sum: {current_sum}")
