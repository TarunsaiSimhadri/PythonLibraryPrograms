"""

@Author: TarunSai
@Date: 2024-07-10
@Last Modified by: 
@Last Modified time:
@Title : Program to create bar plot of scores by group and gender Use multiple X values on the same chart for men and women.

"""


def bar_chart(means_men, means_women):

    """

    description:
        This function is used to create bar plot of scores by group and gender Use multiple X values on the same chart for men and women.
    
    parameters:
        means_men, means_women (tuple): data given and that we are going to plot graph.
            
    return:
        none

    """

    import matplotlib.pyplot as plt
    import numpy as np

    x = np.arange(len(means_men)) 

    bar_width = 0.35

    plt.bar(x - bar_width/2, means_men, bar_width, label='Men')
    plt.bar(x + bar_width/2, means_women, bar_width, label='Women')

   
    plt.xlabel('Groups')
    plt.ylabel('scores')
    plt.title('Popularity of Programming Languages')

    plt.show()  


def main():
    means_men = (22, 30, 35, 35, 26)
    means_women = (25, 32, 30, 35, 29)
    bar_chart(means_men, means_women)


if __name__ == "__main__":
    main()