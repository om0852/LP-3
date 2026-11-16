"""
Assignment 4: 0-1 Knapsack using dynamic programming.

dp[i][w] = best value using the first i items with capacity w
dp[i][w] = max(dp[i-1][w],                         # skip item i
               value[i] + dp[i-1][w - weight[i]])   # take item i (if it fits)

Time complexity : O(n * W)
Space complexity: O(n * W)
"""


def knapsack_01(values, weights, capacity):
    n = len(values)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(capacity + 1):
            dp[i][w] = dp[i - 1][w]
            if weights[i - 1] <= w:
                take = values[i - 1] + dp[i - 1][w - weights[i - 1]]
                if take > dp[i][w]:
                    dp[i][w] = take

    # Trace back to find which items were chosen
    selected = []
    w = capacity
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i - 1][w]:
            selected.append(i)
            w -= weights[i - 1]
    selected.reverse()

    return dp, selected


def main():
    n = int(input("Enter number of items: "))
    values = list(map(int, input("Enter values  (space separated): ").split()))
    weights = list(map(int, input("Enter weights (space separated): ").split()))
    capacity = int(input("Enter knapsack capacity: "))

    if len(values) != n or len(weights) != n:
        print("Number of values/weights does not match n")
        return

    dp, selected = knapsack_01(values, weights, capacity)

    print("\nDP table (rows = items 0..n, columns = capacity 0..W):")
    for row in dp:
        print(" ".join(f"{cell:4}" for cell in row))

    print(f"\nMaximum value = {dp[n][capacity]}")
    print("Items selected:")
    for i in selected:
        print(f"  Item {i}: value = {values[i - 1]}, weight = {weights[i - 1]}")
    print("Total weight  =", sum(weights[i - 1] for i in selected))


if __name__ == "__main__":
    main()
