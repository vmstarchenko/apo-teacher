import matplotlib.pyplot as plt
import numpy as np

from timeit import timeit as ti
from time import time as clock


def timeit(func, args):
    """Меряет время вызова функции.

    Вызывает ``calls'' раз функцию ``func'' с аргументами ``*args'' и
    ``kargs''. Возвращает среднее время вызова в секундах.

    """

    # time = ti('func(*args, **kargs)', number=calls, globals=locals())
    # return time / calls

    start = clock()
    func(*args)
    end = clock()

    return end - start


def compare_functions_time(funcs, labels, data_generator, data_size_generator,
                           title, xlabel, ylabel, calls):
    """\    time function."""

    data_sizes = list(data_size_generator)
    times_number = len(data_sizes)
    funcs_number = len(funcs)
    funcs_times = np.zeros(shape=(funcs_number, times_number))
    for call in range(calls):
        for j in range(times_number):
            data = data_generator(data_sizes[j])
            timeit(funcs[0], data)
            for i in range(funcs_number):
                func = funcs[i]
                start = clock()
                func(*data)
                end = clock()
                ti = end - start
                funcs_times[i, j] += ti

    funcs_times /= calls

    ax = plt

    ax.title(title)
    ax.xlabel(xlabel)
    ax.ylabel(ylabel)

    for func_times, label in zip(funcs_times, labels):
        ax.plot(data_sizes, func_times, label=label)

    ax.grid()
    ax.legend()

    return ax
