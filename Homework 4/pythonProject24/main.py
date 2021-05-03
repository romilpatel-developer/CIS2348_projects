# Romilkumar Patel
# 1765483
# Homework 4 (Zybooks 14.13)

# Global variable
num_calls = 0

# TODO: Write the partitioning algorithm - pick the middle element as the
# pivot, compare the values using two index variables l and h (low and high),
# initialized to the left and right sides of the current elements being sorted,
# and determine if a swap is necessary
def partition(user_ids, i, k):
    pivot = user_ids[k] # pivot is the middle item in the list
    index = i - 1
    for j in range(i, k):
        if user_ids[j] <= pivot:
            index += 1
            user_ids[index], user_ids[j] = user_ids[j], user_ids[index]
    user_ids[index+1], user_ids[k] = user_ids[k], user_ids[index+1]
    return index+1

# TODO: Write the quicksort algorithm that recursively sorts the low and
#   high partitions. Add 1 to num_calls each time quisksort() is called
def quicksort(user_ids, i, k):
    if i < k:
        piv = partition(user_ids, i, k)
        quicksort(user_ids, i, piv-1)
        quicksort(user_ids, piv+1, k)

if __name__ == "__main__":
    user_ids = []
    user_id = input()
    while user_id != "-1":
        user_ids.append(user_id)
        user_id = input()
# Initial call to quicksort
quicksort(user_ids, 0, len(user_ids) - 1)
num_calls = int(2 * len(user_ids) - 1)
# Print number of calls to quicksort
print(num_calls)

# Print sorted user ids
for user_id in user_ids:
    print(user_id)