"""

@Author: TarunSai
@Date: 2024-07-09
@Last Modified by: 
@Last Modified time:
@Title : Program to draw a scatter plot using random distributions to generate balls of different sizes.

"""


def scatter_plot(math_marks, science_marks, marks_range):

    """

    description:
        This function is used to draw a scatter plot using random distributions to generate balls of different sizes.
    
    parameters:
        math_marks, science_marks(array) : points that we are going to plot a graph.
            
    return:
        none

    """

    import matplotlib.pyplot as plt
    
    plt.scatter(marks_range, math_marks, color = 'green', label = 'math_marks')
    plt.scatter(marks_range, science_marks, color = 'orange', label = 'science_marks')
    plt.title('scatter plot')
    plt.xlabel('marks_range')
    plt.ylabel('marks_scored')
    plt.legend()
    plt.show()  
    

def main():

    import numpy as np
    math_marks = [88, 92, 80, 89, 100, 80, 60, 100, 80, 34]
    science_marks = [35, 79, 79, 48, 100, 88, 32, 45, 20, 30]
    marks_range = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
    scatter_plot(math_marks, science_marks, marks_range)


if __name__ == "__main__":
    main()