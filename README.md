# Profiling
# Binary Search – Best, Average and Worst Case Analysis

## 📌 Project Description

This project implements the **Binary Search algorithm** in Python and measures its execution time for three different cases:

* **Best Case**
* **Average Case**
* **Worst Case**

The execution time is measured using Python's `time.perf_counter()` function.

The program works on a large sorted array containing **1,000,000 elements**.

---

## 🎯 Objectives

The main objectives of this project are:

1. To implement Binary Search using Python.
2. To understand how Binary Search works on a sorted array.
3. To analyze Best, Average, and Worst Case performance.
4. To measure the execution time of each case.
5. To understand the time complexity of Binary Search.

---

## 🧠 What is Binary Search?

Binary Search is an efficient searching algorithm that works on a **sorted array**.

Instead of checking every element one by one, Binary Search repeatedly divides the search range into two halves.

### Steps

1. Set `low` to the first index.
2. Set `high` to the last index.
3. Find the middle element.
4. Compare the middle element with the target.
5. If the middle element is the target, return its index.
6. If the target is greater, search the right half.
7. If the target is smaller, search the left half.
8. Continue until the element is found or the search range becomes empty.

---

## 💻 Technologies Used

* **Programming Language:** Python
* **Time Measurement:** `time.perf_counter()`
* **Data Structure:** Sorted List
* **Array Size:** 1,000,000 elements

---

## 📂 Project Structure

```text
Binary-Search/
│
├── binary_search.py
└── README.md
```

---

## ⚙️ Program Details

The program creates a sorted array using:

```python
DATA_SIZE = 1_000_000
arr = list(range(DATA_SIZE))
```

The Binary Search function searches for a target element in this array.

Execution time is measured using:

```python
start_time = time.perf_counter()

result = binary_search(arr, target)

end_time = time.perf_counter()
```

The execution time is calculated as:

```text
end_time - start_time
```

---

## 📊 Test Cases

### 1. Best Case

```python
target = DATA_SIZE // 2
```

The middle element is found in the first comparison.

**Time Complexity:**

```text
O(1)
```

---

### 2. Average Case

```python
target = DATA_SIZE // 4
```

The target requires several comparisons before it is found.

**Time Complexity:**

```text
O(log n)
```

---

### 3. Worst Case

```python
target = DATA_SIZE - 1
```

The target is located near the end of the sorted array and requires several comparisons.

**Time Complexity:**

```text
O(log n)
```

---

## ⏱️ Time Complexity Analysis

| Case         | Time Complexity |
| ------------ | --------------- |
| Best Case    | O(1)            |
| Average Case | O(log n)        |
| Worst Case   | O(log n)        |

### Space Complexity

The Binary Search function uses a constant amount of additional memory.



## 🔍 Conclusion

Binary Search is much more efficient than Linear Search for searching in a sorted array.

The experiment shows that:

* The **Best Case** takes constant time, `O(1)`.
* The **Average Case** takes logarithmic time, `O(log n)`.
* The **Worst Case** takes logarithmic time, `O(log n)`.
* Binary Search requires the input array to be **sorted**.

Therefore, Binary Search is an efficient searching algorithm for large sorted datasets.



