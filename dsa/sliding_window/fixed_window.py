# Main Example
# The box size never changes.
# It stays exactly 3 items wide the entire time.
# It slides across a list of monthly sales to find the highest total.
def max_sales_of_three_months(sales, K):

    # 1. Calculate the first box manually (Jan + Feb + Mar)
    current_sum = sales[0] + sales[1] + sales[2]  # 10 + 20 + 30 = 60
    max_sum = current_sum
    print(f"Starting Box {sales[:K]} Sum: {current_sum}")

    # 2. Slide the box using a loop
    for i in range(K, len(sales)):
        incoming = sales[i]          # The new item entering the front
        outgoing = sales[i - K]      # The old item leaving the back

        # Shortcut: Update the running total directly
        current_sum = current_sum - outgoing + incoming

        # Track the highest total seen so far
        max_sum = max(max_sum, current_sum)

        print(f"Slid to index {i}! Current Sum: {current_sum}")

    print(f"--> Final Highest Sum: {max_sum}")

# Run it
# Array representing sales values
sales = [10, 20, 30, 40, 50]
K = 3  # The box size is strictly 3 items wide
max_sales_of_three_months(sales, K)
