"""
Assignment 6: Analysis of quick sort - deterministic and randomized variants.

Deterministic: pivot is always the last element.
    Best/average O(n log n), worst O(n^2) (already sorted / reverse sorted input)
Randomized: pivot is chosen at random.
    Expected O(n log n) for every input; O(n^2) only with tiny probability.
Space: O(log n) average recursion depth, O(n) in the worst case.
"""
import random
import sys
import time

sys.setrecursionlimit(20000)

comparisons = 0


def partition(arr, low, high):
    """Lomuto partition with arr[high] as the pivot."""
    global comparisons
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        comparisons += 1
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


def quick_sort_deterministic(arr, low, high):
    if low < high:
        p = partition(arr, low, high)
        quick_sort_deterministic(arr, low, p - 1)
        quick_sort_deterministic(arr, p + 1, high)


def quick_sort_randomized(arr, low, high):
    if low < high:
        r = random.randint(low, high)          # random pivot
        arr[r], arr[high] = arr[high], arr[r]  # move it to the end
        p = partition(arr, low, high)
        quick_sort_randomized(arr, low, p - 1)
        quick_sort_randomized(arr, p + 1, high)


def run(sort_fn, data):
    """Sorts a copy of data. Returns (comparisons, seconds)."""
    global comparisons
    arr = data[:]
    comparisons = 0
    start = time.perf_counter()
    sort_fn(arr, 0, len(arr) - 1)
    elapsed = time.perf_counter() - start
    assert arr == sorted(data), "sort produced a wrong result"
    return comparisons, elapsed


def main():
    # Small demonstration
    sample = [38, 27, 43, 3, 9, 82, 10]
    a, b = sample[:], sample[:]
    quick_sort_deterministic(a, 0, len(a) - 1)
    quick_sort_randomized(b, 0, len(b) - 1)
    print("Input array          :", sample)
    print("Deterministic result :", a)
    print("Randomized result    :", b)

    # Analysis on different input types and sizes
    print(f"\n{'n':<7}{'Input':<10}{'Det. comps':<13}{'Det. time(s)':<15}"
          f"{'Rand. comps':<13}{'Rand. time(s)'}")
    print("-" * 71)
    for n in (500, 1000, 2000, 4000):
        inputs = {
            "random": [random.randint(1, 100000) for _ in range(n)],
            "sorted": list(range(n)),
            "reverse": list(range(n, 0, -1)),
        }
        for name, data in inputs.items():
            dc, dt = run(quick_sort_deterministic, data)
            rc, rt = run(quick_sort_randomized, data)
            print(f"{n:<7}{name:<10}{dc:<13}{dt:<15.5f}{rc:<13}{rt:.5f}")
        print()

    print("Observations")
    print("- Random input: both variants need about 1.39 * n * log2(n) comparisons.")
    print("- Sorted / reverse input: the deterministic variant degrades to")
    print("  n(n-1)/2 comparisons (O(n^2)) because every partition is")
    print("  completely unbalanced.")
    print("- The randomized variant stays at O(n log n) on every input,")
    print("  since no fixed input can force bad pivots.")


if __name__ == "__main__":
    main()
