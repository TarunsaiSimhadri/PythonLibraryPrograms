"""

@Author: TarunSai
@Date: 2024-07-09
@Last Modified by: 
@Last Modified time:
@Title : Program to plot two or more lines on same plot with suitable legends of each line.

"""


def draw_line(x_points, y1_points, y2_points):

    """

    description:
        This function is used to plot two or more lines on same plot with suitable legends of each line.
    
    parameters:
        x_points, y1_points, y2_points(array) : points that we are going to plot a graph.
            
    return:
        none

    """

    import matplotlib.pyplot as plt
    import numpy as np

    x_points = np.array(x_points)
    y1_points = np.array(y1_points)
    y2_points = np.array(y2_points)

    plt.plot(x_points, y1_points, label = 'x_points')
    plt.plot(x_points, y2_points, label = 'y_points')
    plt.legend()
    plt.show()  
    

def main():

    x_points = [2, 3, 4]
    y1_points = [100, 200, 300]
    y2_points = [400, 500, 600]

    draw_line(x_points, y1_points, y2_points)


if __name__ == "__main__":
    main()