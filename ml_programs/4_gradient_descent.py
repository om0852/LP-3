"""
Assignment 4: Gradient Descent to find the local minima of a function.
Example: y = (x + 3)^2 starting from x = 2.

Update rule: x_new = x_old - learning_rate * dy/dx
"""

try:
    import matplotlib.pyplot as plt
except ImportError:          # the plot is optional
    plt = None


def f(x):
    return (x + 3) ** 2


def gradient(x):
    return 2 * (x + 3)       # dy/dx


def gradient_descent(start, learning_rate=0.1, precision=1e-6, max_iterations=10000):
    x = start
    history = [x]
    for iteration in range(1, max_iterations + 1):
        x_new = x - learning_rate * gradient(x)
        step = abs(x_new - x)
        x = x_new
        history.append(x)
        if iteration <= 10 or iteration % 10 == 0:
            print(f"Iteration {iteration:>3}: x = {x:.6f}, y = {f(x):.6f}")
        if step < precision:          # converged
            break
    return x, iteration, history


def main():
    start = 2.0
    print(f"Function: y = (x + 3)^2, starting point x = {start}\n")
    x_min, iterations, history = gradient_descent(start)

    print(f"\nConverged after {iterations} iterations")
    print(f"Local minimum at x = {x_min:.4f}")
    print(f"Minimum value   y = {f(x_min):.6f}")

    if plt:
        xs = [i / 10 for i in range(-80, 31)]
        plt.plot(xs, [f(x) for x in xs], label="y = (x + 3)^2")
        plt.plot(history, [f(x) for x in history], "ro-", markersize=3, label="descent path")
        plt.xlabel("x")
        plt.ylabel("y")
        plt.legend()
        plt.title("Gradient descent")
        plt.savefig("gradient_descent.png")


if __name__ == "__main__":
    main()
