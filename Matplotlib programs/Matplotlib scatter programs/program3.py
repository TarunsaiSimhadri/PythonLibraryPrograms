"""

@Author: TarunSai
@Date: 2024-07-09
@Last Modified by: 
@Last Modified time:
@Title : Program to draw a scatter plot using random distributions to generate balls of different sizes.

"""


def scatter_plot(x_points, y_points, sizes):

    """

    description:
        This function is used to draw a scatter plot using random distributions to generate balls of different sizes.
    
    parameters:
        x_points, y_points(array) : points that we are going to plot a graph.
            
    return:
        none

    """

    import matplotlib.pyplot as plt
    
    plt.scatter(x_points, y_points, s = sizes, facecolors = 'none', edgecolors='green')
    plt.title('scatter plot')
    plt.xlabel('x_points')
    plt.ylabel('y_points')
    plt.show()  
    

def main():

    import numpy as np
    x_points = np.random.randn(100)
    y_points = np.random.randn(100)
    sizes = np.random.randn(100)
    scatter_plot(x_points, y_points, sizes)


if __name__ == "__main__":
    main()