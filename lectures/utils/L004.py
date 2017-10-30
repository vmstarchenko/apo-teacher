import matplotlib.pyplot as plt
import numpy as np

from math import log


def plot_funcs():
    ranges = np.linspace(np.finfo(float).eps, 15, 100)
    funcs = [
        ['линия', 'red', lambda x: x],
        ['квадрат', 'blue', lambda x: x * x],
        ['константа', 'green', lambda x: 1],
        ['логорифм', 'orange', lambda x: log(x, 2)],
        ['n log(n)', 'yellow', lambda x: x * log(x, 2)],
    ]
    for label, color, func in funcs:
        values = np.fromiter(map(func, ranges), dtype='float')
        plt.plot(ranges, values, label=label, color=color)

    plt.xlim(0, 15)
    plt.ylim(0, 15)
    plt.legend()
    plt.show()


def main():
    plot_funcs()

if __name__ == "__main__":
    main()
