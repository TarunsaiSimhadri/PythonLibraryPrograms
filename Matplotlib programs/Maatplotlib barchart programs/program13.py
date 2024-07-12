"""

@Author: TarunSai
@Date: 2024-07-09
@Last Modified by: 
@Last Modified time:
@Title : Program to create bar plots with error bars on the same figure attach a text label above each bar displaying men means (integer value).

"""


def bar_chart(mean_velocity, std_dev_velocity):

    """

    description:
        This function is used to create bar plots with error bars on the same figure attach a text label above each bar displaying men means (integer value).
    
    parameters:
        mean_velocity, std_dev_velocity(list): data given and that we are going to plot graph.
            
    return:
        none

    """

    import matplotlib.pyplot as plt
    import numpy as np

   
    labels = ['A', 'B', 'C', 'D']

    mean_values = [int(round(mean)) for mean in mean_velocity]

    fig, ax = plt.subplots()

    bars = ax.bar(labels, mean_velocity, yerr=std_dev_velocity, capsize=7, color='skyblue', edgecolor='blue')
    
    for bar, mean in zip(bars, mean_values):
        ax.text(bar.get_x() + bar.get_width()/2., bar.get_height() + 0.01, f'{mean}', ha='center', va='bottom', fontsize=8)
    plt.show()

def main():
    mean_velocity = [0.2474, 0.1235, 0.1737, 0.1824]
    std_dev_velocity =  [0.3314, 0.2278, 0.2836, 0.2645]
    bar_chart(mean_velocity, std_dev_velocity)


if __name__ == "__main__":
    main()