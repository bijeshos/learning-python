import matplotlib.pyplot as plt
import numpy as np

# an empty figure with no axes
fig = plt.figure()
fig.suptitle('No axes on this figure')  # Add a title
plt.show()

# simple plot
plt.plot([1, 2, 3, 4])
plt.ylabel('some numbers')
plt.show()


# a figure with a 2x2 grid of Axes
fig, ax_lst = plt.subplots(2, 2)
plt.show()

# a simple plot
x = np.linspace(0, 2, 100)
plt.plot(x, x, label='linear')
plt.plot(x, x**2, label='quadratic')
plt.plot(x, x**3, label='cubic')
plt.xlabel('x label')
plt.ylabel('y label')
plt.title("Simple Plot")
plt.legend()
plt.show()


x = np.arange(0, 10, 0.2)
y = np.sin(x)
fig, ax = plt.subplots()
ax.plot(x, y)
plt.show()
