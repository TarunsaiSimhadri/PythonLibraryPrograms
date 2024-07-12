"""

@Author: TarunSai
@Date: 2024-07-09
@Last Modified by: 
@Last Modified time:
@Title : Program to plot two or more lines with different styles.

"""


def draw_lines(x_points, y1_points, y2_points):

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
    y2_points = np.array(y2_points)

    plt.plot(x_points, y1_points, color = 'blue', linewidth = '5.5')
    plt.plot(x_points, y2_points, color = 'green', linewidth = '6')
    plt.xlabel('x_points')
    plt.xlabel('y_points')
    x_lim = plt.xlim()
    y_lim = plt.ylim()
    new_xlim = (2.1, 4.5)
    new_ylim = (79, 630)
    plt.xlim(new_xlim)
    plt.ylim(new_ylim)

    print(x_lim, y_lim)
    print(new_xlim, new_ylim)
    plt.show()  
    

def main():

    x_points = [2, 3, 4]
    y1_points = [100, 200, 300]
    y2_points = [400, 500, 600]

    draw_lines(x_points, y1_points, y2_points)


if __name__ == "__main__":
    main()