"""

@Author: TarunSai
@Date: 2024-07-09
@Last Modified by: 
@Last Modified time:
@Title : Program to plot quantities which have an x and y position.

"""


def plot():

    """

    description:
        This function is used to plot quantities which have an x and y position.
    
    parameters:
        None
            
    return:
        none

    """

    import matplotlib.pyplot as plt
    import numpy as np

    x = np.array([0, 1, 2, 3])
    y = np.array([3, 8, 1, 10])
    z = np.array(['A', 'B', 'C', 'D'])
    p = np.array([20, 30, 40, 10])
    plt.plot(x,y)
    plt.show()
    plt.scatter(x,y)
    plt.show()
    plt.bar(z, y)
    plt.show()
    plt.pie(p, labels=z)
    plt.show()


def main():
    plot()


if __name__ == "__main__":
    main()