"""

@Author: TarunSai
@Date: 2024-07-09
@Last Modified by: 
@Last Modified time:
@Title : Program to draw a scatter graph taking a random distribution in X and Y and plotted against each other.

"""


def scatter_plot(x_points, y_points):

    """

    description:
        This function is used to draw a scatter graph taking a random distribution in X and Y and plotted against each other.
    
    parameters:
        x_points, y_points(array) : points that we are going to plot a scatter graph.
            
    return:
        none

    """

    import matplotlib.pyplot as plt
    
    plt.scatter(x_points, y_points)
    plt.title('scatter plot')
    plt.xlabel('x_points')
    plt.ylabel('y_points')
    plt.show()  
    

def main():
    import numpy as np
    x_points = np.random.randint(10)
    y_points = np.random.randint(10)
    scatter_plot(x_points, y_points)


if __name__ == "__main__":
    main()