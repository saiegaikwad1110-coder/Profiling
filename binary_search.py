import time


def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1


# Create a large sorted array
DATA_SIZE = 1_000_000
arr = list(range(DATA_SIZE))


# ================= BEST CASE =================
# Middle element is found in the first comparison
target = DATA_SIZE // 2

start_time = time.perf_counter()

result = binary_search(arr, target)

end_time = time.perf_counter()

print("BINARY SEARCH - BEST CASE")
print("Target:", target)
print("Index:", result)
print("Execution Time:", end_time - start_time, "seconds")


# ================= AVERAGE CASE =================
# Element requires several comparisons
target = DATA_SIZE // 4

start_time = time.perf_counter()

result = binary_search(arr, target)

end_time = time.perf_counter()

print("\nBINARY SEARCH - AVERAGE CASE")
print("Target:", target)
print("Index:", result)
print("Execution Time:", end_time - start_time, "seconds")


# ================= WORST CASE =================
# Element requires many comparisons
target = DATA_SIZE - 1

start_time = time.perf_counter()

result = binary_search(arr, target)

end_time = time.perf_counter()

print("\nBINARY SEARCH - WORST CASE")
print("Target:", target)
print("Index:", result)
print("Execution Time:", end_time - start_time, "seconds")