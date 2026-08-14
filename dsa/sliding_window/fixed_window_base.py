# BASE EXAMPLE
# Fixed-Size Window (The Box Never Changes Size)

# Our array of ordered numbers
nums = [10, 20, 30, 40]

print("--- RUNNING FIXED-SIZE WINDOW ---")

# --- POSITION 1 (Indices 0, 1, 2) ---
left = 0
right = 2
window = nums[left : right + 1]  # Slices indices 0, 1, 2 -> [10, 20, 30]
window_sum = 10 + 20 + 30

print(f"Window: {window} | Size: {right - left + 1} | Sum: {window_sum}")


# --- POSITION 2 (Slide Right by 1 Step) ---
# To slide a fixed window, BOTH pointers move forward by 1
left = 1
right = 3
window = nums[left : right + 1]  # Slices indices 1, 2, 3 -> [20, 30, 40]

# Shortcut math: drop the old item (nums[0]), add the new item (nums[3])
window_sum = window_sum - nums[0] + nums[3]  # 60 - 10 + 40 = 90

print(f"Window: {window} | Size: {right - left + 1} | Sum: {window_sum}")
