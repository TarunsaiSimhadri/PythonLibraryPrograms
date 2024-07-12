"""

@Author: TarunSai
@Date: 2024-07-09
@Last Modified by: 
@Last Modified time:
@Title : Program to display a pie chart with the data in the csv file.

"""


def pie_chart():

    """

    description:
        This function is used to display a pie chart with the data in the csv file.
    
    parameters:
        None
            
    return:
        none

    """

    import matplotlib.pyplot as plt
    import numpy as np
    import pandas as pd

    data = pd.read_csv('test.csv')
    x = data['counrtry']
    y = data['gold_medal']

    plt.pie(y, labels = x)
    plt.title("pie chart for given data")
    plt.show()

def main():
    pie_chart()


if __name__ == "__main__":
    main()