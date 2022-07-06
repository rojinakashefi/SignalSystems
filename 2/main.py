import numpy
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style


def draw_plot(x, y, label, type="continuous"):
  if type == "discrete":
    plt.stem(x, y, label=label)
  else:
    plt.plot(x, y, label=label)
  plt.title(label)
  plt.xlabel('t')
  plt.ylabel(label)
  plt.legend()
  plt.show()


# Q1
def convolution(x, h, step):
  x = np.concatenate([np.zeros((len(h) - 1,)), x, np.zeros((len(h) - 1,))])
  h = h[::-1]
  return np.array([np.sum(x[i:i + len(h)] * h * step) for i in range(len(x) - len(h) + 1)])


def x1(t):
  return np.heaviside(t - 10, 1) - np.heaviside(t, 1)


def x2(t):
  a = np.empty(t.shape)
  for i in range(len(t)):
    if (t[i] > 0) and (t[i] < 5):
      a[i] = t[i]
    elif (t[i] >= 5) and (t[i] < 10):
      a[i] = 5 - t[i]
    else:
      a[i] = 0
  return a


def Q_3():
  n = np.arange(-20, 30, 1)
  h = np.power(0.9, n) * (np.heaviside(n - 5, 1) - np.heaviside(n, 1))
  x = np.power(1 / 3, n) * (np.heaviside(n, 1) - np.heaviside(n - 10, 1))
  y = convolution(x, h, 1)
  y = y[int(len(y) / 4): -1 * int(len(y) / 4) - 1]
  draw_plot(n, y, 'Y[n]', "discrete")


style.use('ggplot')
x_range = np.arange(-20, 30, 0.01)
# Q2
draw_plot(x_range, x1(x_range), 'x1')
draw_plot(x_range, x2(x_range), 'x2')
x3 = convolution(x1(x_range), x2(x_range), 0.01)
x3 = x3[int(len(x3) / 4): -1 * int(len(x3) / 4) - 1]
draw_plot(x_range, x3, 'x3')
# Q3
Q_3()
