"""

@Author: TarunSai
@Date: 2024-07-09
@Last Modified by: 
@Last Modified time:
@Title : Program to display the current axis limits values and set new axis values.

"""


def change_limits(x_points, y1_points):

    """

    description:
        This function is used to display the current axis limits values and set new axis values.
    
    parameters:
        x_points, y1_points(list) : points that we are going to plot a graph.
            
    return:
        none

    """

    import matplotlib.pyplot as plt
    import numpy as np

    x_points = np.array(x_points)
    y1_points = np.array(y1_points)

    plt.plot(x_points, y1_points, color = 'blue', linewidth = '5.5')
    plt.plot(x_points, color = 'green', linewidth = '6')
    plt.xlabel('x_points')
    plt.xlabel('y_points')
    plt.show()  
    

def main():

    x_points = [2, 3, 4]
    y1_points = [100, 200, 300]

    change_limits(x_points, y1_points )


if __name__ == "__main__":
    main()