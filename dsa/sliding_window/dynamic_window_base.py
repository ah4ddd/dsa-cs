# Variable-Size Window (The Box Stretches and Shrinks)
# The box size changes.
# It expands to add items and only shrinks when a rule is broken.
# In this problem, we want to find the shortest part of
# the array that adds up to a sum of 7 or more.

# Our array of ordered numbers
nums = [2, 3, 1, 4]

print("--- RUNNING VARIABLE-SIZE WINDOW ---")

# --- STEP 1: Start small ---
left = 0
right = 0
print(f"Window: {nums[left:right+1]} | Size: {right - left + 1} | Sum: 2")

# --- STEP 2: STRETCH the right edge (Size becomes 2) ---
left = 0
right = 1
print(f"Window: {nums[left:right+1]} | Size: {right - left + 1} | Sum: 5")

# --- STEP 3: STRETCH the right edge again (Size becomes 3) ---
left = 0
right = 2
print(f"Window: {nums[left:right+1]} | Size: {right - left + 1} | Sum: 6")

# --- STEP 4: STRETCH the right edge again (Size becomes 4) ---
# The sum becomes 10 (2 + 3 + 1 + 4), which hits our target of 7!
left = 0
right = 3
print(f"Window: {nums[left:right+1]} | Size: {right - left + 1} | Sum: 10")

# --- STEP 5: SHRINK the left edge forward (Size drops to 3) ---
# Since the sum is 10 (plenty big), we move 'left' up to make the box smaller.
left = 1
right = 3
print(f"Window: {nums[left:right+1]} | Size: {right - left + 1} | Sum: 8")
