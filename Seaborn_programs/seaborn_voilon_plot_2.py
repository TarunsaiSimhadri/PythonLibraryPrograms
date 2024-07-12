"""

@Author: TarunSai
@Date: 2024-07-09
@Last Modified by: 
@Last Modified time:
@Title : Program to draw point plot of sex against total_bill for a dataset given in the url.

"""


import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
def seaborn_voilon_plot():

    """

    description:
        This function is used to draw point plot of sex against total_bill for a dataset given in the url.
    
    parameters:
        None  
         
    return:
        none

    """
    
    url = "https://github.com/mwaskom/seaborn-data/blob/master/iris.csv"
    data = pd.read_csv(url)
    sns.violinplot(x = "species", y = "sepal_length", data = data)
    plt.show() 
    

def main():
    seaborn_voilon_plot()


if __name__ == "__main__":
    main()