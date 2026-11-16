"""
Assignment 1: Fibonacci numbers - non-recursive and recursive,
with time and space complexity analysis.

Series used: F(0) = 0, F(1) = 1, F(n) = F(n-1) + F(n-2)
"""
import time


def fib_iterative(n):
    """Non-recursive Fibonacci. Returns (value, number of steps)."""
    steps = 0
    if n <= 1:
        return n, 1
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
        steps += 1
    return b, steps


recursive_calls = 0


def fib_recursive(n):
    """Recursive Fibonacci. Counts calls in the global recursive_calls."""
    global recursive_calls
    recursive_calls += 1
    if n <= 1:
        return n
    return fib_recursive(n - 1) + fib_recursive(n - 2)


def main():
    global recursive_calls
    n = int(input("Enter n (try 25-30 to see the difference): "))
    if n < 0:
        print("n must be non-negative")
        return

    series = [fib_iterative(i)[0] for i in range(n + 1)]
    print("\nFibonacci series:", *series)

    start = time.perf_counter()
    value, steps = fib_iterative(n)
    t_iter = time.perf_counter() - start
    print(f"\nNon-recursive: F({n}) = {value}")
    print(f"  Loop iterations : {steps}")
    print(f"  Time taken      : {t_iter:.6f} s")

    recursive_calls = 0
    start = time.perf_counter()
    value = fib_recursive(n)
    t_rec = time.perf_counter() - start
    print(f"\nRecursive: F({n}) = {value}")
    print(f"  Function calls  : {recursive_calls}")
    print(f"  Time taken      : {t_rec:.6f} s")

    print("\nComplexity analysis")
    print("-" * 60)
    print(f"{'Method':<16}{'Time':<22}{'Space'}")
    print(f"{'Non-recursive':<16}{'O(n)':<22}O(1)")
    print(f"{'Recursive':<16}{'O(2^n)  (exponential)':<22}O(n) call stack")
    print("-" * 60)
    print("Non-recursive: one loop from 2..n, only two variables kept.")
    print("Recursive: T(n) = T(n-1) + T(n-2) + O(1), which grows like")
    print("  1.618^n (bounded by 2^n); the deepest chain of calls is n,")
    print("  so the stack needs O(n) space.")


if __name__ == "__main__":
    main()
