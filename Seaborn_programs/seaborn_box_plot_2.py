"""

@Author: TarunSai
@Date: 2024-07-09
@Last Modified by: 
@Last Modified time:
@Title : Program to draw a box plot of day by tips for a dataset given in the url.

"""


import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
def Box_plot():

    """

    description:
        This function is used to draw a box plot of day by tips for a dataset given in the url.
    
    parameters:
        None  
         
    return:
        none

    """
    
    url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/tips.csv"
    data = pd.read_csv(url)
    sns.boxplot(x = "day", y = "tip", data = data)
    plt.show() 
    

def main():
    Box_plot()


if __name__ == "__main__":
    main()