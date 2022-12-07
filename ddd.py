# Python program to show pyplot module
import matplotlib.pyplot as plt
from matplotlib.figure import Figure

# Creating a new figure with width = 5 inches
# and height = 4 inches
fig = plt.figure(figsize=(5, 4))

# Creating first axes for the figure
ax1 = fig.add_axes([1, 1, 1, 1])

# Creating second axes for the figure
ax2 = fig.add_axes([1, 0.5, 0.5, 0.5])

# Adding the data to be plotted
ax1.plot([2, 3, 4, 5, 5, 6, 6],
         [5, 7, 1, 3, 4, 6, 8])
ax2.plot([1, 2, 3, 4, 5],
         [2, 3, 4, 5, 6])

plt.show()
