"""

@Author: TarunSai
@Date: 2024-07-09
@Last Modified by: 
@Last Modified time:
@Title : Program to plot two or more lines with different styles.

"""


def draw_line(x_points, y1_points):

    """

    description:
        This function is used to plot two or more lines with different styles.
    
    parameters:
        x_points, y1_points(list) : points that we are going to plot a graph.
            
    return:
        none

    """

    import matplotlib.pyplot as plt
    import numpy as np

    x_points = np.array(x_points)
    y1_points = np.array(y1_points)

    plt.plot(x_points, y1_points, marker = 'o', color = 'blue', linewidth = '2')
    plt.plot(x_points, marker = '^', color = 'green', linewidth = '2')
    plt.xlabel('x_points')
    plt.xlabel('y_points')
    plt.show()  
    

def main():

    x_points = [2, 3, 4]
    y1_points = [100, 200, 300]

    draw_line(x_points, y1_points )


if __name__ == "__main__":
    main()