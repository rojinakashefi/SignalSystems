import numpy as np
import scipy.signal
from matplotlib import pyplot as plt
from matplotlib import style
import math

style.use('ggplot')


def plot_design(title):
  plt.title(title)
  plt.xlabel('x-axis')
  plt.ylabel('y-axis')
  plt.legend()
  plt.show()


def plot_1a(a=1, b=0, title='1-A', label='X1(t)'):
  x1 = np.arange(-math.pi, math.pi, 0.01)
  y1 = np.sin((a * x1) + b)
  plt.plot(x1, y1, color="red", label=label)
  plot_design(title)


def plot_1b():
  x2 = np.arange(-5, 0)
  y2 = (-1 * x2) - 1
  plt.stem(x2, y2, linefmt='r--', label="X2[n]")
  x2 = np.arange(0, 6)
  y2 = (x2 * x2)
  plt.stem(x2, y2, linefmt="r--")
  plot_design('1-B')


def plot_1c(a=1, b=0, c=1, title="1-C", label="X3[N]"):
  x3 = np.arange(-5, 11)
  x_axis = x3.copy()
  x3 = a * x3 + b
  y3 = c * (np.exp(3 * x3) * np.heaviside(x3, 1) + 2 * scipy.signal.unit_impulse(len(x3)))
  plt.stem(x_axis, y3, linefmt='r--', label=label)
  plot_design(title)


def plot_1d():
  x4 = np.arange(-5, 5, 0.01)
  y4 = np.heaviside(x4 - 2, 0) - np.heaviside(x4 + 2, 0)
  plt.plot(x4, y4, color="red", label="X4(t)")
  plot_design('1-D')


def plot_1e():
  x5 = np.arange(-10, 11)
  y5 = np.cos(3 * x5)
  plt.stem(x5, y5, linefmt='r--', label="X5[n]")
  plot_design('1-e')


def plot_1f():
  x6 = np.arange(-10, 11)
  y6 = np.cos(3 * math.pi * x6)
  plt.stem(x6, y6, linefmt='r--', label="X7[n]")
  plot_design('1-F')


def plot_2a():
  plot_1a(2, -3, '2-A', 'X1[2t-3]')


def plot_2b():
  plot_1c(-5, -7, -2, '2-B', '-2X3[-5n-7]')


def plot_2c():
  plot_1a(-1, 3, '2-C', 'X1[-t+3]')


plot_1a()
plot_1b()
plot_1c()
plot_1d()
plot_1e()
plot_1f()

plot_2a()
plot_2b()
plot_2c()
