import time


def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1


# Create a large array
DATA_SIZE = 1_000_000
arr = list(range(DATA_SIZE))


# ================= BEST CASE =================
# Target is the first element
target = 0

start_time = time.perf_counter()

result = linear_search(arr, target)

end_time = time.perf_counter()

print("LINEAR SEARCH - BEST CASE")
print("Target:", target)
print("Index:", result)
print("Execution Time:", end_time - start_time, "seconds")


# ================= AVERAGE CASE =================
# Target is in the middle
target = DATA_SIZE // 2

start_time = time.perf_counter()

result = linear_search(arr, target)

end_time = time.perf_counter()

print("\nLINEAR SEARCH - AVERAGE CASE")
print("Target:", target)
print("Index:", result)
print("Execution Time:", end_time - start_time, "seconds")


# ================= WORST CASE =================
# Target is the last element
target = DATA_SIZE - 1

start_time = time.perf_counter()

result = linear_search(arr, target)

end_time = time.perf_counter()

print("\nLINEAR SEARCH - WORST CASE")
print("Target:", target)
print("Index:", result)
print("Execution Time:", end_time - start_time, "seconds")