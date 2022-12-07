import matplotlib.pyplot as plt
from matplotlib.figure import Figure
# initialize the data
x = [10, 20, 30, 40]
y = [20, 40, 60, 80]

# plotting the data
plt.plot(x, y)

# Adding the title
plt.title("Simple Plot")

# Adding the labels
plt.xlabel("Y-axis")
plt.ylabel("X-axis")
plt.show()


# year contains the x-axis values
# and e-india & e-bangladesh
# are the y-axis values for plotting

year = [1972, 1982, 1992, 2002, 2012]
e_india = [100.6, 158.61, 305.54, 394.96, 724.79]
e_bangladesh = [10.5, 25.21, 58.65, 119.27, 274.87]

# plotting of x-axis(year) and
# y-axis(power consumption)
#with different colored labels of two countries

plt.plot(year, e_india, color='orange',
         label='India')

plt.plot(year, e_bangladesh, color='g',
         label='Bangladesh')

# naming of x-axis and y-axis
plt.xlabel('Years')
plt.ylabel('Power consumption in kWh')

# naming the title of the plot
plt.title('Electricity consumption per capita\
 of India and Bangladesh')

plt.legend()
plt.show()
