"""

@Author: TarunSai
@Date: 2024-07-09
@Last Modified by: 
@Last Modified time:
@Title : Program to draw a line using given axis values with suitable label in the x axis, y axis and a title.

"""


def draw_plot(x_points, y_points):

    """

    description:
        This function is used to draw a line using given axis values with suitable label in the x axis, y axis and a title.
    
    parameters:
        x_points, y_points(array) : points that we are going to plot a graph.
            
    return:
        none

    """

    import matplotlib.pyplot as plt
    import numpy as np
    
    x_points = np.array(x_points)
    y_points = np.array(y_points)
    plt.plot(x_points, y_points)
    plt.title('plotting')
    plt.xlabel('x_points')
    plt.ylabel('y_points')
    plt.show()  
    

def main():

    x_points = [2, 3, 4]
    y_points = [100, 200, 300]

    draw_plot(x_points, y_points)


if __name__ == "__main__":
    main()