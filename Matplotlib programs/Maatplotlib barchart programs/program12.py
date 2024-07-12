"""

@Author: TarunSai
@Date: 2024-07-09
@Last Modified by: 
@Last Modified time:
@Title : Program to create bar plots with error bars on the same figure.

"""


def bar_chart(mean_velocity, std_dev_velocity):

    """

    description:
        This function is used to create bar plots with error bars on the same figure.
    
    parameters:
        mean_velocity, std_dev_velocity(list): data given and that we are going to plot graph.
            
    return:
        none

    """

    import matplotlib.pyplot as plt
    import numpy as np

   
    labels = ['A', 'B', 'C', 'D']


    fig, ax = plt.subplots()

    bars = ax.bar(labels, mean_velocity, yerr=std_dev_velocity, capsize=7, color='skyblue', edgecolor='blue')
    plt.show()


def main():
    mean_velocity = [0.2474, 0.1235, 0.1737, 0.1824]
    std_dev_velocity =  [0.3314, 0.2278, 0.2836, 0.2645]
    bar_chart(mean_velocity, std_dev_velocity)


if __name__ == "__main__":
    main()