# Challenge 27 — Top K Frequent Elements

nums = [
    42, 7, 99, 13, 42, 88, 7, 42, 55, 99,
    13, 7, 101, 42, 88, 7, 13, 42, 55, 101,
    7, 88, 42, 99, 13, 42, 7, 101, 55, 88,
    42, 13, 7, 42, 99, 101, 7, 42, 13, 88
]

k = 3

def top_k_frequent(nums, k):
    count = {}

    for n in nums:
        if n in count:
            count[n] += 1
        else:
            count[n] = 1

    def get_score(key):
        return count[key]
# Take all the keys in the dictionary and sort them by their frequencies, highest first.
    return sorted(count, key=get_score, reverse=True)[:k]
  # return sorted(count, key=lambda x: count[x], reverse=True)[:k] (works same)


result = top_k_frequent(nums, k)
print(result)
