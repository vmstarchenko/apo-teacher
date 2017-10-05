import matplotlib
import matplotlib.pyplot as plt
from scipy.io.wavfile import read, write
import numpy as np


def draw_line(values, figsize=(4, 4)):
    """Нарисовать график функции по точкам, не отмечая оси и разметку."""
    fig = plt.figure(figsize=figsize)
    ax = fig.add_subplot(111)
    ax.plot(values)
    ax.axis('off')


def write_wav(filename, rate, data):
    """Записать wav файл."""
    write(filename, rate, np.array(data))
