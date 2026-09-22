"""
Linear Search Execution Time Measurement (Seconds)
Course: 02AML204 – Introduction to Artificial Intelligence
PRN: 25UAM053
Name: Saie Suresh Gaikwad
"""

import time


def linear_search(arr, target):
    """
    Linear Search: Sequentially checks each element in the array.
    Time Complexity: Best O(1), Avg/Worst O(n)
    """
    comparisons = 0

    for index in range(len(arr)):
        comparisons += 1
        if arr[index] == target:
            return index, comparisons

    return -1, comparisons


if __name__ == "__main__":
    DATA_SIZE = 100_000
    dataset = list(range(DATA_SIZE))

    # Test cases
    cases = {
        "Best Case (First Element Target)": dataset[0],                     # 0
        "Average Case (Midpoint Target)": dataset[DATA_SIZE // 2],          # 50,000
        "Worst Case (Last Element Target)": dataset[DATA_SIZE - 1],         # 99,999
        "Worst Case (Unsuccessful Search)": DATA_SIZE + 100,                # 100,100
    }

    print("==================================================")
    print(f" LINEAR SEARCH EXECUTION TIME (N = {DATA_SIZE:,})")
    print("==================================================\n")

    for case_name, target in cases.items():
        # Running batch iterations for stable sub-millisecond precision
        iterations = 100
        start_time = time.perf_counter()
        for _ in range(iterations):
            index, comparisons = linear_search(dataset, target)
        end_time = time.perf_counter()

        # Average elapsed time per call in seconds
        elapsed_time_sec = (end_time - start_time) / iterations

        print(f"--- {case_name} ---")
        print(f"Target Value:     {target}")
        print(f"Index Returned:   {index}")
        print(f"Comparisons Made: {comparisons}")
        print(f"Execution Time:   {elapsed_time_sec:.8f} sec\n")
