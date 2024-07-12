"""

@Author: TarunSai
@Date: 2024-07-09
@Last Modified by: 
@Last Modified time:
@Title : Program to create bar plot from a DataFrame.

"""


def bar_chart(data):

    """

    description:
        This function is used to create bar plot from a DataFrame.
    
    parameters:
        data (dict): data given and that we are going to plot graph.
            
    return:
        none

    """

    import matplotlib.pyplot as plt
    import numpy as np
    import pandas as pd

    data = pd.DataFrame(data)
    data_transposed = data.transpose()
    for index, row in data_transposed.iterrows():
        plt.bar(data.columns, row, alpha=0.8, label=f'Row {index}')


    plt.show()


def main():
    data = {
    'a': [2, 4, 6, 8, 10],
    'b': [8, 8, 4, 2, 2],
    'c': [5, 5, 7, 4, 3],
    'd': [7, 2, 7, 8, 3],
    'e': [6, 6, 8, 6, 2]
    }
    bar_chart(data)


if __name__ == "__main__":
    main()