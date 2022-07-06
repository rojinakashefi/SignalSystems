import matplotlib.pyplot as plt
import numpy as np

step = 0.001
t = np.arange(-6, 6, step)
pi_number = np.pi


# Q1
def ak(signal, k, T0):
  w0 = 2 * pi_number / T0
  # under integral
  x = signal * np.cos(k * w0 * t)
  # caluclating integral
  return (2 / T0) * np.sum(x) * step


def bk(signal, k, T0):
  w0 = 2 * pi_number / T0
  # under integral
  x = signal * np.sin(k * w0 * t)
  # caluclating integral
  return (2 / T0) * np.sum(x) * step


# Q2
def fourier(signal, c, T0):
  w0 = 2 * pi_number / T0
  y = np.zeros((len(t),))
  y += ak(signal, 0, T0) / 2
  # include c
  for k in range(1, c + 1):
    y += ak(signal, k, T0) * np.cos(k * w0 * t) + \
         bk(signal, k, T0) * np.sin(k * w0 * t)
  return y


def plot(t, x):
  for c in range(0, 11):
    plt.plot(t, x, 'red', label="x(t)")
    plt.plot(t, fourier(x / 2, c, 6), 'blue', label="c=" + str(c))
    plt.legend()
    plt.show()

# Q3
x = np.heaviside(t, 1) + np.heaviside(-t - 3, 1) + \
    np.heaviside(-t + 3, 1) - 1
plot(t, x)
