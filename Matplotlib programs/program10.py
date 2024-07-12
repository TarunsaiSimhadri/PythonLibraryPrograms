"""

@Author: TarunSai
@Date: 2024-07-09
@Last Modified by: 
@Last Modified time:
@Title : Program to plot quantities which have an x and y position.

"""


def scatter_plot():

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

    x = 10
    y = 20
    x1 = 30
    y1 = 40
    plt.scatter(x1, y1)
    plt.scatter(x, y)
    plt.show()  
    

def main():

    scatter_plot()


if __name__ == "__main__":
    main()