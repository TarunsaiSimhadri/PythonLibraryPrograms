"""

@Author: TarunSai
@Date: 2024-07-09
@Last Modified by: 
@Last Modified time:
@Title : Program to draw scatter plot of sex against total_bill for a dataset given in the url.

"""


import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
def seaborn_scatter_plot():

    """

    description:
        This function is used to draw scatter plot of sex against total_bill for a dataset given in the url.
    
    parameters:
        None  
         
    return:
        none

    """
    
    url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/tips.csv"
    data = pd.read_csv(url)
    sns.scatterplot(x = "day", y = "total_bill", data = data)
    plt.show() 
    

def main():
    seaborn_scatter_plot()


if __name__ == "__main__":
    main()