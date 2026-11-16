"""
Assignment 3: Fractional Knapsack using the greedy method.

Greedy choice: pick items in decreasing order of value/weight ratio;
take a fraction of the item that does not fit completely.
Time complexity : O(n log n)  (sorting)
Space complexity: O(n)
"""


def fractional_knapsack(values, weights, capacity):
    items = sorted(
        zip(values, weights, range(1, len(values) + 1)),
        key=lambda item: item[0] / item[1],
        reverse=True,
    )

    total_value = 0.0
    remaining = capacity
    taken = []  # (item number, fraction taken, value gained)

    for value, weight, number in items:
        if remaining == 0:
            break
        if weight <= remaining:
            taken.append((number, 1.0, value))
            total_value += value
            remaining -= weight
        else:
            fraction = remaining / weight
            taken.append((number, fraction, value * fraction))
            total_value += value * fraction
            remaining = 0

    return total_value, taken


def main():
    n = int(input("Enter number of items: "))
    values = list(map(float, input("Enter values  (space separated): ").split()))
    weights = list(map(float, input("Enter weights (space separated): ").split()))
    capacity = float(input("Enter knapsack capacity: "))

    if len(values) != n or len(weights) != n:
        print("Number of values/weights does not match n")
        return
    if any(w <= 0 for w in weights):
        print("Weights must be positive")
        return

    print(f"\n{'Item':<6}{'Value':<10}{'Weight':<10}Ratio")
    for i in range(n):
        print(f"{i + 1:<6}{values[i]:<10g}{weights[i]:<10g}{values[i] / weights[i]:.2f}")

    total, taken = fractional_knapsack(values, weights, capacity)

    print(f"\n{'Item':<6}{'Fraction':<12}Value gained")
    for number, fraction, gained in taken:
        print(f"{number:<6}{fraction:<12.2f}{gained:.2f}")
    print(f"\nMaximum value in knapsack = {total:.2f}")


if __name__ == "__main__":
    main()
