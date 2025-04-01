import matplotlib.pyplot as plt
import numpy as np
from IPython.core.pylabtools import figsize

# fig, ax = plt.subplots()
# ax.plot([1, 2, 3, 4], [1, 4, 2, 3])


# fig = plt.figure()             # an empty figure with no Axes
# fig, ax = plt.subplots()       # a figure with a single Axes
# fig, axs = plt.subplots(2, 2)  # a figure with a 2x2 grid of Axes
# a figure with one Axes on the left, and two on the right:
# fig, axs = plt.subplot_mosaic([['left', 'right_top'],
                               # ['left', 'right_bottom']])

# np.random.seed(19680801)  # seed the random number generator.
# data = {'a': np.arange(50),
#         'c': np.random.randint(0, 50, 50),
#         'd': np.random.randn(50)}
# data['b'] = data['a'] + 10 * np.random.randn(50)
# data['d'] = np.abs(data['d']) * 100
#
# fig, ax = plt.subplots(figsize=(5, 2.7), layout='constrained')
# ax.scatter('a', 'b', c='c', s='d', data=data)
# ax.set_xlabel('entry a')
# ax.set_ylabel('entry b')


# x = np.linspace(0, 2, 100)  # Sample data.
#
# # Note that even in the OO-style, we use `.pyplot.figure` to create the Figure.
# fig, ax = plt.subplots(figsize=(5, 2.7), layout='constrained')
# ax.plot(x, x, label='linear')  # Plot some data on the Axes.
# ax.plot(x, x**2, label='quadratic')  # Plot more data on the Axes...
# ax.plot(x, x**3, label='cubic')  # ... and some more.
# ax.set_xlabel('x label')  # Add an x-label to the Axes.
# ax.set_ylabel('y label')  # Add a y-label to the Axes.
# ax.set_title("Simple Plot")  # Add a title to the Axes.
# ax.legend()  # Add a legend.


# x = np.linspace(0, 2, 100)  # Sample data.
#
# plt.figure(figsize=(5, 2.7), layout='constrained')
# plt.plot(x, x, label='linear')  # Plot some data on the (implicit) Axes.
# plt.plot(x, x**2, label='quadratic')  # etc.
# plt.plot(x, x**3, label='cubic')
# plt.xlabel('x label')
# plt.ylabel('y label')
# plt.title("Simple Plot")
# plt.legend()


def my_plotter(ax, data1, data2, param_dict):
    """
    A helper function to make a graph.
    """
    out = ax.plot(data1, data2, **param_dict)
    return out

def my_plotter2(ax, data1, data2, param_dict):
    """
    A helper function to make a graph.
    """
    out = ax.scatter(data1, data2, **param_dict)
    return out

data1, data2, data3, data4 = np.random.randn(4, 100)
# fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(5, 2.7))
# # my_plotter(ax1, data1, data2, {'marker': 'x'})
# my_plotter2(ax1, data1, data2, {'marker': 'x'})
# my_plotter(ax2, data3, data4, {'marker': 'o'})


fig, ax = plt.subplots(figsize=(5, 2.7))
x = np.arange(len(data1))
ax.plot(x, np.cumsum(data1), color='blue', linewidth=3, linestyle='--')
l, = ax.plot(x, np.cumsum(data2), color='orange', linewidth=2) # ?
l.set_linestyle(':')



plt.show()