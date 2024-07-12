"""

@Author: TarunSai
@Date: 2024-07-09
@Last Modified by: 
@Last Modified time:
@Title : Program to plot quantities which have an x and y position.

"""


def sub_plots():

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

    plt.subplot(1, 2, 1)
    plt.plot(x,y)

    x = np.array([0, 1, 2, 3])
    y = np.array([10, 20, 30, 40])

    plt.subplot(1, 2, 2)
    plt.plot(x,y)

    plt.show()

def main():

    sub_plots()


if __name__ == "__main__":
    main()