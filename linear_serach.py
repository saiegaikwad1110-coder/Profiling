"""
Linear Search Execution Time Measurement (Seconds)
Course: 02AML204 – Introduction to Artificial Intelligence
PRN: 25UAM053
Name: Saie Suresh Gaikwad
"""

import time


def linear_search(arr: list[int], target: int) -> tuple[int, int]:
    """
    Linear Search: Checks every element sequentially from start to end.
    Time Complexity: Best O(1), Avg/Worst O(n)
    Space Complexity: O(1)
    """
    comparisons = 0

    for index in range(len(arr)):
        comparisons += 1
        if arr[index] == target:
            return index, comparisons

    return -1, comparisons


if __name__ == "__main__":
    DATA_SIZE = 1_000_000
    dataset = list(range(DATA_SIZE))

    # Test cases
    cases = {
        "Best Case (Target at Index 0)": 0,
        "Average Case (Target at Midpoint)": DATA_SIZE // 2,          # 500,000
        "Worst Case (Target at End)": DATA_SIZE - 1,                 # 999,999
        "Worst Case (Unsuccessful Search)": -1,                      # Missing element
    }

    print("==================================================")
    print(f" LINEAR SEARCH EXECUTION TIME (N = {DATA_SIZE:,})")
    print("==================================================\n")

    for case_name, target in cases.items():
        # Lower iteration count used because O(n) linear scanning takes longer than binary search
        iterations = 10
        start_time = time.perf_counter()
        for _ in range(iterations):
            index, comparisons = linear_search(dataset, target)
        end_time = time.perf_counter()

        elapsed_time_sec = (end_time - start_time) / iterations

        print(f"--- {case_name} ---")
        print(f"Target Value:     {target}")
        print(f"Index Returned:   {index}")
        print(f"Comparisons Made: {comparisons}")
        print(f"Execution Time:   {elapsed_time_sec:.8f} sec\n")
