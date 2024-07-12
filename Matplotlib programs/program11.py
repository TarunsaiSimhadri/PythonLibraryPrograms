
"""

@Author: TarunSai
@Date: 2024-07-09
@Last Modified by: 
@Last Modified time:
@Title : Program to plot several lines with different format styles in one command using arrays.

"""


def types_of_plots():

    """

    description:
        This function is used to plot several lines with different format styles in one command using arrays.
    
    parameters:
        None
            
    return:
        none

    """

    import matplotlib.pyplot as plt
    import numpy as np


    x = np.array([0, 10, 20, 30, 100])

    y1 = np.sin(x)
    y2 = np.cos(x)
    y3 = np.tan(x)

    plt.plot(x, y1, '-r', label='sin(x)')  # red solid line
    plt.plot(x, y2, '--g', label='cos(x)')  # green dashed line
    plt.plot(x, y3, ':b', label='tan(x)')  # blue dotted line

    plt.title('Multiple Lines with Different Styles')
    plt.xlabel('x')
    plt.ylabel('y')

    plt.legend()
    plt.show()
    


def main():

    types_of_plots()


if __name__ == "__main__":
    main()